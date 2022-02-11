import pygame
import time
import tkinter
from tkinter import *
from tkinter import messagebox
import math
import _thread
import random

black=(100,100,100)
white=(255,255,255)
green=(0,155,0)
pingreen=(100,200,100)
yellow=(155,155,0)
purple=(155,0,155)


pygame.init()
pygame.display.set_caption('graph')
screen = pygame.display.set_mode((500,500))
def clears():
    screen.fill((white))
    pygame.draw.rect(screen, (black), (249, 0, 2, 500), 0)
    pygame.draw.rect(screen, (black), (0, 249, 500, 2), 0)
    #pygame.display.update()
clears()
pygame.display.update()


root = tkinter.Tk()
root.title("function grapher")
e1=Text(root,height=5,width=24,font=("Consolas",12,'bold'),relief=FLAT,highlightthickness=2, highlightcolor='darkgray', highlightbackground='silver')
e1.pack(fill=BOTH,expand=Y)



funclist=[]
colist=[]
ran=random.randint(0,5)
tzb="0123456789abcdef"


def to16(c):
    ans="#"+tzb[int(c[0]/16)]+tzb[c[0]%16]+tzb[int(c[1]/16)]+tzb[c[1]%16]+tzb[int(c[2]/16)]+tzb[c[2]%16]
    return ans
def drawall(wait):
    global consa
    for i in range(0, len(funclist)):
        if len(colist)<=i:
            r=150
            g=random.randint(0,150)
            b=0
            choo=(i+ran)%6
            e1.tag_add(str(i),float(i+1),float(i+1)+0.99999)
            if choo==0:
                colist.append((r,g,b))
            elif choo==4:
                colist.append((r,b,g))
            elif choo==2:
                colist.append((g,b,r))
            elif choo==3:
                colist.append((g,r,b))
            elif choo==1:
                colist.append((b,r,g))
            elif choo==5:
                colist.append((b,g,r))
        if funclist[i]=='':
            continue
        color=colist[i]
        e1.tag_delete(str(i))
        e1.tag_add(str(i),float(i+1),float(i+1)+0.99999)
        e1.tag_config(str(i),foreground = to16(colist[i]))
        draw(funclist[i],consa,wait,color)
def zoom(zm):
    global zoomx,zoomy
    zm = int(zm)
    zm*=2
    zoomx = zm/500
    zoomy = 500/zm
    clears()
    drawall(0)
    pygame.display.update()


def changea(a):
    global consa
    consa=float(a)
    clears()
    drawall(0)
    pygame.display.update()

consa=0
zoom(10)
#print(zoomx,zoomy)

def adddt(l,r,vl,vr,func,a,gap,dtmin,color):
    global zoomx,zoomy
    if abs(vr-vl)<=gap or r-l<dtmin:
        return
    m=(l+r)/2
    x=zoomx*(m-251)
    #print(func,x,l,m,r,vl,vr)
    try:
        y=eval(func)
        if abs(y)>100000:
            return
        ym=int(250-zoomy*y)
    except:
        ym=250
    #if ym>vl and ym>vr and ym>500 or ym<vl and ym<vr and ym<0:
     #   return
    if ym>=0 and ym<=500:
        pygame.draw.circle(screen, (color), (int(m), ym), 1)
    #print(l,m,r,vl,vr)
    adddt(l,m,vl,ym,func,a,gap,dtmin,color)
    adddt(m,r,ym,vr,func,a,gap,dtmin,color)

def draw(func,a,wait,color):
    lst=0
    if wait:
        gap=1
        dtmin=0.00001
    else:
        gap=2
        dtmin=0.1
    #print(eval(func))
    for i in range(-250, 250):
        x = zoomx*i
        try:
            y = eval(func)  # 解析式
            '''
            if abs(y)>=100000:
                pygame.draw.circle(screen, (255,0,0), (400, 400), 20)
                return
            '''
            trxx = int(i+250)
            tryy = int(250-zoomy*y)
        except:
            adddt(i+250,i+251,lst,0,func,a,gap,dtmin,color)
            lst=0
            continue
        if tryy<=500 and tryy>=0:
            pygame.draw.circle(screen, (color), (trxx, tryy), 1)
            if wait:
                pygame.display.update()
                time.sleep(0.002)

        vl=lst
        vr=tryy
        #print(i,i+1,his[i],his[i+1])
        if vl>500 and vr>500 or vl<0 and vr<0:
            continue
        adddt(i+250,i+251,vl,vr,func,a,gap,dtmin,color)
        lst=tryy

    if wait:
        pygame.display.update()
    #print(his)

def GO():
    global funclist
    funclist = (e1.get("0.0","end").replace(" ","")).split("\n")
    clears()
    drawall(1)




def AF(x):
    global auto
    auto=1
    while auto==1:
        global funclist
        funclistt = (e1.get("0.0","end").replace(" ","")).split("\n")
        if funclist!=funclistt:
            funclist=funclistt
            clears()
            drawall(0)
            pygame.display.update()
        time.sleep(1)
    #print("exit")
def toAF(x):
    #print("start")
    _thread.start_new_thread( AF, (1,) )
def cutAF(x):
    global auto
    auto=0



e1.bind('<FocusIn>',toAF)
e1.bind('<FocusOut>',cutAF)

bi=Button(root,text="calibrate",command=GO,relief=FLAT,bg="silver")
bi.pack(fill=X)
s1 = Scale( root,from_ = 1, to = 50,orient="horizontal",command=zoom,label="zoom")
s1.set(10)
s1.pack(fill=X)
s2 = Scale(root, from_=-20, to=20,resolution=0.1, orient="horizontal", command=changea,label="value of a")
s2.set(0)
s2.pack(fill=X)

root.mainloop()


#(a*x-1)/(a*x**2+4*a*x+a)
#math.sin(a/x)
#pyinstaller -F grapher1.0.py -w -i C:\Users\jcliu\Desktop\vscode\383136_function_icon.ico


