# Changelog

## Non publié

### Ajouté
- `mockups/v4-dashboard.html` : les lignes de Contrats sont cliquables et ouvrent un
  tiroir de détail (licencié, territoire, support, montant, échéance, signature) ;
  bouton "Générer une facture" qui bascule vers l'aperçu de facture, avec retour
  possible au contrat
- `exemples/contrat-exemple.pdf` + `exemples/extraction_contrat.py` : exemple
  fonctionnel d'extraction de données depuis un contrat PDF fictif (regex),
  utilisé comme preuve de concept pour le module de facturation automatique
- Le contrat "Chambre 12 / CineWave GmbH" dans la maquette est relié à cet exemple
  (mention "document source" dans son tiroir de détail)

### Note de portée
- L'extraction par regex démontrée dans `exemples/` est fragile : elle dépend de la
  formulation exacte de ce contrat précis. Une extraction robuste sur des contrats
  hétérogènes nécessitera une approche par LLM plutôt que des regex fixes.
- La lecture automatique de contrats réels et l'envoi de relances par email restent
  du développement backend réel (phase 2/3 de la roadmap), pas de la maquette.

## Précédent

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
