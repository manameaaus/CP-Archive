'''Tetrahedron. Tetrahedron has 4 triangular faces.
Cube. Cube has 6 square faces.
Octahedron. Octahedron has 8 triangular faces.
Dodecahedron. Dodecahedron has 12 pentagonal faces.
Icosahedron. Icosahedron has 20 triangular faces.'''
t = int(input())
s = 0
for i in range(t):
    j = input()
    if j[0]=="T":
        s+=4
    elif j[0]=="C":
        s+=6
    elif j[0]=="O":
        s+=8
    elif j[0]=="D":
        s+=12
    elif j[0]=="I":
        s+=20
print(s)