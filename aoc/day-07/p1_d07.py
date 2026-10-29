#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 25/10/2026
# Description : How much times did the beam splitted ?

import copy


def collect_input(path: str) -> tuple[list[str], list[str]]:
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
    
    return [list(line.strip()) for line in lines]



def trace_beam(input_list: list) -> list, int:
    """
    Créé une copie d'une liste de liste de caractères et la parcours pour 
    en modifier certains selon un schéma spécifique. Chaque '^' donnant lieu à une division
    du faisceau, marqué '|', en deux. Chaque division du faisceau est en parallèle comptabilisée.

    :param input_list: Liste de listes de caractères
    :source: La position de départ du faisceau sur la première ligne
    :beam: Une copie de la liste permettant de ne pas altérer l'entrée si besoin
    :beam_pos: Position du faisceau sur la ligne actuelle
    :next_pos: Position du faisceau à prévoir sur la ligne suivante
    :splits: Compteur du nombre de division du faisceau effectuées
    :return: Retourne la copie de la liste modifiée et le compteur de divisions
    """
    source = input_list[0].index("S")
    beam = [line.copy() for line in input_list]
    beam_pos = {source}
    splits = 0

    for num in range(len(beam)-1):
        next_pos = set()
        for i in beam_pos:
                if input_list[num+1][i] == "^":
                    if i-1 >= 0:
                        beam[num+1][i-1] = "|"
                        next_pos.add(i-1)

                    if i+1 <= len(beam[num + 1]):
                        beam[num+1][i+1] = "|"
                        next_pos.add(i+1)
                    
                    splits += 1
                else:
                    beam[num+1][i] = "|"
                    next_pos.add(i)
        
        beam_pos = next_pos
        
    return beam, splits



def main():
    ex = "example_d07.txt"
    file = "input_d07.txt"

    trace, total_splits = trace_beam(collect_input(file))
    # for line in trace:
    #     print(line)
   
    print(
        f"\n\n → Total de splits : {total_splits}"
    )
if __name__ == "__main__":
    main()