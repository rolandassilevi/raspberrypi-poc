# Notes diverses durant le développement du projet

## Étapes pour retirer .rpi-poc du dépôt Git

*  J'ai push le dossier .rpi-poc avant de l'insérer dans .gitignore. Il se trouve actuellement dans le dépot Github. Comment le supprimer du dépot, et ne plus le considerer dans les prochain commit?

1. Ajouter le dossier à .gitignore
Ouvre (ou crée) le fichier *.gitignore* à la racine du projet et ajoute :
```bash
.rpi-poc/
```

2.Supprimer le dossier de l’index Git sans le supprimer du disque local :
```bash
git rm -r --cached .rpi-poc
```
*--cached* : dit à Git de supprimer uniquement du dépôt, pas du système de fichiers local.

3. Commiter la suppression et le *.gitignore*
```bash
git add .gitignore
git commit -m "Remove .rpi-poc from repository and add to .gitignore"
```
4. Pousser les changements sur GitHub :
```bash
git push origin main
```
(Si ta branche n’est pas main, remplace main par le nom de ta branche)