#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 18/10/2026
# Description : Break rolls wall

def longueur_list(test_list: list) -> int:
    return sum(len(line) for line in test_list)


def affiche_list(entry_list: list, pas: int) -> list:
    chaine = "".join(entry_list)
    grille = "\n".join(
        chaine[i:i+pas]
        for i in range(0, len(chaine), pas)
    )
        
    return grille


def collect_input(path: str) -> tuple[str]:
    with open(path, "r", encoding="utf-8") as file:
        inputs = file.readlines()

        chain_list = [
            item.strip()
            for item in inputs
            if item.strip()
        ]
    
    return chain_list


def check_arround(str_list: list) -> list:
    copy_chain_list = []
    
    for numLine, chainItem in enumerate(str_list):
        for idx, posChar in enumerate(chainItem):
            nb_arobase = 0
            # print(posChar)
            for decalage_ligne in [-1, 0, 1]:
                for decalage_colonne in [-1, 0, 1]:
                    if decalage_ligne == 0 and decalage_colonne == 0:
                        continue

                    ligne_voisine = numLine + decalage_ligne
                    colonne_voisine = idx + decalage_colonne

                    if (0 <= ligne_voisine < len(str_list) 
                        and 0 <= colonne_voisine < len(str_list[ligne_voisine])):
                        if str_list[ligne_voisine][colonne_voisine] == '@':
                            nb_arobase += 1
            
            if posChar == '@' and nb_arobase < 4:
                copy_chain_list.append('x')
            else:
                copy_chain_list.append(posChar)
    
    longueur_entree = longueur_list(str_list)
    chaine = "".join(copy_chain_list)
    longueur_chaine = longueur_list(chaine)

    # print(
    #     f"{affiche_list(copy_chain_list, len(str_list))}"
    #     f"\n ENTREE : {longueur_entree} caractères"
    #     f"\n COPIE : {len(chaine)} caractères"
    # )
    # if longueur_chaine == longueur_entree:
    #     print("\n✅ Les longueurs correspondent\n")

    return copy_chain_list.count('x')



def main():
    exemple = "example_d04.txt"
    file = "input_d04.txt"

    # print(collect_input(file))
    print(
        f"Nombre de rouleau pouvant être déplacés : {check_arround(collect_input(file))}"
    )

if __name__ == "__main__":
    main()