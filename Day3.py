snowlines = ['..##.......','#...#...#..','.#....#..#.','..#.#...#.#','.#...##..#.',
'..#.##.....','.#.#.#....#','.#........#','#.##...#...','#...##....#','.#..#...#.#']

routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

with open('Day3a.txt') as snow:
    snowlines = []
    for i in snow.readlines():
        snowlines.append(i.strip())

def route_check(x_move, y_move, hill):
    trees = 0
    start_x = 0
    start_y = 0
    patt_length = len(hill[0])
    hill_height = len(hill)
    while start_y < hill_height:
        if start_x > patt_length - 1:
            start_x = start_x - patt_length
        check = snowlines[start_y][start_x]
        if check == '#':
            trees += 1
        start_x += x_move
        start_y += y_move
    return trees

total_trees = 1

for route in routes:
    total_trees *= route_check(route[0],route[1],snowlines)

print(f'There are {route_check(3,1,snowlines)} on the route.')

print(f'There are {total_trees} on all the routes')

