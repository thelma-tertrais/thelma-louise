# Thelma & Louise

ERP interne de gestion des droits et de la distribution pour Le Films du Losange.

Ce dépôt documente la conception et le développement progressif d'un outil destiné à
remplacer, module par module, le système actuel (AVEDIS).

## Statut actuel

**Phase 0 — Cadrage & maquettage.** Une première maquette interactive du tableau de
bord et de trois modules (Films & droits, Ventes, Festivals) a été produite pour
présentation à l'équipe. Aucun code applicatif réel n'existe encore : la maquette est
en HTML/CSS/JS statique, avec des données fictives, pour valider le concept avant le
développement.

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
    └── v1-dashboard.html # maquette interactive (ouvrir dans un navigateur)
```

## Voir la maquette

Ouvrir `mockups/v1-dashboard.html` directement dans un navigateur — aucune
installation nécessaire.

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
