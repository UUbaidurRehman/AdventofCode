with open('input2.txt', 'r') as file:
    data = file.read().strip()

game_ids_p1 = []
game_cubes = []

for line in data.split('\n'):
    _, game_data = line.split(':')
    ball_set = game_data.split(';')

    R = []
    G = []
    B = []

    for ball_set in ball_set:
        balls = ball_set.split(',')

        for ball in balls:
            ball = ball.strip().split(' ')
            value = int(ball[0])

            if 'green' in ball:
                G.append(value)
            if 'red' in ball:
                R.append(value)
            if 'blue' in ball:
                B.append(value)

    game_cubes.append(max(R) * max(G) * max(B))

total_p2 = sum(game_cubes)
print(total_p2)