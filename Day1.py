depth_file = open("Q1.txt", "r")

depth_list = []
increase_counter = 0
decrease_counter = 0

for line in depth_file:
	stripped_line = line.strip()
	d_line = stripped_line.split()
	depth_list.append(int(d_line[0]))

for i in range(len(depth_list) - 1):
	if depth_list[i] < depth_list[i + 1]:
		increase_counter += 1

print(increase_counter)