#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 16/10/2026
# Description : Break the safe

def coco():
    print("Coco")
    return 0


def main():
    print("Hello, World!")
    print(banane.__module__)
    return 0


if __name__ == "__main__":
    main()



# # Initial
# positions = list(range(100))
# start = 0
# # instructions[i] → récupérer la liste des éléments du fichier (dans l'ordre donné)

# for instruction in instructions:
#     # Décomposer la chaîne :
#     # - direction
#     # - nombre de pas (transtyper en entier)

#     if direction == "R":
#         start = (start + nombre_de_pas) % 100
#     elif direction == "L":
#         start = (start - nombre_de_pas) % 100
#     else:
#         break
