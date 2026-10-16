#!/usr/bin/env python3

# Auteur : N.M.
# Date : 2026.10.16
# Description : Travail sur les différents types de collections

# ↓ Par soucis de simplification ↓
# L : Liste
# T : Tuples
# D : Dictionnaires

def main():
    
    # LISTES

    L_auto = list(range(10)) # 0 à 9
    L_man = [1, "Bonjour", 3.14, L_auto, True]

    for l in L_auto:
        print(l)

    print("\n")

    for i, l in enumerate(L_man):
        if l == L_auto:         # Le test doit comparer directement la variable et non une str qui donnerai son nom "L_auto" (← ne fonctionne pas)
            print(f"index = {i}")
            for item in l:      # On parcourt et affiche chaque élément de la sous-liste
                print(item)
            continue            # Passer à l'itération suivante du premier for pour ne pas afficher → L_auto[0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9]
        print(l)                # Positionner le print après le if évite aussi d'afficher la sous-liste avant de la détailler
        if l is True:
            print(f"\nindex = {i}")

    print("\n")

    print("\n")

    print("\n")


if __name__ == "__main__":
    main()
