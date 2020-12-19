# https://adventofcode.com/2020/day/1

with open("input.txt", 'r') as infile, open("output.txt", 'w') as outfile:
	remainder = {}
	part_two_found = False
	for line in infile:
		num = int(line)
		if remainder.get(2020-num, False):
			outfile.write("Part 1 Solution: " + str(num*(2020-num)) + "\n")
		else:
			remainder[num] = num
		if not part_two_found:	
			for num2 in remainder:
				#check part_two_found flag twice, once within for loop and once for the for loop to run
				if remainder.get(2020-num-num2, False) and not part_two_found:
					part_two_found = True
					outfile.write("Part 2 Solution: " + str(num*num2*(2020-num-num2)) + "\n")


