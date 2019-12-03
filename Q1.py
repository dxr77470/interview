#1

import sys
import re


def read_text(filname):
    
    items = {}
    try:
        with open(filename, 'r') as t_file:
            for line in t_file:
                initial_data = line.rstrip()
                found_non_numeric = re.search(r'[^0-9]',  initial_data)
                if found_non_numeric:
                    text_start_index = found_non_numeric.start()
                else:
                    continue

               
                try:
                    number = int( initial_data[:text_start_index])
                except ValueError:
                    number = sys.maxsize

                number_values = items.setdefault(number, [])
                number_values.append((text_start_index,  initial_data))
    except IOError as io_error:
        print(io_error.strerror, ':', filename)
        items = None

    return items


def sort_data(items):

    if not isinstance(items, dict):
        print('Incorrect Data Format')
        return None
    final_result = []
    try:
        sorted_numbers = sorted(items)
        alpha_num = re.compile(r'[\W_]+')
        for number in sorted_numbers:
            sorting_values = map(lambda item: (alpha_num.sub('', item[1][item[0]:]).lower(), item), items[number])
            final_result += map(lambda value: value[1][1], sorted(sorting_values))
    except Exception as ex:
        print(ex)
        final_result = None
    return final_result


def write_output(values, filename='output.txt'):
    try:
        with open(filename, 'w') as output_file:
            for value in values:
                if not isinstance(value, str):
                    raise TypeError

                print(value, file=output_file)

    except IOError as io_error:
        print(io_error.strerror, ':', filename)
        return False
    except TypeError:
        print('Data input error')
        return False

    return True


# Standalone script mode
if __name__ == '__main__':
   
    argc = len(sys.argv)
    if argc < 2:
        print(
            'No input received, Please pass input in the following order :\n',
            '\t python3 Q1.py <input_filename> <output_filename>'
        )
        sys.exit(1)

 
    data = read_text(sys.argv[1])
    if data is None:
        sys.exit(1)

 
    final_values = sort_data(data)
    if not final_values:
        sys.exit(1)

  
    if argc == 2:
        solution = write_output(final_values)
   
    else:
        solution = write_output(final_values, filename=sys.argv[2])

    print('Data was successfully sorted' if result else 'Failed to sort data')