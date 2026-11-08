import random

rows = int(input('Enter rows: '))
columns = int(input('Enter Columns: '))
treasure_map = []
total_treasures = 0

for i in range(rows):
    row = []

    for j in range(columns):
        number = random.randint(0,100)

        if number < 30:
            row.append('T')
            total_treasures += 1
        elif number < 50:
            row.append('X')
        else:
            row.append('E')
    treasure_map.append(row)
print(f'Total Treasures : {total_treasures}')

for i in range(rows):
    for j in range(columns):
        print(treasure_map[i][j], end='')
    print()

score = 0
traps_encountered = 0
locations_explored = 0
streak = 0

while total_treasures > 0:
    r = int(input(f'Enter row (0 to {rows-1}) : '))
    c = int(input(f'Enter column (0 to {columns-1}) : '))

    location = (r,c)

    if treasure_map[location[0]][location[1]] == 'T'
        score += 10
        total_treasures -= 1
        treasure_map[location[0]][location[1]] = 'V'
        locations_explored += 1
        streak += 1

        if streak >= 2:
            score += 5
            print('Treasure found! +15 points (including bonus).')
        else:
            print('Treasure found! +10 points.')
    elif treasure_map[location[0]][location[1]] == 'X':
        score -= 5
        traps_encountered += 1
        locations_explored += 1
        treasure_map[location[0]][location[1]] = 'V':
        streak = 0
        print('You hit a trap! -5 points.')
    elif treasure_map[location[0]][location[1]] == 'E':
        treasure_map[location[0]][location[1]] = 'V'
        locations_explored += 1
        streak = 0
        print('Nothing found at this location.')
    elif treasure_map[location[0]][location[1]] == 'V':
        print('You have already explored this location.')

    for i in range(rows):
        for j in range(columns):
            print(treasure_map[i][j], end='')
        print()
    print(f'Current score = {score}')
    print(f'Remaining Treasures = {total_treasures}')

print('Congratulations! All treasures have been collected!')
print('Final Map:')

for i in range(rows):
    for j in range(columns):
        print(treasure_map[i][j], end='')
    print()

print(f'Final Score = {score}')
print(f'Traps Encountered = {traps_encountered}')
print(f'Locations explored = {locations_explored}')