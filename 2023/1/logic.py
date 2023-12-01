import re

def q1_sum_calibration_values(document):
    calibration_value = 0
    with open(document, 'r') as f:
        for line in f:
            extracted_value = int(get_first_num(line) + get_last_num(line))
            calibration_value += extracted_value
    print('calibration_value: ', calibration_value)

def get_first_num(line):
    for char in line:
        if char.isnumeric():
            return char

def get_last_num(line):
    for char in reversed(line):
     if char.isnumeric():
            return char

def get_search_strgins():
    digits_search_strings = [str(x) for x in range(10)]
    non_digit_search_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
    return digits_search_strings + non_digit_search_strings

def map_str_to_digit(item):
    str_to_digit_mapping = {
        'one' : '1', 
        'two' : '2',
        'three' : '3', 
        'four' : '4', 
        'five' : '5', 
        'six' : '6', 
        'seven' : '7', 
        'eight' : '8', 
        'nine' : '9'
    }

    try:
        return str(int(item))
    except:
        return str_to_digit_mapping[item]

def q2_sum_calibration_values(document):
    calibration_value = 0
    with open(document, 'r') as f:
        for line in f:
            values_locations = extract_values_locations(line)
            values_locations.sort()
            extracted_value = int(values_locations[0][-1] + values_locations[-1][-1])
            calibration_value += extracted_value
    print('calibration_value: ', calibration_value)

def extract_values_locations(line):
    values_location = []
    for search_string in get_search_strgins():
        locations = [m.start() for m in re.finditer(search_string, line)]

        for loc in locations:
            values_location.append((loc, search_string, map_str_to_digit(search_string)))
    return values_location


if __name__ == "__main__":
    print(get_search_strgins())