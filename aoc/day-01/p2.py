#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 16/10/2026
# Description : Break the safe


def collect_input(path: str) -> tuple[tuple[str, int], ...]:
    with open(path, "r", encoding="utf-8") as file:      # Ouvre en lecture un fichier et retourne un objet "flux"
        inputs = file.readlines()          # Lit et ajoute ligne par ligne dans une liste, méthode de l'objet file
    
    liste = []
    for line in inputs:
        line = line.strip()
        if not line:
            # raise ValueError("Ligne vide dans le fichier d'entrée")       → Arrête le programme et affiche une erreur 
            continue
        liste.append((line[0], int(line[1:])))
    
    tuple_list = tuple(liste)
    return tuple_list


def rotate_dial(instructions: tuple) -> int:
    count = 0
    p0 = 50
    # left = 0
    # right = 0
    for l in instructions:
        # print(l, l[0], l[1], type(l[1]))      → vérification de la bonne récupération et lecture des instructions
        if l[0] == 'R':
            # count += (p0 + l[1]) // 100
            # right += (p0 + l[1]) // 100
            # print("RIGHT : " + str((p0 + l[1]) // 100))
            p0 = (p0 + l[1]) % 100
        elif l[0] == 'L':
            # count -= (p0 - l[1]) // 100
            # left += (p0 - l[1]) // 100
            # print("LEFT : "+ str((p0 - l[1]) // 100))
            p0 = (p0 - l[1]) % 100
        else:
            break
        if p0 == 0:
            count += 1
    
    # print("L : " + str(left) + " - R : " + str(right))
    return count


def main():
    print("→ " + str(rotate_dial(collect_input('input.txt'))) + " passages par 0")

    return 0


if __name__ == "__main__":
    main()


# Dernière MàJ : Droite OK + Problème de comptage vers la gauche
# (p0 - pas) // 100 → ne compte pas lorsqu'on tombe pile sur 0, retard de 1 à chaque fois