def complete_inventory(warehouse_1, x, warehouse_2, y):
    back_index = len(warehouse_1) - 1
    first_pointer = x - 1
    second_pointer = y - 1

    while second_pointer >= 0:
        if first_pointer >= 0 and warehouse_1[first_pointer] >= warehouse_2[second_pointer]:
            warehouse_1[back_index] = warehouse_1[first_pointer]
            first_pointer -= 1
        else:
            warehouse_1[back_index] = warehouse_2[second_pointer]
            second_pointer -= 1
        back_index -= 1

    return warehouse_1

# Test cases
print(complete_inventory([2,3,4,0,0,0], 3, [1,5,9], 3))  # Output: [1, 2, 3, 4, 5, 9]
print(complete_inventory([1,8,0,0,0], 2, [1,1,5], 3))