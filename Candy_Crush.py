import random
dim= 11
matrice = [[0 for x in range(dim)]for y in range(dim)]
culori=['r' , 'g' , 'a' , 'v']
for i in range(dim):
    for j in range (dim):
        rand=random.choice(culori)
        matrice[i][j]=rand
def eliminare_3_linii(matrice):
    for i in range(dim):
        for j in range(0, 11, 1):
             if((matrice[i][j]=='*')):
                for k in range(i-1,-1,-1):
                     matrice[k+1][j]=matrice[k][j]
                rand = random.choice(culori)
                matrice[0][j] = rand
    return 1
def cautare_3_linii_orizontal(matrice):
    for i in range(dim):
        for j in range(0, 8, 1):
             if((matrice[i][j]==matrice[i][j+1]) and (matrice[i][j+1]==matrice[i][j+2])):
                 matrice[i][j]='*'
                 matrice[i][j+1]='*'
                 matrice[i][j+2]='*'
                 return 1
    return 0;
def afisare(matrice):
    for i in range(dim):
        for j in range (dim):
            print(matrice[i][j] , end=" ")
        print()
# if(cautare_3_linii_orizontal(matrice)==1):
#     afisare(matrice)
#     eliminare_3_linii(matrice)
# print()
# print("---------------------")
# print()
# afisare(matrice)
def cautare_plus(matrice):
    for i in range (1,10,1):
        for j in range(1, 10, 1):
            if(matrice[i][j]==matrice[i][j-1] and matrice[i][j]==matrice[i][j+1]
                and matrice[i][j]==matrice[i-1][j] and matrice[i][j]==matrice[i+1][j]):
                matrice[i][j]='*'
                matrice[i][j-1]='*'
                matrice[i][j+1]='*'
                matrice[i-1][j]='*'
                matrice[i+1][j]='*'
                return 1
def eliminare_plus(matrice):
    for i in range(dim):
        for j in range (dim):
            if(matrice[i][j]=='*'):
                for k in range (i-1,-1,-1):
                    matrice[k+3][j]=matrice[k][j]
                for k in range(i , -1, -1):
                    matrice[k+1][j-1] = matrice[k][j-1]
                    matrice[k+1][j+1] = matrice[k][j+1]
                matrice[0][j] = random.choice(culori)
                matrice[1][j] = random.choice(culori)
                matrice[2][j] = random.choice(culori)
                matrice[0][j-1] = random.choice(culori)
                matrice[0][j+1] = random.choice(culori)
                return 1
# L X X
# L X X
# L L L
def cautare_L_poz1(matrice):
   for i in range (0,9,1):
    for j in range(1,9, 1):
        if(matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j]
         and matrice[i][j]==matrice[i+2][j+1] and matrice[i][j]==matrice[i+2][j+2]):
            matrice[i][j]='*'
            matrice[i+1][j] = '*'
            matrice[i+2][j] = '*'
            matrice[i+2][j+1] = '*'
            matrice[i+2][j+2] = '*'
            return 1
def sterge_L_poz1(matrice):
    for i in range(dim):
        for j in range (dim):
            if(matrice[i][j]=='*'):
                for k in range(i+2,-1,-1):
                    matrice[k][j]=matrice[k-3][j]
                    matrice[k][j+1] = matrice[k - 1][j+1]
                    matrice[k][j+2] = matrice[k - 1][j+2]
                matrice[0][j]=random.choice(culori)
                matrice[0][j+1] = random.choice(culori)
                matrice[0][j+2] = random.choice(culori)
                return 1
# X X L
# X X L
# L L L
def cautare_L_poz2(matrice):
    for i in range(0,9,1):
        for j in range(2, 10, 1):
            if(matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j]
            and matrice[i][j]==matrice[i+2][j-1] and matrice[i][j]==matrice[i+2][j-2]):
                matrice[i][j]='*'
                matrice[i+1][j]='*'
                matrice[i+2][j]='*'
                matrice[i+2][j-1]='*'
                matrice[i+2][j-2]='*'
                return 1
# L L L
# X X L
# X X L
def cautare_L_poz3(matrice):
    for i in range(0,9,1):
        for j in range(2, 10, 1):
            if(matrice[i][j]==matrice[i-1][j] and matrice[i][j]==matrice[i-2][j]
            and matrice[i][j]==matrice[i-2][j-1] and matrice[i][j]==matrice[i-2][j-2]):
                matrice[i][j]='*'
                matrice[i-1][j]='*'
                matrice[i-2][j]='*'
                matrice[i-2][j-1]='*'
                matrice[i-2][j-2]='*'
                return 1
# L L L
# L X X
# L X X
def cautare_L_poz4(matrice):
    for i in range(0,9,1):
        for j in range(0, 9, 1):
            if(matrice[i][j]==matrice[i][j+1] and matrice[i][j]==matrice[i][j+2]
            and matrice[i-1][j]==matrice[i][j] and matrice[i][j]==matrice[i-2][j]):
                matrice[i][j]='*'
                matrice[i][j+1] = '*'
                matrice[i][j+2] = '*'
                matrice[i-1][j] = '*'
                matrice[i-2][j] = '*'
                return 1
# T T T
# X T X
# X T X
def cautare_T_poz1(matrice):
    for i in range(0,9,1):
        for j in range(1,10,1):
            if(matrice[i][j]==matrice[i][j-1] and matrice[i][j]==matrice[i][j+1]
            and matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j]):
                matrice[i][j] = '*'
                matrice[i][j+1] = '*'
                matrice[i][j-1] = '*'
                matrice[i+1][j] = '*'
                matrice[i+2][j] = '*'
                return 1
