# Visuels LinkedIn Rield

Visuels publiés sur la page LinkedIn de Rield. Dépôt public : les images sont récupérées par Metricool via leur adresse `raw.githubusercontent.com`.

## Organisation

- `AAAA-MM/` : visuels du mois, un fichier par slide (`sujet-1.png`, `sujet-2.png`...).
- `kit/` : charte et outils pour produire les visuels.
  - `base.css` : couleurs, typographies et composants Rield.
  - `fonts/` : polices embarquées (Outfit pour les titres, Playfair Display noir italique pour le mot en accent, Poppins pour le texte). Licences OFL incluses.
  - `render.py` : transforme un fichier HTML en PNG 1080x1350.
  - `exemples/` : un carrousel et une image de référence.

## Charte

- Couleurs : Dark Forest `#1A3A34`, Lime Volt `#00E64D`, Teal Mid `#2D6B5E`, Off-White `#F2F0EC`.
- Titres en Outfit gras, avec un mot ou une fin de phrase en italique serif (`<em>`), en vert lime sur fond sombre.
- Petit libellé en capitales espacées en haut de slide (`.label`), mot-symbole RIELD en bas à gauche, pagination ou rield-rm.com en bas à droite.
- Alterner fonds sombres (`.dark`) et clairs (`.light`) dans un carrousel. Couverture et dernière slide en sombre.
- Format 1080x1350 (portrait). Carrousel : 5 à 7 slides. Image seule : 1 slide.
- Pas de tiret cadratin, pas d'emoji, sources citées en pied de slide quand il y a des chiffres.

## Produire un visuel

```
cp kit/exemples/carrousel-marche.html kit/brouillon.html   # partir d'un exemple, réécrire le contenu
python3 kit/render.py kit/brouillon.html 2026-11 sujet
```

Puis supprimer `kit/brouillon.html`, committer les PNG et utiliser :
`https://raw.githubusercontent.com/xavierjarousseau-spec/rield-visuels/main/<AAAA-MM>/<sujet>-<n>.png`
