depth_file = open("Q1.txt", "r")

depth_list = []
increase_counter = 0

for line in depth_file:
	stripped_line = line.strip()
	d_line = stripped_line.split()
	depth_list.append(int(d_line[0]))

for i in range(len(depth_list) - 1):
	if depth_list[i] < depth_list[i + 1]:
		increase_counter += 1

print("Part 1 answer: " + str(increase_counter))

first_value = 0
second_value = 0
increase_counter_2 = 0

for i in range(len(depth_list) - 3):
	first_value = depth_list[i] + depth_list[i + 1] + depth_list[i + 2]
	second_value = depth_list[i + 1] + depth_list[i + 2] + depth_list[i + 3]
	if first_value < second_value:
		increase_counter_2 += 1

print("Part 2 answer: " + str(increase_counter_2))