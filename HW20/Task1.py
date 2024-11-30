# START

def is_valid_parentheses(s: str) -> bool:
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if not stack or stack.pop() != matching_parentheses[char]:
                return False
        else:
            return False

    return not stack


def remove_duplicates(sorted_list: list[int]) -> list[int]:
    if not sorted_list:
        return sorted_list

    write_index = 1
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[write_index - 1]:
            sorted_list[write_index] = sorted_list[i]
            write_index += 1

    return sorted_list[:write_index]



def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


# END
