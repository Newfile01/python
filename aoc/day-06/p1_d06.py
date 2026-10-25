#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 25/10/2026
# Description : Solve every column math operation


def collect_input(path: str) -> tuple[list[str], list[str]]:
    """
    Récupère le contenu d'un fichier ligne par ligne. 
    Retourne chaque ligne nettoyée de tout " " ou "\n" dans une liste de ligne.

    :param path: Le nom ou chemin du fichier sous forme de chaîne de caractères
    :lines: Liste de chaînes de caractères représentant chaque ligne du fichier d'entrée
    :return: Une liste de liste de chaînes (str) nettoyées de tout " " ou "\n" 
    
    Exemple : '  1 2  3 ... +\n' → list['  1 2  3 ... +\n'] → list[['1','2','3',...'+']]
    """
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return [line.split() for line in lines]


def operate(input_list: list) -> list:
    """
    Récupère une liste de chaînes de caractères représentant des nombres
    et la découpe en deux sous-listes : operators & numbers_rows. La fonction 
    réalise ensuite les opérations sur l'ensemble des éléments d'une même colonne 
    en se basant sur l'opérateur indiqué au dernier élément de chaque colonne.

    :param input_list: Liste d'entrée (doit être formatté correctement) → list[list[str, str], list[str, str]] sans " " ni "\n"
    :operators: Liste récupérant uniquement la dernière ligne = les opérateurs de chaque colonne
    :numbers_rows: Liste ne récupérant que les nombres de chaque ligne
    :results: Liste récupérant dans chaque élément le résultat de chaque colonne
    :result: Le résultat de chaque colonne
    :i: L'index servant au décalage par colonne
    :return: La liste de l'ensemble des résultats
    """
    operators = input_list[-1]
    numbers_rows = input_list[:-1]
    results = []

    for i, operator in enumerate(operators):
        if operator == "+":
            result = 0
        elif operator == "*":
            result = 1

        for row in numbers_rows:
            if operator == "+":
                result += int(row[i])
            elif operator == "*":
                result *= int(row[i])

        results.append(result)

    return results


def main():
    exemple = "example_d06.txt"
    file = "input_d06.txt"

    list_retour = collect_input(file)
    resultats = operate(list_retour)
    total = sum(item for item in resultats)
    print(
        # f"\n\n 1️⃣ ENTREE NETTOYEE : {list_retour}"
        # f"\n\n 2️⃣ RESULTATS DES COLONNES : {resultats}"
        f" 3️⃣ TOTAL : {total}"
    )

if __name__ == "__main__":
    main()