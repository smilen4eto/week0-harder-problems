def prepare_meal(number):
    output = ''
    meal_copy = number
    was_divided_by_three = 0
    while meal_copy % 3 == 0 and number != 0:
        if was_divided_by_three:
            output += ' '
        output += 'spam'
        meal_copy /= 3
        was_divided_by_three = 1
    if meal_copy % 5 == 0 and number != 0:
        if was_divided_by_three:
            output += ' and '
        output += 'eggs'
    return output

print(prepare_meal(30))
