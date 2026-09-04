# Thelma & Louise

ERP interne de gestion des droits et de la distribution pour Les Films du Losange.

Ce dépôt documente la conception et le développement progressif de l'outil.

## Statut actuel

**Phase 0 — Cadrage & maquettage.** La maquette interactive couvre désormais 7
modules (Tableau de bord, Films & droits, Contrats, Ventes, Festivals, Matériels,
Subventions). Aucun code applicatif réel n'existe
encore : la maquette est en HTML/CSS/JS statique, avec des données fictives, pour
valider le concept avant le développement.

Voir [`docs/roadmap.md`](docs/roadmap.md) pour le plan complet et
[`CHANGELOG.md`](CHANGELOG.md) pour l'historique des avancées.

## Structure du dépôt

```
thelma-louise-erp/
├── README.md
├── CHANGELOG.md
├── docs/
│   └── roadmap.md        # roadmap détaillée, modules, priorités
└── mockups/
    ├── v1-dashboard.html # première version (4 modules)
    └── v2-dashboard.html # version actuelle (7 modules)
```

## Voir la maquette

Voir [`mockups/v3-dashboard.html`](https://thelma-tertrais.github.io/thelma-louise/mockups/v9-dashboard.html)
pour la maquette interactive (ouvre la version rendue via GitHub Pages).

Ou en local : ouvrir `mockups/v9-dashboard.html` directement dans un navigateur —
aucune installation nécessaire.

## Modules prévus

1. Catalogue & droits (films, territoires, médias, échéances)
2. Contrats & tiers (licenciés, coproducteurs, documents juridiques)
3. Ventes (France / international)
4. Servicing & matériels (DCP, masters, livraisons)
5. Festivals (soumissions, sélections)
6. Finance (facturation, budgets)
7. Subventions (CNC et autres)

## Auteur

Projet développé en solo, avec Claude comme assistant de conception et de code.
