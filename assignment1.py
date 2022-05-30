"""
Ali Alzamani
"""

import string

from data import countries_and_capitals, countries, capitals


def print_json_countries_capitals():
    """
    This function prints each country and its capital in json format
    First variant, no parameter, no return
    :return: None
    """
    print("{")
    for item in countries_and_capitals:
        print("""    {\n        "country_name":"%s",\n        "capital_city":"%s"\n    },""" % (item[0], item[1]))
    print("}")


def get_list_of_countries_whose_nth_letter_is(n=0, letter=""):
    """
    This function creates and returns a list of all countries whose nth letter matches the letter in the parameter
    Fourth variant, parameters and return
    :param n: the location of the letter to be matched
    :param letter: the letter to be matched
    :return: list of all countries whose nth letter matches the letter in the parameter
    """
    list_of_countries_whose_nth_letter_is = []
    for county in countries:
        if county[n-1].lower() == letter.lower():
            list_of_countries_whose_nth_letter_is.append(county)
    return list_of_countries_whose_nth_letter_is


def get_funny_case_capital_cities(letter=""):
    """
    This function creates and returns a list of capital cities formatted in a way where
    A letter that immediately precedes and follows the parameter letter is uppercased
    Fourth variant, a parameter and return
    :param letter: the letter whose preceding and following letters to be uppercased
    :return: a list of capital cities formatted in a way where
             A letter that immediately precedes and follows the parameter letter is uppercased
    """
    funny_case_capital_cities = []
    for capital in capitals:
        if letter in capital.lower():
            capital = list(capital.lower())
            for index, item in enumerate(capital):
                if item == letter and index - 1 >= 0 and capital[index-1] != letter:
                    capital[index-1] = str(capital[index-1]).capitalize()
                if item == letter and index + 1 < len(capital) and capital[index+1] != letter:
                    capital[index+1] = str(capital[index+1]).capitalize()
            capital = "".join(capital)
            funny_case_capital_cities.append(capital)
    return funny_case_capital_cities


def get_doubled_letter_countries():
    """
    This function creates and returns a tuple of all the countries that have consecutive repeated letters
    Third variant, no parameter, but return
    :return: a tuple of all the countries that have consecutive repeated letters
    """
    doubled_letter_countries = []
    sorted_doubled_letter_countries = []
    alphabet = list(string.ascii_lowercase)
    for country in countries:
        for index, letter in enumerate(country):
            if index - 1 >= 0 and letter == country[index-1].lower():
                doubled_letter_countries.append(country)
                break
            elif index + 1 < len(country) and str(letter).lower() == country[index+1]:
                doubled_letter_countries.append(country)
                break
    for character in alphabet:
        for country in doubled_letter_countries:
            for index, letter in enumerate(country):
                if index - 1 >= 0 and letter == country[index - 1].lower() and letter == character:
                    sorted_doubled_letter_countries.append(country)
                    break
                elif index + 1 < len(country) and str(letter).lower() == country[index + 1] \
                        and str(letter).lower() == character:
                    sorted_doubled_letter_countries.append(country)
                    break
    # Below was an attempt to do everything in one go. It still works, but the execution time was way more
    # Using two nested loops as above, the time was 0.0033 seconds.
    # While using one nested loop as below, the time was 0.0298 seconds!
    # for character in alphabet:
    #     for country in countries:
    #         for index, letter in enumerate(country):
    #             if index - 1 >= 0 and letter == country[index - 1].lower() and letter == character:
    #                 sorted_doubled_letter_countries.append(country)
    #                 break
    #             elif index + 1 < len(country) and str(letter).lower() == country[index + 1] \
    #                     and str(letter).lower() == character:
    #                 sorted_doubled_letter_countries.append(country)
    #                 break
    return tuple(sorted_doubled_letter_countries)


def main():
    print("I should not be called")


if __name__ == "__main__":
    main()
