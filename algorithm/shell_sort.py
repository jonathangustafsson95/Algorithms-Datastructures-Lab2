def sort(a_list):
    return shell_sort(a_list)


def shell_sort(a_list):
    count = 0

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            count += gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2
    return count


def gap_insertion_sort(a_list, start, gap):
    count = 0
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        count += 1

        while position >= gap and a_list[position - gap] > current_value:
            count += 1
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

    return count
