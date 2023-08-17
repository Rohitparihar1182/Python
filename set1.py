#set operations
s1={1,2,3}
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)

#set union
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
#OR
C=A.union(B)
print(C)

#set intersection
print(A&B)
#OR
C=A.intersection(B)
print(C)

#set difference
print(A-B)
#OR
C=A.difference(B)
D=B.difference(A)
print(C)
print(D)

#set symmetric difference
print(A^B)
C=A.symmetric_difference(B)
print(C)

