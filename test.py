#test.py

path="data\currentdata.txt"

with open (path) as data:
	line=data.readlines()
#line.trim()
current=0

for data in line:
	#r=int(data.rstrip())
	current=max(int(data.rstrip()),current)
	#max=max(int(data),max)

print(current)