# SCD_imageo
Répertoire destiné au projet d'organisation et de fairisation des données dans Nakala, dans le cadre du Consortium HumaNum ImaGEO
---
## Introduction
Ce répertoire Github contient tous les scripts en **Python3** (Python 3.10.2) réalisés lors de ma mission de mars à mai (2022). Il s'agit dans le cadre du projet ImaGEO, de pouvoir récupérer les métadonnées du Sudoc pour ensuite les upload dans Nakala.

Un des objectifs est de permettre la réutilisation des scripts dans le futur, j'ai donc essayé de me rapprocher le plus possible d'un [**"clean code"**](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29) en utilisant également le moins de librairies possibles et pérennes (voir [requirements.txt](https://github.com/belzepaf/SCD_imageo/blob/main/requirements.txt)). Je vais présenter rapidement les fichiers dans ce read.me. Tout a été testé et fonctionne sous https://test.nakala.fr/.

*Note : Si jamais ces scripts sont réutilisés pour upload sur Nakala (et non Nakala Test), pensez à changer :*
* *les constantes dans **definitions.py**, notamment pour l'url et la clé d'API (uploadé API test ici)*
* *les chemins des fichiers /output dans **4.md_put_post_nakala.py** et **6.nakala_relations.py**: de base, ce sont les fichiers de test. Il y a #en commentaire les fichiers finaux*

---
## Projet
### Scripts
#### definitions.py
Fichier contenant toutes les constantes nécessaires au bon fonctionnement des scripts. 
* Des paths
* Des URLS
* Clé API
* Dictionnaires
#### 1.save_copy_from_z.py [👉](https://github.com/belzepaf/SCD_imageo/blob/main/scripts/1.save_copy_from_z.py)
Crée une copie du fichier d'état des lieux que j'ai réalisé (Z:/SCD/Pôle Services Numériques/Numérisation/Cartothèque/aubry_melanie_2022_etat_des_lieux.xlsx). Dans un souci de conservation, je préfère créer une copie du fichier original plutôt que de travailler directement dessus.
#### 2.parsing_sudoc_xml copy.py
Il s'agit ici de "parser" les objets depuis leur URL Sudoc, en utilisant leur PPN.
On récupère les tags et on extrait les données en utilisant l'arborescence du XML.
Le résultat sort sous forme de dataframe qui est exporté.
#### 3.build_metadata.py
Petit script de mise en forme des métadonnées SUDOC pour permettre l'import sur Nakala.
* Conversion DMS to DD
* Mise en forme
* Export CSV/XLS
#### 4.md_put_post_nakala.py
* Import des métadonnées sur Nakala 
* Prise en compte des formats, des dictionnaires (voir **definitions.py**)
* Si une donnée est déjà présente, on ne l'écrasera pas
* Si la donnée est vide dans le fichier construit avec **3.build_metadata.py** , pas d'import.
* Le script devrait push sur tous les handles (sélectionnés depuis le fichier créé avec **3.build_metadata.py**)
#### 5.build_relations_xls.py
Petit script de mise en forme d'un fichier pour upload les relations (fusion du fichier d'état des lieux (Z:/SCD/Pôle Services Numériques/Numérisation/Cartothèque/aubry_melanie_2022_etat_des_lieux.xlsx) et de celui de Philippe Laymond (dont on peut retrouver une copie dans **input**)
#### 6.nakala_relations.py
Push des relations sur Nakala (pour le moment, ça push dans les deux sens car cela me semblait plus logique).
### utils
**utils** est une collection de petites fonctions Python communes aux scripts.
### input
Dossier contenant les fichiers d'entrée
### output
Dossier contenant les fichiers de sortie (notamment les fichiers créés avec les scripts).

---

Création d'environnement virtuel Python si nécessaire https://docs.python.org/fr/3.6/tutorial/venv.html

---
La moindre question, n'hésitez pas à me contacter : aubry.melanie33@gmail.com
