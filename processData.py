f = open("results.txt", "r")

for x in range(4):
	f.readline()[:-1]

count = 0
current = dict()
results = []
for line in f:
	if count < 10:
		val = int(line.split()[1])
		dist = float(line.split()[4])
		
		if not 'values' in current:
			current['values'] = []
		if not 'distances' in current: 
			current['distances'] = []

		current['values'].append(val)
		current['distances'].append(dist)
		
	elif count == 10:
		count = count + 1
		continue
	else:
		actual = int(line.split()[4])
		current['actual'] = actual
		results.append(current)
		current = dict()
		count = -1 
	count = count + 1
print(results)
