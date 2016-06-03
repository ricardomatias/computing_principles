"""
Merge function for 2048 game.

Start with a result list that contains the same number of 0's as the length of the line argument.
Iterate over the line input looking for non-zero entries.
For each non-zero entry, put the value into the next available entry of the result list (starting at position 0).
"""
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result_line = line[::]

    line_len = len(result_line)

    def in_range(idx):
        """
        checks if index is in list's range
        """
        return idx + 1 < line_len

    def sort_list(item1, item2):
        """
        sorts a list
        """
        if item2 == 0:
            return -1
        else:
            return 0

    result_line = sorted(result_line, cmp=sort_list)

    for idx in range(line_len):
        if in_range(idx) and not result_line[idx] == 0:
            if result_line[idx] == result_line[idx + 1]:
                result_line[idx] = result_line[idx] + result_line[idx + 1]
                result_line[idx + 1] = 0

    result_line = sorted(result_line, cmp=sort_list)

    return result_line


# Create tests to check the correctness of your code

def test_merge():
    """
    Test code for Solitaire Mancala
    """

    print merge([8, 8]), "Test Passed:", (merge([8, 8]) == [16, 0])
    print merge([2, 0, 2, 2]), "Test Passed:", (merge([2, 0, 2, 2]) == [4, 2, 0, 0])
    print merge([2, 0, 2, 4]), "Test Passed:", (merge([2, 0, 2, 4]) == [4, 4, 0, 0])
    print merge([0, 0, 2, 2]), "Test Passed:", (merge([0, 0, 2, 2]) == [4, 0, 0, 0])
    print merge([2, 2, 0, 0]), "Test Passed:", (merge([2, 2, 0, 0]) == [4, 0, 0, 0])
    print merge([2, 2, 2, 2, 2]), "Test Passed:", (merge([2, 2, 2, 2, 2]) == [4, 4, 2, 0, 0])
    print merge([8, 16, 16, 8]), "Test Passed:", (merge([8, 16, 16, 8]) == [8, 32, 8, 0])

test_merge()
