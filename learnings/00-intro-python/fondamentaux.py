#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 2026-16-10
# Description : Script d'apprentissage des fondamentaux Python


# Bienvenue dans l'apprentissage des fondamentaux Python
print("=== Fondamentaux de Python ===")

# === VARIABLES ET TYPES DE DONNÉES ===
print("\n1. Variables et types de données")

# Déclaration de variables de différents types
nom = "Alice"  # Chaîne de caractères (str)
age = 30       # Entier (int)
taille = 1.75  # Flottant (float)
est_majeur = True  # Booléen (bool)

# Affichage des variables avec leur type
print(f"Nom: {nom} (type: {type(nom).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Taille: {taille} (type: {type(taille).__name__})")
print(f"Est majeur: {est_majeur} (type: {type(est_majeur).__name__})")


# === OPÉRATIONS MATHÉMATIQUES ===
print("\n2. Opérations mathématiques")

a = 10
b = 3

# Les opérations de base
addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b
modulo = a % b

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {addition}")
print(f"Soustraction: {a} - {b} = {soustraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division:.2f}")
print(f"Modulo: {a} % {b} = {modulo}")
print(f"Addition v2: a + b directement dans le print → {a + b}")

# Priorités des opérations
resultat1 = 5 + 2 * 3
resultat2 = (5 + 2) * 3
print(f"\nPriorités: 5 + 2 * 3 = {resultat1}")
print(f"Avec parenthèses: (5 + 2) * 3 = {resultat2}")


# === MANIPULATION DE CHAÎNES ===
print("\n3. Manipulation de chaînes de caractères")
chaine1 = "Bonjour"
chaine2 = "Python"

# Opérations sur les chaînes
concatenation = chaine1 + " " + chaine2
premierCaract = chaine1[0]
dernierCaract = chaine1[-1]
sous_chaine = chaine1[0:3]
longueurC1 = len(chaine1)
longueurC2 = len(chaine2)
repetition = chaine1 * 3
inversion = chaine1[::-1]

print("\nRésultats des opérations sur les chaînes de caractères")
print("Chaine 1:", chaine1)
print("Chaine 2:", chaine2)
print(f"\nConcaténation: {concatenation}")
print(f"Premier caractère: {premierCaract}")
print(f"Dernier caractère: {dernierCaract}")
print(f"Sous-chaîne: {sous_chaine}")
print(f"Longueur de la chaîne 1: {longueurC1}")
print(f"Longueur de la chaîne 2: {longueurC2}")
print(f"Répétition: {repetition}")
print(f"Inversion: {inversion}")


# === OPÉRATIONS LOGIQUES ===
print("\n4. Opérations logiques")

vrai = True
faux = False

# Opérateurs logiques
resultat_et = vrai and faux
resultat_ou = vrai or faux
resultat_non = not vrai

print(f"vrai = {vrai}, faux = {faux}")
print(f"vrai AND faux = {resultat_et}")
print(f"vrai OR faux = {resultat_ou}")
print(f"NOT vrai = {resultat_non}")

# Comparaisons
x = 10
y = 20
print(f"\nx = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")

# === CONVERSIONS DE TYPES ===
print("\n5. Conversions entre types")

# Conversion de chaîne vers nombre
nombre_texte = "123"
nombre_entier = int(nombre_texte)
nombre_flottant = float(nombre_texte)

print(f"Chaîne: '{nombre_texte}' -> Entier: {nombre_entier}")
print(f"Chaîne: '{nombre_texte}' -> Flottant: {nombre_flottant}")

# Conversion de nombre vers chaîne
age_num = 30
age_texte = str(age_num)
print(f"Entier: {age_num} -> Chaîne: '{age_texte}'")

# Conversion booléenne
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool('Hello'): {bool('Hello')}")