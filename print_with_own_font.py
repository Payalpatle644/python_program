n = input("Enter the name to print: ")
length = len(n)
l = ""

for a in range(0, length):
	b= name[a]
	b = b.upper()
	
	if (b == "A"):
		print("..######..\n..#....#..\n..######..", end = " ")
		print("\n..#....#..\n..#....#..\n")
		
	elif (b == "B"):
		print("..######..\n..#....#..\n..#####...", end = " ")
		print("\n..#....#..\n..######..\n")
		
	elif (b == "C"):
		print("..######..\n..#.......\n..#.......", end = " ")
		print("\n..#.......\n..######..\n")
		
	elif (b == "D"):
		print("..#####...\n..#....#..\n..#....#..", end = " ")
		print("\n..#....#..\n..#####...\n")
		
	elif (b == "E"):
		print("..######..\n..#.......\n..#####...", end = " ")
		print("\n..#.......\n..######..\n")
		
	elif (b == "F"):
		print("..######..\n..#.......\n..#####...", end = " ")
		print("\n..#.......\n..#.......\n")
		
	elif (b == "G"):
		print("..######..\n..#.......\n..#.####..", end = " ")
		print("\n..#....#..\n..#####...\n")
		
	elif (b == "H"):
		print("..#....#..\n..#....#..\n..######..", end = " ")
		print("\n..#....#..\n..#....#..\n")
		
	elif (b == "I"):
		print("..######..\n....##....\n....##....", end = " ")
		print("\n....##....\n..######..\n")
		
	elif (b == "J"):
		print("..######..\n....##....\n....##....", end = " ")
		print("\n..#.##....\n..####....\n")
		
	elif (b == "K"):
		print("..#...#...\n..#..#....\n..##......", end = " ")
		print("\n..#..#....\n..#...#...\n")
		
	elif (b == "L"):
		print("..#.......\n..#.......\n..#.......", end = " ")
		print("\n..#.......\n..######..\n")
		
	elif (b == "M"):
		print("..#....#..\n..##..##..\n..#.##.#..", end = " ")
		print("\n..#....#..\n..#....#..\n")
		
	elif (b == "N"):
		print("..#....#..\n..##...#..\n..#.#..#..", end = " ")
		print("\n..#..#.#..\n..#...##..\n")
		
	elif (b == "O"):
		print("..######..\n..#....#..\n..#....#..", end = " ")
		print("\n..#....#..\n..######..\n")
		
	elif (b == "P"):
		print("..######..\n..#....#..\n..######..", end = " ")
		print("\n..#.......\n..#.......\n")
		
	elif (b == "Q"):
		print("..######..\n..#....#..\n..#.#..#..", end = " ")
		print("\n..#..#.#..\n..######..\n")
		
	elif (b == "R"):
		print("..######..\n..#....#..\n..#.##...", end = " ")
		print("\n..#...#...\n..#....#..\n")
		
	elif (b == "S"):
		print("..######..\n..#.......\n..######..", end = " ")
		print("\n.......#..\n..######..\n")
		
	elif (b == "T"):
		print("..######..\n....##....\n....##....", end = " ")
		print("\n....##....\n....##....\n")
		
	elif (b == "U"):
		print("..#....#..\n..#....#..\n..#....#..", end = " ")
		print("\n..#....#..\n..######..\n")
		
	elif (b == "V"):
		print("..#....#..\n..#....#..\n..#....#..", end = " ")
		print("\n...#..#...\n....##....\n")
		
	elif (b == "W"):
		print("..#....#..\n..#....#..\n..#.##.#..", end = " ")
		print("\n..##..##..\n..#....#..\n")
		
	elif (b == "X"):
		print("..#....#..\n...#..#...\n....##....", end = " ")
		print("\n...#..#...\n..#....#..\n")
		
	elif (b == "Y"):
		print("..#....#..\n...#..#...\n....##....", end = " ")
		print("\n....##....\n....##....\n")
		
	elif (b == "Z"):
		print("..######..\n......#...\n.....#....", end = " ")
		print("\n....#.....\n..######..\n")
		
	elif (b == " "):
		print("..........\n..........\n..........", end = " ")
		print("\n..........\n\n")
		
	elif (b == "."):
		print("----..----\n\n")
