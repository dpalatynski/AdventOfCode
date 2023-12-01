def count_visible_trees(trees):
    map_of_trees = [list(grid) for grid in trees.split('\n')]
    distances = []
    visible = 2 * len(map_of_trees[0]) + 2 * (len(map_of_trees) - 2)
    for i in range(1, len(map_of_trees) - 1):
        for j in range(1, len(map_of_trees[0]) - 1):
            left_trees = map_of_trees[i][:j]
            right_trees = map_of_trees[i][j + 1:]
            top_trees = [map_of_trees[k][j] for k in range(i - 1, -1, -1)]
            below_trees = [map_of_trees[k][j] for k in range(i + 1, len(map_of_trees[i]))]
            distance = 1
            for trees in [left_trees[::-1], right_trees, top_trees, below_trees]:
                it = 0
                while map_of_trees[i][j] > trees[it]:
                    if it + 1 >= len(trees):
                        break
                    it += 1
                if it != 0:
                    distance *= it + 1

            distances.append(distance)
            if map_of_trees[i][j] > min([max(left_trees), max(right_trees), max(top_trees), max(below_trees)]):
                visible += 1

    return visible, max(distances)


sample_input = '''30373
25512
65332
33549
35390'''

puzzle_input = open("Day 8.txt").read()

print(count_visible_trees(sample_input))
print(count_visible_trees(puzzle_input))
