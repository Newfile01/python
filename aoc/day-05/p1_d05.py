#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 18/10/2026
# Description : How many available ingredients are fresh ?


def collect_input(path: str) -> tuple[list[str], list[str]]:
    """
    Récupère le contenu d'un fichier ligne par ligne. 
    Il intègre chacune des deux parties séparées par une ligne vide
    dans deux listes de chaînes de caractères distinctes après suppresison
    des caractères non nécessaires "\n" ou " " entourant chaque ligne.

    :path: Le nom ou chmin du fichier sous forme de chaîne de caractères
    :ranges: Liste de chaînes de ranges
    :availables: Liste de chaînes représentant les ingrédients disponibles
    :return: Un tuple de listes de chaînes de caractères
    """
    with open(path, "r", encoding="utf-8") as file:
        inputs = file.readlines()

    ranges = []
    availables = []
    second_part = False

    for item in inputs:
        item = item.strip()

        if not item:
            second_part = True
            continue

        if second_part:
            availables.append(item)
        else:
            ranges.append(item)

    return ranges, availables


def str_range_limits_to_int(str_range: str) -> tuple(int, int):
    """
    Convertit un range sous forme de chaîne de caractère en 2 entiers déterminant les extrémités

    :param str_range: Range d'entiers sous forme de chaîne de caractères, séparés par '-'
    :range_min: L'extrémité basse
    :range_max: L'extrémité haute
    :return: Les deux éléments (sous forme de tuple d'entiers)
    """
    range_min, range_max = str_range.split("-")

    return int(range_min), int(range_max)


def is_fresh(ing_ranges: list, ing_availables: list) -> int:
    """
    Fait correspondre le contenu d'une liste de nombre sous forme de chaînes de caractères avec
    une liste d'intervalles également sous forme de chaîne de caractère. Elle compte le nombre 
    d'inclusion d'un élément de la première liste dans au moins un des intervals de la seconde.

    :param int_ranges: Liste d'intervalles en chaînes de caractères, séparés par '-'
    :param int_availables: Liste d'élément chaînes de caractères dont il faut vérifier l'inclusion dans au moins un interval de int_ranges
    :count_fresh: Compteur d'élément frais (entier)
    :checked: Booléen indiquant si l'élément a déjà été compté dans un interval
    :minimum: Extrémité basse d'un interval sous forme d'entier
    :maximum: Extrémité haute d'un interval sous forme d'entier
    """
    count_fresh = 0
    for item in ing_availables:
        checked = False
        for element in ing_ranges:
            minimum, maximum = str_range_limits_to_int(element)

            if minimum <= int(item) <= maximum and not checked:
                checked = True
                print(
                    f" Element : {item}"
                )
                count_fresh += 1
    
    return count_fresh



def main():
    exemple = "example_d05.txt"
    file = "input_d05.txt"

    print("\n\n Nombre d'ingrédients frais → "+str(is_fresh(*collect_input(file))))


if __name__ == "__main__":
    main()