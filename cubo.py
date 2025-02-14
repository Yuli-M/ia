from turtle import *


home()
#penup()
#dot()
#goto(50,50)
#dot(20, "blue")

penup()
puntos=10
espacio = 5
x,y = 0,0
x2, y2 = 15,15

#listas de coordenadas
A = []  # primer cuadrado
B = []  # segundo cuadrado

#primer cuadro
for i in range(puntos):
    goto(x + i * espacio, y)
    dot()
    if i == 0 or i == puntos-1:
        A.append((x + i * espacio, y)) 
        print(A)


for i in range(puntos):
    goto(x + (puntos-1)* espacio, y-i * espacio)
    dot()
    if i == 0 or i == puntos-1:
        A.append((x, y - i * espacio))
        print(A)

for i in range(puntos):
    goto(x + (puntos - 1 - i) * espacio, y - (puntos - 1) * espacio)
    dot()
    if i == 0 or i == puntos-1:
        A.append((x + (puntos - 1) * espacio, y - i * espacio)) 
        print(A)


for i in range(puntos):
    goto(x, y - (puntos - 1 - i) * espacio)
    dot()



        
#segundo cuadro
for i in range(puntos):
    goto(x2 + i * espacio, y2)
    dot()
    if i == 0 or i == puntos-1:
        B.append((x2 + i * espacio, y2)) 
        print(B)
for i in range(puntos):
    goto(x2 + (puntos-1)* espacio, y2-i * espacio)
    dot()
    if i == 0 or i == puntos-1:
        B.append((x2, y2 - i * espacio)) 
        print(B)

for i in range(puntos):
    goto(x2 + (puntos - 1 - i) * espacio, y2- (puntos - 1) * espacio)
    dot()
    if i == 0 or i == puntos-1:
        B.append((x2 + (puntos - 1) * espacio, y2 - i * espacio)) 
        print(B)

for i in range(puntos):
    goto(x2, y2- (puntos - 1 - i) * espacio)
    dot()



#unir dos cuadros
pencolor("green")

for i in range(6): 
    x1, y1 = A[i]  
    x2, y2 = B[i]  
    
    # punto intermedio
    for j in range(puntos):
        #  A y B para cada punto
        x = x1 + (x2 - x1) * j / (puntos - 1)
        y = y1 + (y2 - y1) * j / (puntos - 1)
        
        goto(x, y)
        dot()







# goto(B[0][0], B[0][1])
# dot()

# goto(A[1][0], A[1][1])
# dot()
# goto(B[1][0], B[1][1])
# dot()

# goto(A[2][0], A[2][1])
# dot()
# goto(B[2][0], B[2][1])
# dot()

# goto(A[3][0], A[3][1])
# dot()
# goto(B[3][0], B[3][1])
# dot()

done()
