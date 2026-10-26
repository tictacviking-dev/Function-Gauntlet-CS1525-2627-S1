from typing import Optional
def is_even(number: int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: The number to check if it is even.
    :return: True if the number is even, otherwise False.
    """
    if number % 2 == 0:
        return True
    else:
        return False


def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: The text to look through for vowels.
    :return: The number of vowels found in the text.
    """
    vowels = "aeiou"
    count = 0
    for letter in text.lower():
        if letter in vowels:
            count = count + 1
    return count


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: The temperature in degrees Celsius.
    :return: The temperature in degrees Fahrenheit.
    """
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def reverse_text(text: str) -> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: The text to reverse.
    :return: The text with its characters in reverse order.
    """
    reversed_text = ""
    for letter in text:
        reversed_text = letter + reversed_text
    return reversed_text


def larger_number(a: int, b: int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: The first integer.
    :param b: The second integer.
    :return: The larger of the two integers.
    """
    if a > b:
        return a
    else:
        return b


def average_two(a: int, b: int) -> float:
    """Calculate and return the average of two integers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The average of the two integers.
    """
    total = a + b
    average = total / 2
    return average


def can_afford(balance: float, cost: float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: The amount of money available.
    :param cost: The price of the item.
    :return: True if the balance covers the cost, otherwise False.
    """
    if balance >= cost:
        return True
    else:
        return False


def repeat_text(text: str, times: int) -> str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: The text to repeat.
    :param times: How many times to repeat the text.
    :return: One string with the text repeated.
    """
    repeated = text * times
    return repeated


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: The sentence to search inside.
    :param word: The word to look for.
    :return: True if the word is found in the sentence, otherwise False.
    """
    if word in sentence:
        return True
    else:
        return False


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: The cost before the tip.
    :param percent: The tip percentage (15 means 15%).
    :return: The amount of the tip.
    """
    tip = cost * (percent / 100)
    return tip


def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: The person's first name.
    :param last_name: The person's last name.
    :return: The two initials in uppercase.
    """
    first_initial = first_name[0].upper()
    last_initial = last_name[0].upper()
    return first_initial + last_initial


def percent_score(points: float, possible: float) -> Optional[float]:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: The points that were earned.
    :param possible: The total points possible.
    :return: The percentage earned, or None if possible is less than 1.
    """
    if possible < 1:
        return None
    percentage = points / possible * 100
    return percentage


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: The number to check.
    :param minimum: The lowest allowed value.
    :param maximum: The highest allowed value.
    :return: True if the number is within the range, otherwise False.
    """
    if number >= minimum and number <= maximum:
        return True
    else:
        return False


def all_different(a: str, b: str, c: str) -> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a: The first string.
    :param b: The second string.
    :param c: The third string.
    :return: True if no two strings are the same, otherwise False.
    """
    if a != b and a != c and b != c:
        return True
    else:
        return False


def average_three(a: int, b: int, c: int) -> float:
    """Calculate and return the average of three integers.

    :param a: The first integer.
    :param b: The second integer.
    :param c: The third integer.
    :return: The average of the three integers.
    """
    total = a + b + c
    average = total / 3
    return average


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: The temperature to describe.
    :param cold_limit: Temperatures below this are cold.
    :param hot_limit: Temperatures above this are hot.
    :return: "cold", "hot", or "comfortable".
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"


if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    print(is_even(4))
    print(is_even(7))
    print(count_vowels("Education"))
    print(celsius_to_fahrenheit(100))
    print(reverse_text("robot"))
    print(larger_number(3, 9))
    print(average_two(4, 9))
    print(can_afford(20, 15.5))
    print(can_afford(5, 15.5))
    print(repeat_text("Go!", 3))
    print(contains_word("The cat sat", "cat"))
    print(calculate_tip(20.0, 15))
    print(make_initials("Ada", "Lovelace"))
    print(percent_score(18, 20))
    print(percent_score(5, 0))
    print(is_between(5, 1, 10))
    print(all_different("a", "b", "c"))
    print(average_three(3, 6, 9))
    print(describe_temperature(5, 10, 25))