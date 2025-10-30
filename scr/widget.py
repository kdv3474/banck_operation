import re

from scr.masks import get_mask_account, get_mask_card_number


def get_date(str_date: str) -> str:
    """принимает на вход строку с датой в формате
"2024-03-11T02:26:18.671407"
 и возвращает строку с датой в формате
"ДД.ММ.ГГГГ   """
    format_str = str_date[8:10] + "." + str_date[5:7] + "." + str_date[0:4]
    return format_str


def mask_account_card(str_number_card: str) -> str:
    """Функция принимает на вход строку ввиде Visa Platinum 7000792289606361
     или Счет 73654108430135874305 и маскирует их по зарным правилам"""
    if  str_number_card.startswith("Счет"):
        pattern = r"\d+"  # поиск чисел
        match = re.search(pattern, str_number_card)
        if match:
            number = int(match.group())
            masked_string = re.sub(r"\d+", get_mask_account(number), str_number_card)
    else:
        pattern = r"\d+"  # поиск чисел
        match = re.search(pattern, str_number_card)
        if match:
            number = int(match.group())
            masked_string = re.sub(r"\d+", get_mask_card_number(number), str_number_card)
    return masked_string
