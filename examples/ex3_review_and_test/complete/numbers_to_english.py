# task: https://edabit.com/challenge/mZqMnS3FsL2MPyFMg

digits_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

ten_to_nineteen_dict = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eightteen",
    "19": "nineteen",
}

dozens_dict = {
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}


def _handle_one_digit(num_text: str, skip_zero: bool = False) -> str:
    if skip_zero and num_text == "0":
        return ""
    return digits_dict[num_text]


def _handle_two_digits(num_text: str) -> str:
    if num_text[0] == "0":
        return _handle_one_digit(num_text[1], skip_zero=True)
    elif num_text[0] == "1":
        return ten_to_nineteen_dict[num_text]
    else:
        print(num_text)
        return " ".join([dozens_dict[num_text[0]], _handle_one_digit(num_text[1], skip_zero=True)]).strip()


def _handle_three_digits(num_text: str) -> str:
    hundred = "hundred"
    return " ".join([_handle_one_digit(num_text[0], skip_zero=True), hundred, _handle_two_digits(num_text[1:])]).strip()


def num_to_eng(n: int) -> str:
    num_text = str(n)
    digits_count = len(num_text)

    if digits_count == 1:
        return _handle_one_digit(num_text)

    elif digits_count == 2:
        result = _handle_two_digits(num_text)
        return result

    elif digits_count == 3:
        result = _handle_three_digits(num_text)
        return result

    else:
        raise ValueError(
            "This function accepts only a positive integer between 0 and 999"
        )

print(num_to_eng(100))