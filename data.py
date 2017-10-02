#data.py

def maxdata():
	path="data\currentdata.txt"
	game_max_data=0

	with open(path) as cd:
		lines=cd.readlines()
		for line in lines:
			game_max_data=max(int(line.rstrip()),game_max_data)
		return game_max_data

def write_data(data):
	path="data\currentdata.txt"

	with open(path,'a') as wd:
		wd.write(str(data))
		wd.write("\n")

#print("\n")
#print("\n")