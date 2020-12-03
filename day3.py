TREE = '#'

file1 = open('day3_input.txt', 'r')

slope = []

while True:
    line = file1.readline()

    if not line:
        break

    slope.append(list(line.strip()));

file1.close()


def get_num_of_trees(step_size, slope_line_step_size=1):
    slope_line_length = len(slope[0])
    tree_count = 0
    step = 0

    for slope_line in range(0, len(slope), slope_line_step_size):
        if slope[slope_line][step] == TREE:
            tree_count += 1

        step += step_size

        if step >= slope_line_length:
            step = step - slope_line_length

    return tree_count


answer_one = get_num_of_trees(3, 1)
answer_two = (
        get_num_of_trees(1, 1) *
        get_num_of_trees(3, 1) *
        get_num_of_trees(5, 1) *
        get_num_of_trees(7, 1) *
        get_num_of_trees(1, 2)
)
