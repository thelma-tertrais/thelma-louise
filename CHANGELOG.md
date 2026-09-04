# Changelog

## Non publié

### Ajouté
- `mockups/v8-dashboard.html` : dans le tiroir "Suivi des factures", un champ
  mots-clés + bouton "Générer le mail" qui compose un objet et un corps de mail de
  relance, avec bouton "Copier le texte"
  - mots-clés reconnus : ton ferme/sévère, urgent, pénalités/intérêts, délai/
    échelonnement, ton amical/cordial — chacun modifie le texte généré
  - tout mot-clé non reconnu est repris tel quel dans une ligne "Points
    supplémentaires à mentionner"

### Note de portée
- Génération basée sur des règles/templates, pas un vrai appel à un modèle de
  langage : le fichier est ouvert en local, sans connexion à une IA. La vraie
  version brancherait ceci sur un LLM pour un texte plus naturel et plus flexible
  face à des mots-clés imprévus — phase 6 de la roadmap.

## Précédent

### v7
- Timeline de suivi de facture + interrupteur de relance automatique

### v6
- Fix : ouverture du PDF du contrat via Blob au lieu d'une data URI directe

### v5
- PDF du contrat consultable depuis le tiroir (embarqué en base64)
- Génération d'un vrai PDF de facture (jsPDF) depuis les données du contrat

### v4
- Tiroir contrat cliquable avec détail complet, navigation contrat → facture
- Exemple fonctionnel d'extraction de contrat PDF (`exemples/`)

### v3
- Facturation automatique depuis les contrats (bouton isolé) + suivi des factures
  et relances

### v2
- Trois nouveaux modules : Contrats, Matériels (servicing), Subventions

### v1
- Maquette interactive v1 : tableau de bord, catalogue & droits (avec panneau de
  détail par film), ventes, festivals
- Identité : nom "Thelma & Louise", palette bleu clair, clin d'œil au losange dans le
  logo
- Roadmap détaillée en 7 phases (`docs/roadmap.md`)
