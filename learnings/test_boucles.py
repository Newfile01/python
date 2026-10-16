#!/usr/bin/env python3

def main():
    mot = "Alleluia"

    for i in mot:
        print(i)

    print("\n\nRange 5")
    # Afficher les nombres de 0 à 4
    for i in range(5):
        print(i)

    print("\n\n Range 1, 6")
    # Afficher les nombres de 1 à 5
    for i in range(1, 6):
        print(i)

    print("\n\nRange 0, 11 ,2")
    # Afficher les nombres pairs de 0 à 10
    for i in range(0, 11, 2):
        print(i)

    print("\n\nWhile c < 5")
    compteur = 0
    while compteur < 5:
        print(f"Compteur : {compteur}")
        compteur += 1

    # Break sort immédiatement de la boucle
    print("\n\nBreak à 5")
    for i in range(10):
        if i == 5:
            break
        print(i)
    # Affiche 0, 1, 2, 3, 4

    # Continue passe à l'itération suivante
    print("\n\nContinue % 2")
    for i in range(10):
        if i % 2 == 0:  # Si le nombre est pair
            continue
        print(i)
    # Affiche 1, 3, 5, 7, 9


if __name__ == "__main__":
    main()