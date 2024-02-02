# Conditional

# kalau kita mau check 
# apakah variable lebih dari 10
a = 11
print(a > 10)

# kalau kita mau check 
# apakah variable sama dengan [1,2,3,4]
arr1 = [1,2,3,4]
arr2 = [1,2,3,4]
print(arr1 == arr2) # TRUE
# bagaimana kalau kita ingin memastikan
# bahwa id dan value dari variable SAMA PERSIS
print(id(arr1),id(arr2)) # Memiliki ID yang berbeda

# copy id
arr3 = arr1
print(id(arr1),id(arr3)) 
print(arr1 is arr3) # menyamakan variable value dan id
print("==========")

# IF ELSE statement
if (arr1[0] == 0):
    print("ok")
# (arr1[0] > 0) => expression / condition
# print("ok") => statement
    
# bagaimana kalau kita mau menambahkan ELSE
elif(arr1[1] == 2):
    print("else if")
else:
    print("else")

# one line if statement / ternary statement

# Program to demonstrate conditional operator
a, b = 10, 20
# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)

if a < b:
    min = a 
else:
    min = b

if (a < b): min = min+1; min = min+3
print("==========")

# LOOPING
# while loop
i= 0
while (i < 10):
    print(i)
    i += 1 # update statement
    # jika tidak ada update statement: infinit loop
else: 
    print("finish")
print("==========")

# jika i == 100, akan mengakhiri loop
i = 0
while (i < 1000):
    i += 1
    
    # continue statement
    if i == 50: continue

    print("i = ", i)
    # jika i == 100, dia akan mengakhiri loop
    
    # break statement
    if i== 100: break
else:
    print("end of loop")
print("==========")

# for loop
# for (let i = 0; i < 10; i++)
for i in range(10):
    print(i)

arr4 = [1,2,3,4,5,6,7,8,9,0]
# bagaimana caranya kita looping
# dan menampilkan seluruh isi list
# 4 solusi

print("==========")
# SOLUSI 1
for num in arr4:
    print(num)

print("==========")
# SOLUSI 2
i = 0
while(i < len(arr4)):
    print(arr4[i])
    i += 1

print("==========")
# SOLUSI 3 
for i in range(len(arr4)):
    print(arr4[i])

print("==========")
# SOLUSI 4
while len(arr4):
    print(arr4.pop(0))

# deep dive range
# override function
ran = range(10)
print(ran, type(ran))

print("==========")
ran2 = range(10, 100)
for i in ran2:
    print(i)

print("==========")
ran2 = range(10, 100, 10)
for i in ran2:
    print(i)

# apakah range bisa decremental?
print("==========")
ran3 = range(100, 10, -5)
for i in ran3:
    print(i)

# apakah bisa looping suatu dictionary? 
print("==========")
dic1 = {"key1" :"val1", "key2":"val2"}
for x in dic1:
    print(x, dic1[x]) # x => key; print key dari dictionary

for x in dic1.values():
    print(x) # x => value; print values dari dictionary

for key, value in dic1.items():
    print(key, value)

# CHALLENGE
# mencari angka yang jumlahnya 2
# untuk angka yang jumlah 2, dia akan diprint
    
# in: [1,2,3,4,2,5,6,7,1,8,2,3]
# out: 1, 3
# in: [3,44,2,21,33,4,2,33,44,5,5]
# out: 44,33,5,2
print("==========") 
input = [1,2,3,4,2,5,6,7,1,8,2,3]
dic2 = {}
for num in input:
    if num in dic2: dic2[num] += 1
    else: dic2[num] = 1
res = []
for key, val in dic2.items():
    if val == 2: res.append(key)
print(res)