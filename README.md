# Visuels LinkedIn Rield

Visuels publiés sur la page LinkedIn de Rield. Dépôt public : les images sont récupérées par Metricool via leur adresse `raw.githubusercontent.com`.

## Organisation

- `AAAA-MM/` : visuels du mois, un fichier par slide (`sujet-1.png`, `sujet-2.png`...).
- `kit/` : charte et outils pour produire les visuels.
  - `base.css` : couleurs, typographies et composants Rield.
  - `fonts/` : polices libres embarquées (Archivo, Fraunces, Poppins, licences OFL), substituts définis par le Rield Design System.
  - `fonts-licence/` : emplacement des polices de marque sous licence (Boska Black Italic, Electrolux Sans Bold). Jamais commité (voir .gitignore) : récupérer les fichiers depuis le Project Claude « Marketing » au moment du rendu. Quand ils sont présents, `base.css` les utilise automatiquement.
  - `logo/` : logo officiel Rield. `rield-logo-couleur.png` sur fond clair, `rield-logo-inverse.png` sur fond sombre, et les pictos.
  - `render.py` : transforme un fichier HTML en PNG 1080x1350.
  - `exemples/` : un carrousel et une image de référence.

## Charte

- Couleurs : Dark Forest `#1A3A34`, Lime Volt `#00E64D`, Teal Mid `#2D6B5E`, Off-White `#F2F0EC`.
- Source de vérité : le Rield Design System (artefact claude.ai). Ce kit en reprend les couleurs, polices, règles et logos.
- Titres en Electrolux Sans Bold (substitut Archivo). Accent Boska Black Italic (substitut Fraunces) via `<em>`, sur 1 à 3 mots-clés maximum, jamais une phrase entière.
- Lime #00E64D uniquement en accent sur fond sombre (chiffres clés, mot en accent, filet). Sur fond clair, texte en lime-muted #00A838. Jamais de grand aplat lime.
- Aucune icône en caractère unicode (pas de flèche texte) : SVG en trait 2px, style Lucide.
- Petit libellé en capitales espacées en haut de slide (`.label`), logo officiel en bas à gauche (version inversée sur sombre, couleur sur clair), pagination ou rield-rm.com en bas à droite.
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
