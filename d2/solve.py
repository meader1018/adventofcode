# https://adventofcode.com/2020/day/2

with open("input.txt", 'r') as infile, open("output.txt", 'w') as outfile:
	valid_passwords_1 = 0
	valid_passwords_2 = 0
	boundary_low, boundary_high = 0, 0
	split_string = []
	for line in infile:
		split_string = line.split(" ")
		char = split_string[1][0]
		num_occurrences = split_string[2].count(char)
		split_string[0] = split_string[0].replace("-", "")
		range_len = len(split_string[0])		
		boundary_low = int(split_string[0][0:range_len//2])
		boundary_high = int(split_string[0][range_len//2:])

		# following conditionals only work for boundary_high < 100
		# because of how boundaries are calculated
		if boundary_low <= num_occurrences <= boundary_high:
			valid_passwords_1 += 1
			
		if (split_string[2][boundary_low-1] == char) ^ (split_string[2][boundary_high-1] == char):
			valid_passwords_2 += 1

	outfile.write("Part 1 Solution: " + str(valid_passwords_1) + "\n")
	outfile.write("part 2 Solution: " + str(valid_passwords_2))