value = input().split(".")
f = False

if len(value) > 1:
	temlen = int(len((value[1].split(" "))[0])) * int((value[1].split(" "))[1])
	val = value[0] + value[1].split(" ")[0]
	v3 = int((value[1].split(" "))[1])
	f = False
else:
	# 정수
	val = value[0].split(" ")[0]
	v3 = int(value[0].split(" ")[1])
	f = True

v1 = val
v2 = v1
lenv1 = len(v1)
lenv2 = len(v2)

if v1 == "0":
	print(0)

a = []
b = []
t = []

k = lenv1 - 1
for i in range(0, lenv1):
	a.append(int(v1[k]))
	k = k-1

k = lenv2 - 1
for i in range(0, lenv2):
	b.append(int(v2[k]))
	k = k-1

v1 = int(v1)
v2 = int(v2)

a_i = 0
b_i = 0
t_i = 0
t.append(0)
for k in range(0,v3-1):
	for i in range(0, lenv2):
		t.append(0)
		for j in range(0, lenv1):
			if i == 0:
				t.append(0)
				
			temp = (a[a_i] * b[b_i])/10
			#if k == 1:
			if(temp >= 1):
				#올림수가 있을때.
				if(j == lenv1-1):
					t.append(0)
					
				t[t_i + 1] = t[t_i + 1] + int(temp)
				temp = (temp - int(temp))
				temp = round(temp, 2)
				
			temp = int(temp * 10)
			
			t[t_i] = t[t_i] + temp
			
			if t[t_i] > 9:
				t[t_i + 1] = t[t_i + 1] + int(round((t[t_i]/10),2))
				t[t_i] = t[t_i] - (int(round((t[t_i]/10),2)) * 10)
				
			
			
			
			a_i = a_i + 1
			t_i = t_i + 1
			
		
		a_i = 0
		b_i = b_i + 1
		t_i = i + 1 

	#print()
	del a[:]
	for i in range(0, len(t)):
		#a.append(t[i])
		a.append(t[i])
	lenv1 = len(a)
	del t[:]
	t.append(0)
	a_i = 0
	b_i = 0
	t_i = 0

k = lenv1 - 1
flag = False;
result = []
for i in range(0, lenv1):
	if a[k] != 0:
		flag = True
	
	if flag:
		result.append(a[k])
		
	k = k-1
	
#print(temlen)
if f == False:
	lv = ""
	for i in range(0, len(result)):
		#print(result[i], end = '')
		lv += str(result[i])

	if len(lv) < temlen:
		print("0.", end='')
		for i in range(0, temlen - len(lv)):
			print("0", end='')
			
		print(lv)
	else:
		lv1 = ""
		for i in range(0, len(result)):
			if (len(lv) - temlen) == i:
				lv1 += "."
			lv1 += str(result[i])
			#print(lv[len(lv) - temlen])
		
		if lv1[0] == ".":
			print("0", end='')
		print(lv1)
else:
	for i in range(0, len(result)):
		print(result[i], end='')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

