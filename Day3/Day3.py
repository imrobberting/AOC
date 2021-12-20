from collections import Counter

binary_file = open("Q3.txt", "r")

binary_row = []

for line in binary_file:
	stripped_line = line.strip()
	b_line = stripped_line.split()
	binary_row.append(b_line[0])

binary_len = len(binary_row[0])

binary_column = [''] * binary_len

for i in range(len(binary_row)):
	for j in range(len(binary_row[i])):
		binary_column[j] = binary_column[j] + binary_row[i][j]

gamma = ''
epsilon = ''

for new_binary in binary_column:
	gamma = gamma + Counter(new_binary).most_common(2)[0][0]
	epsilon = epsilon + Counter(new_binary).most_common(2)[1][0]

gamma_rate = int(gamma, 2)
epsilon_rate = int(epsilon, 2)
power_consumption = gamma_rate * epsilon_rate

print("Day 3 Part 1 answer: " + str(power_consumption))