def sterge_T_poz1(matrice):
    for i in range(0,9,1):
        for j in range(1,10,1):
            if(matrice[i][j]=='*'):
                for k in range(i,-1,-1):
                    matrice[k][j]=matrice[k-1][j]
                    matrice[k][j+2]=matrice[k-1][j+2]
                    matrice[k+2][j+1]=matrice[k-1][j+1]
                matrice[0][j]=random.choice(culori)
                matrice[0][j+2]=random.choice(culori)
                matrice[0][j+1] = random.choice(culori)
                matrice[1][j+1] = random.choice(culori)
                matrice[2][j+1] = random.choice(culori)
                return 1
# T X X
# T T T
# T X X
def cautare_T_poz2(matrice):
    for i in range(0,9,1):
        for j in range (0,9,1):
            if(matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j]
            and matrice[i][j]==matrice[i+1][j+1] and matrice[i][j]==matrice[i+1][j+2]):
                matrice[i][j]='*'
                matrice[i+1][j] = '*'
                matrice[i+2][j] = '*'
                matrice[i+1][j+1] = '*'
                matrice[i+1][j+2] = '*'
                return 1
def sterge_T_poz2(matrice):
    for i in range(0,9,1):
        for j in range (0,9,1):
            if (matrice[i][j] == '*'):
                for k in range(i,-1,-1):
                    matrice[k+2][j]=matrice[k-1][j]
                    matrice[k+1][j+1] = matrice[k][j+1]
                    matrice[k+1][j + 2] = matrice[k][j+2]
                matrice[0][j]=random.choice(culori)
                matrice[1][j] = random.choice(culori)
                matrice[2][j] = random.choice(culori)
                matrice[0][j+1] = random.choice(culori)
                matrice[0][j+2] = random.choice(culori)
                return 1
# X X T
# T T T
# X X T
def cautare_T_poz3(matrice):
    for i in range(1,9,1):
        for j in range(2,dim,1):
            if(matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j]
            and matrice[i+1][j-1]==matrice[i+1][j-2] and matrice[i+1][j]==matrice[i+1][j-2]):
                matrice[i][j]='*'
                matrice[i+1][j] = '*'
                matrice[i+2][j] = '*'
                matrice[i+1][j-1] = '*'
                matrice[i+1][j-2] = '*'
                return 1
def sterge_T_poz3(matrice):
    for i in range(1,9,1):
        for j in range(2,dim,1):
            if(matrice[i][j]=='*'):
                for k in range(i, -1, -1):
                    matrice[k+2][j] = matrice[k-1][j]
                    matrice[k+1][j-1] = matrice[k][j-1]
                    matrice[k+1][j-2] = matrice[k][j-2]
                matrice[0][j] = random.choice(culori)
                matrice[1][j] = random.choice(culori)
                matrice[2][j] = random.choice(culori)
                matrice[0][j-1] = random.choice(culori)
                matrice[0][j-2] = random.choice(culori)
                return 1

# X T X
# X T X
# T T T
def cautare_T_poz4(matrice):
    for i in range(0,9,1):
        for j in range(0,10,1):
            if(matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j]
            and matrice[i][j]==matrice[i+2][j-1] and matrice[i][j]==matrice[i+2][j+1]):
                matrice[i][j]='*'
                matrice[i+1][j] = '*'
                matrice[i+2][j] = '*'
                matrice[i+2][j-1] = '*'
                matrice[i+2][j+1] = '*'
                return 1
# X T X
# X T X
# T T T
def sterge_T_poz4(matrice):
    for i in range(0,9,1):
        for j in range(0,10,1):
            if(matrice[i][j]=='*'):
                for k in range(i,2,-1):
                    matrice[k+2][j]=matrice[k-1][j]
                for k in range(i+2, -1, -1):
                    matrice[k][j-1]=matrice[k-1][j-1]
                    matrice[k][j + 1] = matrice[k - 1][j + 1]
                matrice[0][j]=random.choice(culori)
                matrice[1][j] = random.choice(culori)
                matrice[2][j] = random.choice(culori)
                matrice[0][j-1] = random.choice(culori)
                matrice[0][j+1] = random.choice(culori)
                return 1

afisare(matrice)
ok=1
while(ok==1):
    x1=cautare_plus(matrice)
    ok=0
    if(x1==1):
        ok=1
        eliminare_plus(matrice)
        print()
        afisare(matrice)
    x2=cautare_T_poz1(matrice)
    if(x2==1):
        ok=1
        sterge_T_poz1(matrice)
        print()
        afisare(matrice)
    x3 = cautare_T_poz2(matrice)
    if (x3 == 1):
        ok = 1
        sterge_T_poz2(matrice)
        print()
        afisare(matrice)
    x4 = cautare_T_poz2(matrice)
    if (x4 == 1):
        ok = 1
        sterge_T_poz2(matrice)
        print()
        afisare(matrice)
    x5 = cautare_T_poz3(matrice)
    if (x5 == 1):
        ok = 1
        sterge_T_poz1(matrice)
        print()
        afisare(matrice)
    x6 = cautare_T_poz4(matrice)
    if (x2 == 1):
        ok = 1
        sterge_T_poz4(matrice)
        print()
        afisare(matrice)