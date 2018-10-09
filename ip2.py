import sys
args=sys.argv[1]
with open("ip2.txt") as f:
	for line in f:
		f=line.split(" ")
		if args in line:
			print("ip present :",args)
			sys.exit()