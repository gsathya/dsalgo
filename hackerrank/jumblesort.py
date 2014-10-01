import sys

def main():
    try:
        all_elements = raw_input()
    except EOFError:
        return
    
    if all_elements == '':
        return

    int_positions = []
    strings = []
    ints = []

    for an_element in all_elements:
        is_int = True

        try:
            int(an_element)
        except ValueError:
            is_int = False

        int_positions.append(is_int)

        if is_int:
            ints.append(int(an_element))
        else:
            strings.append(an_element)

    ints.sort()
    strings.sort()

    next_int_to_take = 0
    next_string_to_take = 0
    next_index = 0

    for an_element in all_elements:
        do_we_need_an_int = int_positions[next_index]
        next_index += 1

        if do_we_need_an_int:
            sys.stdout.write(str(ints[next_int_to_take]) + " ")
            next_int_to_take += 1
        else:
            sys.stdout.write(strings[next_string_to_take] + " ")
            next_string_to_take += 1

    sys.stdout.write('\n')

main()
