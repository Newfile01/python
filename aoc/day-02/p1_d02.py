#!/usr/bin/env python3

# Auteur : Nicolas MOREL
# Date : 16/10/2026
# Description : Find Wrong IDs

# import random

# #1 - RECUPERATION RANGES
# -------------------------
def chain_input_as_list(path: str):
    print(" ⬇️  Loading inputs")
    
    with open(path, "r", encoding="utf-8") as file:
        chain = file.read()
    
    range_tuple = tuple(                # Transforme les éléments obtenus en tuple
        item.strip()                    # Nettoie les espaces et retours à la ligne autour de chaque élément
        for item in chain.split(",")    # Découpe le texte à virgule
        if item.strip()                 # ignore les éléments vides ou composés uniquement d'espaces
    )

    return range_tuple


# #2 - COLLECT WRONG IDs
# -------------------------
def collect_wrong_patterns(tuple_range_list: tuple) -> list:
    print(" ✔️  Checking IDs")
    range_list = list(tuple_range_list)
    wrong_patterns = []
    # Pour comprendre
    # print(
    #         f"\n Longueur liste de plages : {len(range_list)}\n"
    # )
    for range_item in range_list:
        first_id, last_id = map(int, range_item.split("-"))

        # Pour comprendre
        # print(
        #     f" Plage {range_list.index(range_item):<5}:"
        #     f"{f'{first_id}-{last_id}':<22}"
        #     f" Nombre d'IDs à tester : {last_id - first_id + 1:>10}"
        # )

        for id_value in range(first_id, last_id + 1):
            id_to_string = str(id_value)

            if is_wrong_id(id_to_string):
                wrong_patterns.append(id_value)

    tuple(wrong_patterns)
    
    return wrong_patterns


# def sum_list(tuple_patterns: tuple) -> int:
#     print(" ➕ Processing results")
#     patterns_list = list(tuple_patterns)
#     res = 0

#     for i in patterns_list:
#         res += i
#         # print(
#         #     f" i = {i}\t res = {res}"
#         # )

#     return res


# #3 - VALIDATION IDs
# -------------------------
# Générateur aléatoire d'IDs
# def generate_id() -> int:
#     length = random.randint(2, 10)
#     first_digit = random.randint(1, 9)
#     remaining_digits = random.randint(0, 10**(length - 1) - 1)

#     return first_digit * 10**(length - 1) + remaining_digits

def is_wrong_id(id_str: str) -> bool:
    if len(id_str) % 2 != 0:
        return False

    middle = len(id_str) // 2

    groupe1 = id_str[:middle]
    groupe2 = id_str[middle:]

    return groupe1 == groupe2


def main():
    # Pour comprendre
    # print(
    #     f"Liste de plage {chain_input_as_list("input_d02.txt")}"
    # )

    # Pour comprendre
    # while True:
    #     id_value = generate_id()
    #     result = is_wrong_id(str(id_value))
    #     print(id_value, result)

    #     if result:
    #         break

    file = "input_d02.txt"

    print(
        f" ➕ Processing results"
        f"\n\n  → Res = {sum(collect_wrong_patterns(chain_input_as_list(file)))}"
    )

    # print("Test nettoyage :", chain_input_as_list(file))
    

    # tests = [
    #     "11",
    #     "22",
    #     "99",
    #     "1010",
    #     "58721123",
    #     "12312345",
    #     "12345678",
    # ]

    # for test_id in tests:
    #     print(f"{test_id:<12} -> {is_wrong_id(test_id)}")
    

    # print("Affichage des IDs incorrect : ", collect_wrong_patterns(tuple(tests)))

if __name__ == "__main__":
    main()