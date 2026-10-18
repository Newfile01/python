#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 18/10/2026
# Description : Total output joltage

def collect_input(path: str) -> tuple[tuple[str, int], ...]:
    with open(path, "r", encoding="utf-8") as file:     # Ouvre en lecture un fichier et retourne un objet "flux"
        input_tuple = tuple(                            # Génère un tuple en suivant la forme d'une compréhension :
            item.strip()                                # méthode de parcours (for x in y) ; expression (item.strip()) ; condition de filtrage (si la chaîne item.strip() est vraie)
            for item in file                            # 
            if item.strip()                             # Ne retiens que les éléments valides et ignore les éléments vides ou composés uniquement d'espaces
        )


    return input_tuple

def largest_pair(tuple_list: tuple) -> int:
    final_sum = 0
    for item in tuple_list:
        max_pair = 0

        for index, digit1 in enumerate(item):
            for digit2 in item[index + 1:]:
                pair = int(digit1 + digit2)

                if pair > max_pair:
                    max_pair = pair

        final_sum += max_pair
        print(f"{item} -> {max_pair}")
        
    return final_sum


def main():
    file = "input_d03.txt"

    print(
        f"\n → Total Output joltage = {largest_pair(collect_input(file))} V"
    )


if __name__ == "__main__":
    main()