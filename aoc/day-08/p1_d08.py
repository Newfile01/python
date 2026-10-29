#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 29/10/2026
# Description : Find the shortest circuit between boxes


def collect_ListListStr(path: str) -> list[list[str], list[str]]:
    """
    Récupère le contenu d'un fichier ligne par ligne. 
    Purge d'éventuels caractères blanc en début et en fin de chaque ligne.
    Les converties en listes de caractères et les retourne dans une grande liste assemblée.

    :param path: Le nom ou chemin du fichier sous forme de chaîne de caractères
    :lines: Liste de chaînes de caractères représentant chaque ligne du fichier d'entrée
    :return: Une liste de liste de caractères sans caractères balanc en début et fin de chaque ligne

    Exemple : '  1 2  3 ... +\n' → list['  1 2  3 ... +\n'] → list[['1','2','3',...'+']]
    """
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines = [line.split() for line in lines]
        coordinates = []

        for line in lines:
                for chain in line:
                    chain_list = chain.split(",")                    
                    coordinates.append(chain_list)
    # Les lignes qui suivent le `with open(...)` pourraient être remplacer par : 
    # coordinates = [line.strip().split(",") for line in file]
    # 
    # Une variante pour obtenir directement les entiers pourrait être :
    # coordinates = [
    #     [int(value) for value in line.strip().split(",")]
    #     for line in file
    # ]
    #
    # À noter que le parcours d'un fichier avec `for line in file` permet de le lire ligne par ligne
    # (Ce n'est pas une tournure/un mot clé particulière, seulement l'effet du parcours d'un fichier avec un for)

    return coordinates


def coordinates_to_int(chain_coordinates: list) -> list[list[int]]:
    int_coordinates = []
    for line in chain_coordinates:
        int_line = []
        for value in line:
            value = int(value)
            int_line.append(value)
        
        int_coordinates.append(int_line)

    return int_coordinates


def circuit_lengh(int_coordinates: list) :
    # À chaque liste de coordonnées → établir la distance avec chaque autre liste de la liste principale
    # d = ((x2 - x1) + (y2 - y1) + (z2 - z1)) ** 0,5
    # Liste_evaluee[x1,y1,z1]
    # Liste_a_comparer[x2,y2,z2]

    # Passage par un dictionnaire ? Dictionnaires imbriqués : dict{boxe{x,y,z}}
    # → zip cordinates["x","y","z"] avec int_coordinates[list[int]] → boxes{}   ----   Voir comment les imbriquer
    # 
    # for key, val_key in boxes.items():
    #   for compared_key, val_comp in boxes.items():
    #       if compared_key not key:
    #           d = (boxes[compared_key][x]-boxes[key][x])+(boxes[compared_key][y] - boxes[key][y])+(boxes[compared_key][z] - boxes[key][z])   

def main():
    ex = "example_d08.txt"
    file = "input_d08.txt"

    print(coordinates_to_int(collect_ListListStr(ex)))

if __name__ == "__main__":
    main()