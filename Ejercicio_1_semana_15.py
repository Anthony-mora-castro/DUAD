def my_first_bubble_sort (list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1):
        has_made_changes = False

        for index in range (0, len(list_to_sort)-1 - outer_index):

            current_element = list_to_sort[index]

            next_element = list_to_sort[index + 1]

            print(f'Iteracion {outer_index}.{index}, elemento actual: {current_element}, siguiente elemento:{next_element}')


            if current_element > next_element:
                
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element

                has_made_changes = True
        if not has_made_changes:
            return


list_of_ages = [ 12, 2, 45, 37, 81, 82,20]

my_first_bubble_sort(list_of_ages)

print(list_of_ages)

