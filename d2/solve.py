# https://adventofcode.com/2020/day/2

with open("input.txt", 'r') as infile, open("output.txt", 'w') as outfile:
	valid_passwords = 0
	broken_string = []
	for line in infile:
		broken_string = line.split(" ")
		num_occurrences = broken_string[2].count(broken_string[1][0])
		broken_string[0] = broken_string[0].replace("-", "")
		size_range = len(broken_string[0])		
		
		# following conditional only works for upper_bound < 100
		if int(broken_string[0][0:size_range//2]) <= num_occurrences <= int(broken_string[0][size_range//2:]):
			valid_passwords += 1
	outfile.write("Part 1 Solution: " + str(valid_passwords))