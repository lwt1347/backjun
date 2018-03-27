#value = input().split("")
loof = input()
loofa = []
for i in range(0, int(loof)):
	loofa.append(input())


a = [0] * 3
a[0] = 1
a[1] = 2
a[2] = 4
result = 0
for j in range(0, int(loof)):
	val = int(loofa[j])
	if val == 1:
		print(1)
	elif val == 2:
		print(2)
	elif val == 3:
		print(4)
	for i in range(3, val):
		result = a[0] + a[1] + a[2]
		a[0] = a[1]
		a[1] = a[2]
		a[2] = result
	if val != 1 and val !=2 and val !=3:	
		print(result)
	
	result = 0
	a[0] = 1
	a[1] = 2
	a[2] = 4
	
	
	