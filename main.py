# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from numpy import *
from math import *
from sympy import *
A, B, C, D, E, F, G, H, r, n, b, q, k, p, t, P, R, N, B, Q, K = symbols ('A, B, C, D, E, F, G, H, r, n, b, q, k, p, ., P, R, N, B, Q, K')
pole = [[ ' ', A, B, C, D, E, F, G, H, ''],   [8, r, n, b, q, k, b, n, r, 8], [7, p, p, p, p, p, p, p, p, 7], [6, t, t, t, t, t, t, t, t, 6], [5, t, t, t, t, t, t, t, t, 5],[4, t, t, t, t, t, t, t, t, 4],[3, t, t, t, t, t, t, t, t, 3], [2, P, P, P, P, P, P, P, P, 2], [1, R, N, B, Q, K, B, N, R, 1],[ ' ', A, B, C, D, E, F, G, H, '']]
letters="abcdefgh"

def board():
    for i in pole:
        print(*i)

def borw(piece):
    piece=str(piece)
    b = "rnbqkp"
    w = "RNBQKP"
    print(piece)
    if piece in w: return 1
    elif piece in b: return -1
    else: return 0

def wtpiece(pole,id1,id2,ch1,ch2):
    piece1=str(pole[ch1][id1])
    piece2=str(pole[ch2][id2])
    if piece1=="r" or piece1 == "R":
        return rook(id1,id2,ch1,ch2)
    elif piece1=="n" or piece1 == "N":
        return knight(id1,id2,ch1,ch2)
    elif piece1=="b" or piece1 == "B":
        return bishop(id1,id2,ch1,ch2)
    elif piece1=="q" or piece1 == "Q":
        return queen(id1,id2,ch1,ch2)
    elif piece1=="k" or piece1 == "K":
        return king(id1,id2,ch1,ch2)
    else:
        return pawn(piece1,piece2,id1,id2,ch1,ch2)

def rook(id1,id2,ch1,ch2):
    if (id1==id2 or ch1==ch2):
        return 1
    else:
        print("Невозможный ход для фигуры")
        return 0

def bishop(id1,id2,ch1,ch2):
    if abs(id1-id2)==abs(ch1-ch2):
        return 1
    else:
        print("Невозможный ход для фигуры")
        return 0

def queen(id1,id2,ch1,ch2):
    if abs(id1-id2)==abs(ch1-ch2) or (id1==id2 or ch1==ch2):
        return 1
    else:
        print("Невозможный ход для фигуры")
        return 0

def king(id1,id2,ch1,ch2):
    if abs(id1-id2)==1 and ch1==ch2 or abs(ch1-ch2)==1 and id1==id2 or abs(id1-id2)==1 and abs(ch1-ch2)==1:
        return 1
    else:
        print("Невозможный ход для фигуры")
        return 0

def pawn(piece1,piece2,id1,id2,ch1,ch2):
    if id1==id2\
    and ((ch1==2 or ch1==7) and abs(ch1-ch2)==2\
         or (piece2=="." and ((piece1=="p" and ch2-ch1==1) or (piece1=="P" and ch1-ch2==1 ))))\
                     or (piece1=="p" and ch2<ch1 and abs(id1-id2)==1 and abs(ch1-ch2)==1 and piece2!="." ) \
                            or (piece1=="P" and ch2>ch1 and abs(id1-id2)==1 and abs(ch1-ch2)==1 and piece2!="." ) :
        return 1
    else:
        print("Невозможный ход для фигуры")
        return 0

def knight(id1,id2,ch1,ch2):
    if abs(ch1-ch2)==2 and abs(id1-id2)==1 or abs(id1-id2)==2 and abs(ch1-ch2)==1:
        return 1
    else:
        print("Невозможный ход для фигуры")
        return 0

key=0
st=1
f1=f2=0
p=1
zv=0
zp=0
hody=[]
nummove=1
while key==0:
    if nummove%2!=0 :
        p=1
        print("Ход белых")
    else:
        p=2
        print("Ход чёрных")
    if nummove!=1:
        print("Номер хода:", math.ceil(nummove/2))
    else: print("Номер хода:", nummove)
    strok=input()
    if strok == "Завершить чтение" and zv!=1:
        zv=1
        f1.close()
        strok=input()
        st=-st
    if strok == "Завершить запись" and zp==1 or strok=="Завершить" and zp==1:
        #print(hody)
        zp=0
        for i in hody:
            f2.write(letters[i[0]]+str(pole[i[1]][0])+"-"+letters[i[2]]+str(pole[i[3]][0])+"\n")
        f2.close()
        strok=input()
    if strok=="Завершить": break
    if "Партия:" in strok and nummove==1:
        f1=open(strok[7::],"r")
        file=f1.readlines()
        continue
    if "Блокнот:" in strok:
        f2=open(strok[8::],"w")
        zp=1
        continue
    if f1==0: zv=1
    if strok=="Ход назад":
        if len(hody)==0:
            print("Невозможен возврат")
        else:
            pole[hody[-1][0]][hody[-1][1]]=pole[hody[-1][2]][hody[-1][3]]
            pole[hody[-1][2]][hody[-1][3]]=hody[-1][4]
            hody.pop()
            for i in pole:
                print(*i)
        nummove-=1
    else:
        if zv==0:
            if strok=="Ход вперед":
                move=list(file[nummove-1][:-1].split("-"))
        else:
            move=list(strok.split("-"))
        print(move)
        ch1=abs(8-int(move[0][1]))+1
        ch2=abs(8-int(move[1][1]))+1
        id1=letters.find(move[0][0])+1
        id2=letters.find(move[1][0])+1
        piece1= pole[ch1][id1]
        piece2= pole[ch2][id2]
        if move[0]!=move[1] and borw(piece1) == st and borw(piece2)!=st \
    and wtpiece(pole,id1,id2,ch1,ch2)==1 and (piece2!="K" or piece2!="k"):
            hody.append([ch1,id1,ch2,id2, piece2])
            if borw(piece2)==-st:
                pole[ch1][id1]=t
                pole[ch2][id2]=piece1
            else:
                pole[ch1][id1]=pole[ch2][id2]
                pole[ch2][id2]=piece1
            for i in pole:
                print(*i)
            st=-st
            nummove+=1
            print(hody)
        else:
            print("Ошибка")
            break