# Changelog

## Non publié

### Ajouté
- `mockups/v5-dashboard.html` :
  - Le contrat "Chambre 12" a un lien "contrat-exemple.pdf" cliquable dans son
    tiroir de détail, qui ouvre le vrai PDF (embarqué en base64 dans le fichier,
    donc la maquette reste autonome, un seul fichier à partager)
  - Le bouton de la facture générée télécharge un vrai PDF (via jsPDF, chargé
    depuis un CDN), mis en forme et rempli avec les données du contrat

### Note de portée
- Le PDF de facture généré ici est un gabarit simple pour la démo — la vraie
  version en production devra respecter les mentions légales obligatoires sur les
  factures françaises (numéro de TVA, mentions de pénalités de retard, etc.)

## Précédent

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
