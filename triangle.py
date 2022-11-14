# This takes in a string and a sub string, and calculates the number of sub strings that can be made without using
# the substring submitted
# i.e. input('abc','defabcghi) produces 12 possible substrings. def, de, d, ef, e, f, ghi, gh, g, hi, h, i


def triangles(sub_string, main_string):
    input_array = main_string.split(sub_string)
    total_sub_strings = 0
    for val in input_array:
        n = len(val)
        sub_string_count = (n * (n + 1)) / 2
        total_sub_strings += sub_string_count
    return total_sub_strings


print(triangles('abc', 'defabcghi'))
