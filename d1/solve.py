# https://adventofcode.com/2020/day/1

with open("input.txt", 'r') as infile, open("output.txt", 'w') as outfile:
	remainder = {}
	for line in infile:
		if remainder.get(2020-int(line), False):
			outfile.write(str(int(line)*(2020-int(line))))
		else:
			remainder[int(line)] = int(line)

