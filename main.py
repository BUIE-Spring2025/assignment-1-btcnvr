def int_to_roman(num):
    roman_num = ""
    if 4000 > num >= 1000:
        roman_amount = num //1000
        roman_num += "M" * roman_amount
        num -= roman_amount * 1000
    if 800< num <1000:
        roman_amount = (num-500) // 100
        roman_num += "C" * (5-roman_amount) + "M"
        num -= (roman_amount*100 + 500)
    if 500<= num <= 800:
        roman_amount = (num-500)//100
        roman_num += "D" + roman_amount * "C"
        num -= (500 + roman_amount*100)
    if 400 <= num < 500:
        roman_amount = num // 100
        roman_num += "CD"
        num -= roman_amount *100
    if 100 <= num < 400:
        roman_amount = num // 100
        roman_num += "C" * roman_amount
        num -= roman_amount * 100
    if 80< num <100:
        roman_amount = (num-50) // 10
        roman_num += (5-roman_amount) * "X" + "C"
        num -= (roman_amount*10 + 50)
    if 50<= num <= 80:
        roman_amount = (num-50)//10
        roman_num += "L" + roman_amount * "X"
        num -= (50 + roman_amount*10)
    if 40 <= num < 50:
        roman_amount = num // 10
        roman_num += "XL"
        num -= roman_amount *10
    if 10 <= num < 40:
        roman_amount = num // 10
        roman_num += "X" * roman_amount
        num -= roman_amount * 10
    if 8 < num < 10:
        roman_amount = num-5
        roman_num += (5-roman_amount) * "I" + "X"
        num -= (roman_amount + 5)
    if 5 <= num <= 8:
        roman_amount = num - 5
        roman_num += "V" + "I" * roman_amount
        num -= (5 + roman_amount)
    if 4 == num:
        roman_num += "IV"
    if num <=3:
        roman_num += "I" * num

    return roman_num


print(int_to_roman(1994))    
"""
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
