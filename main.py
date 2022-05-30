"""
Ali Alzamani
"""

import string

import assignment1


def main():
    print("\n       ** running print JSON countries capitals **\n")
    assignment1.print_json_countries_capitals()
    print("-------------------------------------------------------")
    print("\n       ** running get list of countries whose nth\n"
          "               letter is (n, letter) **\n")
    letters = ['a', 'e', 'i', 'o', 'u']
    for n in range(1, 4):
        for letter in letters:
            print(assignment1.get_list_of_countries_whose_nth_letter_is(n, letter))
            print()
    print("-------------------------------------------------------")
    print("\n       ** running get funny case capital cities **\n")
    alphabet = list(string.ascii_lowercase)
    for character in alphabet:
        funny_case_capital_cities = assignment1.get_funny_case_capital_cities(character)
        for index, capital in enumerate(funny_case_capital_cities):
            if index % 3 == 0:
                print()
            print(f"'{capital}',", end=' ')
        print("\n\n-------------------------------------------------------")
    print("\n       ** running get doubled letter countries **\n")
    doubled_letter_countries = assignment1.get_doubled_letter_countries()
    for index, country in enumerate(doubled_letter_countries):
        if index % 3 == 0:
            print()
        print(f"'{country}',", end='')
    print()


if __name__ == '__main__':
    main()
