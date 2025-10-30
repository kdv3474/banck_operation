def get_mask_card_number(number_card: int) -> str:
    """Функция маскирует номер карты,    отставляя видимыми только первые 6 цифр
    и последние 4 цифры"""
    str_number_card = str(number_card)
    # Выделяем первую видимую часть номера карты
    part1 = str_number_card[:6]
    # Вторая часть номера карты
    part2 = "******"
    # Последняя часть номера карты
    part3 = str_number_card[-4:]
    # Собираем маскированный номер карты
    mask_number_card = part1 + part2 + part3
    # Делим строку по четыре знака через пробел
    mask_new = f"{part1[:4]} {part1[4:]}{part2[:2]} {part2[2:]} {part3[:2]}{part3[2:]}"
    return mask_new
print(get_mask_card_number(7000792289606361))

def get_mask_account(account_number: int) -> str:
    """Функция маскирует аккаунт, оставляя последние 4 цифры, а передними
    ставиться 2 (*)"""
    str_account_number = str(account_number)
    # Извлекаем последние 4 цифры
    last_four_digit = str_account_number[-4:]
    # Формируем маску
    mask_account = "**" + last_four_digit
    # Возвращаем маскированный номер
    return mask_account
