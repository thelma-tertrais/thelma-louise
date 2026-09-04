"""
Exemple d'extraction de données structurées à partir d'un contrat de licence PDF.

Approche démontrée ici : extraction par expressions régulières, adaptées à la
structure de CE contrat (articles numérotés, formulations types). C'est la manière
la plus simple de démarrer, mais elle est fragile : elle suppose que tous les
contrats de Le Films du Losange suivent à peu près le même gabarit rédactionnel.

En production, avec des contrats hétérogènes (négociés par différents juristes,
années différentes, langues différentes), une extraction par LLM (prompt à Claude
avec le texte du contrat, demandant un JSON structuré) est beaucoup plus robuste
face aux variations de formulation — voir la note en bas de fichier.
"""

import pdfplumber
import re
import json

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_contract_data(text):
    data = {}
    # Le PDF coupe les phrases sur plusieurs lignes ; on aplatit en une seule
    # ligne pour que les regex n'aient pas à gérer les retours à la ligne.
    flat = re.sub(r"\s+", " ", text)

    # Référence du contrat
    m = re.search(r"Réf\. contrat\s*:\s*([A-Z0-9\-]+)", text)
    data["reference"] = m.group(1) if m else None

    # Licencié (partie autre que Le Films du Losange, en gras/majuscules après "ET")
    m = re.search(r"ET\s*\n?([A-Z][A-Z0-9\s]+GMBH|[A-Z][A-Z0-9\s]+(?:SAS|SARL|LTD|INC))", text)
    data["licencie"] = m.group(1).strip() if m else None

    # Film concerné
    m = re.search(r"intitulée\s*«\s*(.+?)\s*»", text)
    data["film"] = m.group(1).strip() if m else None

    # Territoire (la phrase se termine par une parenthèse fermante avant le point)
    m = re.search(r"territoire suivant\s*:\s*(.+?\))\.", flat)
    data["territoire"] = m.group(1).strip() if m else None

    # Support / mode d'exploitation
    m = re.search(r"limités à l'exploitation en\s*(.+?\(SVOD/VOD\))", flat)
    data["support"] = m.group(1).strip() if m else None

    # Montant (recherche d'un motif "X EUR" en chiffres, espaces/retours à la ligne possibles)
    m = re.search(r"\(([\d\s]+)\s*EUR\)", text)
    data["montant_eur"] = int(re.sub(r"\s+", "", m.group(1))) if m else None

    # Échéance de la licence
    m = re.search(r"au plus tard le\s*(\d{1,2}\s+\w+\s+\d{4})", text)
    data["echeance_licence"] = m.group(1) if m else None

    # Délai de paiement
    m = re.search(r"délai de\s*(trente|soixante|quinze)\s*\(\d+\)\s*jours", text)
    data["delai_paiement"] = m.group(1) if m else None

    # Date de signature
    m = re.search(r"Fait à \w+, le\s*(\d{1,2}\s+\w+\s+\d{4})", text)
    data["date_signature"] = m.group(1) if m else None

    return data

if __name__ == "__main__":
    text = extract_text("contrat-exemple.pdf")
    data = extract_contract_data(text)
    print(json.dumps(data, indent=2, ensure_ascii=False))
