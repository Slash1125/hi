data = []
more50 =[]
less50 = []
odda = []
even = []
with open('practice.txt', 'r') as f:
    for line in f:
        data.append(line.strip()) 
data = list(map(int,data))
data.sort()
for i in data :
    if i > 50 :
        more50.append(i)
    else :
    	less50.append(i)
print('大於50的有:', more50)
print('小於50的有:', less50)
for ii in data :
    if ii % 2 == 0 :
    	even.append(ii)
    else :
    	odda.append(ii)
print('奇數有', odda)
print('偶數有', even)
