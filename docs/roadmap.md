# Roadmap

Projet solo, remplacement progressif d'AVEDIS module par module. Estimation totale
pour une parité complète : 2 à 3 ans, en construisant chaque module comme un outil
utilisable seul avant de passer au suivant.

## Phase 0 — Cadrage & maquette (en cours)

- [x] Analyse de l'outil existant (AVEDIS) et de son organisation par modules
- [x] Maquette interactive : tableau de bord, catalogue & droits, ventes, festivals
- [ ] Retours de l'équipe sur la maquette
- [ ] Priorisation du premier module réel à développer

## Phase 1 — Socle : Films & Droits (4–8 semaines)

- Catalogue de films (métadonnées, quote-parts de coproduction)
- Table des droits : territoire × média × langue × dates × licencié
- Alertes d'échéance de droits

## Phase 2 — Tiers & Contrats (3–5 semaines)

- Fiches tiers (licenciés, ayants droit, coproducteurs)
- Enregistrement des contrats liés aux droits
- Stockage de documents avec métadonnées

## Phase 3 — Ventes (6–10 semaines)

- Un seul périmètre pour commencer (France ou international)
- Pipeline commercial, conditions de deal
- Facturation liée aux droits, logique de minimum garanti / recoupement

## Phase 4 — Servicing & Matériels (4–6 semaines)

- Inventaire des matériels (DCP, masters)
- Suivi des livraisons aux licenciés

## Phase 5 — Festivals (3–4 semaines)

- Soumissions, statuts, contacts

## Phase 6 — Finance & Subventions (8–12 semaines)

- Factures fournisseurs, règlements, budgets par film
- Suivi des subventions (CNC, etc.)

## Phase 7 — Marketing, reporting, finition (continu)

## Choix techniques (à confirmer)

- Stack encore à trancher — privilégier une techno mature avec un bon socle
  admin/CRUD (Django, Rails, ou Postgres + FastAPI/Next.js)
- Migration en parallèle d'AVEDIS, pas de bascule brutale
