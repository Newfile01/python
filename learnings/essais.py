#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 2026-16-10
# Description : Ce script rassemble plusieurs éléments de base de la programmation en Python à des fins d'exercices et de rappels.

# Rq. :
# - Pour exploiter le shebang en début de script il faut rendre le fichier exécutable avec chmod +x
# - f-string est une façon de formater des chaînes de caractères en Python.


# Fonction prenant un nom en entrée et sortant une salutation personnalisée
def welcome(nom):
    return f"Bonjour {nom} !"

nom = "Nicolas"

print("Coucou c'est Python !")
print(welcome(nom))