import random
import os
from threading import Thread
from time import sleep
from msvcrt import getch
arr=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
a=random.randint(5,35)
b=random.randint(5,15)
snakeArr=[[a,b],[a+1,b],[a+2,b]]
Where="L"
T=0.16
for i in range(0,3):
    arr[snakeArr[i][1]][snakeArr[i][0]]=1
flage=False
count=0
def InputMD():
    global T
    a=input("请选择难度：(1:简单 2:困难 3:地狱")
    if a=='1':
        T=0.5
    elif a=='2':
        T=0.25
    elif a=='3':
        T==0.16
    else:
        InputMD()
def PlaySnake():
    global Where
    while True:
        a=getch()
        if a==b'a' or a==b'A':
            if Where!='R':
                Where='L'
        elif a==b'd' or a==b'D':
            if Where!='L':
                Where='R'
        elif a==b'w' or a==b'W':
            if Where!='D':
                Where='U'
        elif a==b's' or a==b'S':
            if Where!='U':
                Where='D'
def GetSnakeIndex():
    global arr,count,flage
    if arr[snakeArr[0][1]][snakeArr[0][0]]==2:
        arr[snakeArr[0][1]][snakeArr[0][0]]=1
        count+=1
        flage=False
    elif arr[snakeArr[0][1]][snakeArr[0][0]]==0:
        DelTile()
        snakeArr.pop(snakeArr.__len__()-1)
        arr[snakeArr[0][1]][snakeArr[0][0]]=1
    else:
        Die()
def DelTile():
    global snakeArr,arr
    arr[snakeArr[snakeArr.__len__()-1][1]][snakeArr[snakeArr.__len__()-1][0]]=0

def MoveLeft():
    global snakeArr
    if snakeArr[0][0]-1 !=-1:
        snakeArr.insert(0,[snakeArr[0][0]-1,snakeArr[0][1]])
        GetSnakeIndex()
        PMap()
    else:
        Die()
    sleep(T)
    MoveSnake()

def MoveUp():
    if snakeArr[0][1]-1 !=-1:
        snakeArr.insert(0,[snakeArr[0][0],snakeArr[0][1]-1])
        GetSnakeIndex()
        PMap()
    else:
        Die()
    sleep(T)
    MoveSnake()

def MoveRight():
    if snakeArr[0][0]+1 !=40:
        snakeArr.insert(0,[snakeArr[0][0]+1,snakeArr[0][1]])
        GetSnakeIndex()
        PMap()
    else:
        Die()
    sleep(T)
    MoveSnake()

def MoveDown():
    if snakeArr[0][1]+1 !=20:
        snakeArr.insert(0,[snakeArr[0][0],snakeArr[0][1]+1])
        GetSnakeIndex()
        PMap()
    else:
        Die()
    sleep(T)
    MoveSnake()

def MoveSnake():
    if Where=='L':
        MoveLeft() 
    elif Where=='U':
        MoveUp() 
    elif Where=='R':
        MoveRight()
    elif Where=='D':
        MoveDown()()    
def PMap():
    os.system("cls")
    print("000000000000000000000000000000000000000000")
    for i in range(0,20):
        print('0',end='')
        for j in range(0,40):
            if arr[i][j]==0:
                print(" ",end='')
            elif arr[i][j]==1:
                print("#",end='')
            elif arr[i][j]==2:
                print("*",end='')
        print('0')
    print("000000000000000000000000000000000000000000\n"+"              "+str(count))
def Foud():
    global arr,flage
    while True:
        if flage==False:
            a=random.randint(0,39)
            b=random.randint(0,19)
            if arr[b][a]!=1:
                arr[b][a]=2
                flage=True
        sleep(T)
def Die():
    os.system("cls")
    print("得分："+str(count))
    os.system("pause")
    os._exit(1)
InputMD()
Thread(target=PlaySnake,args=()).start()
Thread(target=MoveSnake,args=()).start()
Thread(target=Foud,args=()).start()
