def oxygen(binary_list, i):
	updated_list = []
	one_counter = 0
	zero_counter = 0
	most_common = ''
	for binary in binary_list:
		if binary[i] == "1":
			one_counter += 1
		else:
			zero_counter += 1
	if one_counter >= zero_counter:
		most_common = "1"
	else:
		most_common = "0"
	for binary in binary_list:
		if binary[i] == most_common:
			updated_list.append(binary)
	return updated_list

def co2(binary_list, i):
	updated_list = []
	one_counter = 0
	zero_counter = 0
	least_common = ''
	for binary in binary_list:
		if binary[i] == "1":
			one_counter += 1
		else:
			zero_counter += 1
	if one_counter >= zero_counter:
		least_common = "0"
	else:
		least_common = "1"
	for binary in binary_list:
		if binary[i] == least_common:
			updated_list.append(binary)
	return updated_list

binary_file = open("Q3.txt", "r")

binary_row = []

for line in binary_file:
	stripped_line = line.strip()
	b_line = stripped_line.split()
	binary_row.append(b_line[0])

binary_len = len(binary_row[0])
oxygen_binary = binary_row
co2_binary = binary_row

for i in range(binary_len):
	oxygen_binary = oxygen(oxygen_binary, i)
	co2_binary = co2(co2_binary, i)
	if len(oxygen_binary) == 1:
		oxygen_rate = int(oxygen_binary[0], 2)
	if len(co2_binary) == 1:
		co2_rate = int(co2_binary[0], 2)

life_support = oxygen_rate * co2_rate

print("Day 3 Part 2 answer: " + str(life_support))