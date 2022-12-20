n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
A = {}
B = {}
for i in range(n):
    A[a[i]] = 1
for i in range(m):
    B[b[i]] = 1
for i in sorted(A):
    if i in B:
        print(i,end = " ")
print()
for i in sorted(A):
    if i not in B:
        print(i,end=" ")
print()
for i in sorted(B):
    if i not in A:
        print(i,end = " " )