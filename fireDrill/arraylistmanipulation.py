list_of_numbers = []
for index in range(1, 16):
    list_of_numbers.append(index)
duplicate_list = list_of_numbers * 2

for number in list_of_numbers:
    if number in duplicate_list:
        duplicate_list.remove(number)


def add_third_elements(array: list) -> int:
    total = 0
    for num in range(2, len(array), 3):
        if type(array[num]) is not int:
            return TypeError("Invalid input")
        total += array[num]
    return total


def sum_first_middle_and_last_element(elements: list) -> int:
    if type(len(elements)) is not int:
        return TypeError("Invalid input")
    total = elements[-1] + elements[0] + elements[len(elements)//2]
    return total

