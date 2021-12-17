move_file = open("Q2.txt", "r")

move_list = []
x = 0
y = 0
horizontal = 0
depth = 0
aim = 0

for line in move_file:
	stripped_line = line.strip()
	m_line = stripped_line.split()
	move_list.append(m_line)

for move in move_list:
	if move[0] == "forward":
		x = x + int(move[1])
	elif move[0] == "down":
		y = y + int(move[1])
	elif move[0] == "up":
		y = y - int(move[1])

final = x * y
print("Part 1 answer: " + str(final))

for move in move_list:
	if move[0] == "forward":
		horizontal = horizontal + int(move[1])
		depth = depth + (aim * int(move[1]))
	elif move[0] == "down":
		aim = aim + int(move[1])
	elif move[0] == "up":
		aim = aim - int(move[1])

final2 = horizontal * depth
print("Part 2 answer: " + str(final2))