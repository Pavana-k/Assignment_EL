import sys
args=sys.argv[1]
with open("ip.txt") as f:
	for line in f:
		f=line.split("\n")
		if args in line:
			print("ip present :",args)
			sys.exit()