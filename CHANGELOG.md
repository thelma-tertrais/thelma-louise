# Changelog

## Non publié

### Ajouté
- `mockups/v7-dashboard.html` : les lignes de "Suivi des factures" sont cliquables
  et ouvrent un tiroir avec :
  - une timeline verticale des étapes (émission, envoi, rappels, échéance,
    relances, paiement), avec l'étape en cours mise en évidence
  - un interrupteur "Relance automatique" (activable/désactivable), avec un texte
    qui se met à jour en direct selon l'état

### Note de portée
- L'interrupteur est purement visuel dans la maquette (état gardé en mémoire le
  temps de la session, pas persisté). La vraie automatisation des relances (envoi
  d'email programmé) reste un développement backend réel — phase 6 de la roadmap.

## Précédent

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
