def convert_temperature(temp):
    try:
        # check length of input and count the number of alphabetic characters
        if len(temp) < 2:
            raise ValueError(
                'Wrong input. It must contain number and unit of temperature')
        count = 0
        for t in temp:
            if t.isalpha():
                count += 1
        if count > 1:
            raise ValueError(
                'Wrong input. It must contain only one unit of temperature')
        # extract the last character as the unit and the rest as the number
        char = temp[-1].upper()
        number = float(temp[:-1].strip())
        # convertion
        c_to_f = (number * 9/5) + 32
        f_to_c = (number - 32) * 5/9
        
        if char == 'C':
             result = c_to_f
        elif char == 'F':
             result = f_to_c
        else:
                raise ValueError(
                    'Wrong input. It must contain only one unit of temperature (C or F)')
    except ValueError as e:
            print(e)
    else:
         return result


print(convert_temperature('89 b'))
