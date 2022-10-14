c=0
r=int(input("Введите количество чисел в первом массиве"))
A = [0] * r
for i in range (r):
    print(i+1, "Введите число:",)
    A[i]=float(input())
g=int(input("Введите количество чисел во втором массиве"))
B = [0] * g
for j in range (g):
    print(j+1, "Введите число:",)
    B[j]=float(input())
for i in range(r):
    for j in range(r):
        if A[i] == B[j]:
            print(A[i])
