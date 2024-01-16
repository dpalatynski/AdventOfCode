# Day 23
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap 
import sys
import os
import imageio.v2 as imageio
sys.setrecursionlimit(100000)


def day23(my_input, part):
    data = my_input.split('\n')
    edges = {}
    for r, row in enumerate(data):
        for c, v in enumerate(row):
            if part == 2:
                if v in ".<>v^":
                    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                        ar, ac = r + dr, c + dc
                        if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                            continue
                        if data[ar][ac] in '.<>v^':
                            edges.setdefault((r, c), set()).add((ar, ac))
                            edges.setdefault((ar, ac), set()).add((r, c))
            elif part == 1:
                if v == ".":
                    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                        ar, ac = r + dr, c + dc
                        if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                            continue
                        if data[ar][ac] == ".":
                            edges.setdefault((r, c), set()).add((ar, ac))
                            edges.setdefault((ar, ac), set()).add((r, c))
                if v == ">":
                    edges.setdefault((r, c), set()).add((r, c + 1))
                    edges.setdefault((r, c - 1), set()).add((r, c))
                if v == "v":
                    edges.setdefault((r, c), set()).add((r + 1, c))
                    edges.setdefault((r - 1, c), set()).add((r, c))

    n, m = len(data), len(data[0])

    def dfs(r, c, d, edges, visited, path):
        if (r, c) == (n - 1, m - 2):
            return [(d, path + [(n - 1, m - 2)])]

        visited.add((r, c))
        all_paths = []
        
        for ar, ac in edges[(r, c)]:
            if (ar, ac) not in visited:
                new_path = path + [(ar, ac)]
                result = dfs(ar, ac, d + 1, edges, visited, new_path)
                all_paths.extend(result)
        
        visited.remove((r, c))
        return all_paths

    paths = dfs(1, 1, 0, edges, set(), [(1, 1)])
    longest_path = max(paths, key=lambda path: path[0])[0]

    return paths, longest_path+1


def create_gif_from_pngs(png_files, gif_filename, duration=0.5):
    frames = []
    for png_file in png_files:
        frames.append(imageio.imread(png_file))
    
    imageio.mimsave(gif_filename, frames, duration=duration, loop=0)


def clear_files(files):
    for file in files:
        os.remove(file)


def create_plot(my_input:str, steps:list, save=None):
    cmap = ListedColormap(['forestgreen', 'peru', 'gold'])

    grid_chars = np.array([list(row) for row in my_input.split('\n')]) 

    sample_input_numbers = my_input.replace('#', '0').replace('.', '1').replace('>', '1').replace('v', '1').replace('<', '1').replace('^', '1')
    grid_ints = np.array([list(row) for row in sample_input_numbers.split('\n')]).astype(int)
    for step in steps:
        grid_ints[step[0], step[1]] = 2

    plt.figure(facecolor='forestgreen')
    for i in range(0, grid_ints.shape[0]):
        for j in range(0, grid_ints.shape[1]):
            c = grid_chars[j, i]
            if c == 'v':
                plt.text(i-0.05, j, str(c), va='center', ha='center', color='brown')
            elif c == '>':
                plt.text(i, j, str(c), va='center', ha='center', color='brown')
            elif c == '<':
                plt.text(i, j+0.05, str(c), va='center', ha='center', color='brown')


    plt.title(f'Day 23. Find the longest path.')
    plt.text(8, 23, f'Steps: {save+1}', size=20, color='black')
    plt.axis('off')
    plt.imshow(grid_ints, cmap=cmap)
    plt.tight_layout()
    if type(save) == int:
        plt.savefig(f'frame{save}.png')
        plt.close()
    else:
        plt.show()
    plt.close()


def create_gif(my_input, filename, part=1):
    paths, longest_path = day23(my_input, part)
    frames = []
    for k in range(longest_path):
        el_to_plots = []
        for path in paths:
            if k < len(path[1]):
                el_to_plots.append(path[1][k])
        frame = create_plot(my_input, el_to_plots, k)
        frames.append(f'frame{k}.png')

    create_gif_from_pngs(frames, filename, duration=0.1)
    clear_files(frames)


sample_input = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''


if __name__ == "__main__":
    # Test 
    assert(day23(sample_input, 1)[1] == 94)
    assert(day23(sample_input, 2)[1] == 154)

    my_input = open(r"2023/inputs/Day_23.txt").read()
    # Results
    results = False
    if results:
        print(day23(my_input, 1)[1])
        print(day23(my_input, 2)[1])

    # Create gif
    gifs = True
    if gifs:
        create_gif(sample_input, '2023/images/sample_input_animation.gif', 1)
