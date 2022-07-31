import pygame
from pygame.locals import *
import time
import tkinter
from tkinter import *
import math
import _thread
import random

black=(100,100,100)
white=(255,255,255)
green=(0,155,0)
pingreen=(100,200,100)
yellow=(155,155,0)
purple=(155,0,155)



funclist=[]
colist=[]
ran=random.randint(0,5)
tzb="0123456789abcdef"
viewpozx=0
viewpozxx=0
viewpozy=0
viewpozxx=0

winsize=500
pygame.init()
pygame.display.set_caption('graph')
screen = pygame.display.set_mode((winsize,winsize),0,32)
def clears():
    global viewpozx,viewpozy,winsize
    screen.fill((white))
    pygame.draw.rect(screen, (black), (winsize/2-1+viewpozx, 0, 2, winsize), 0)
    pygame.draw.rect(screen, (black), (0, winsize/2-1+viewpozy, winsize, 2), 0)
    #pygame.display.update()
clears()
pygame.display.update()


root = tkinter.Tk()
root.title("function grapher")
e1=Text(root,height=5,width=24,font=("Consolas",12,'bold'),relief=FLAT)
e1.pack(fill=BOTH,expand=Y)




def to16(c):
    ans="#"+tzb[int(c[0]/16)]+tzb[c[0]%16]+tzb[int(c[1]/16)]+tzb[c[1]%16]+tzb[int(c[2]/16)]+tzb[c[2]%16]
    return ans
def drawall(wait,in3d):
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
        if in3d:
            draw3D(funclist[i],consa,color)
        else:
            draw(funclist[i],consa,wait,color)
def zoom(zm):
    global zoomx,zoomy
    zm = int(zm)
    zm*=2
    zoomx = zm/winsize
    zoomy = winsize/zm
    clears()
    drawall(0,0)
    pygame.display.update()


def changea(a):
    global consa
    consa=float(a)
    clears()
    drawall(0,0)
    pygame.display.update()

consa=0
zoom(10)
#print(zoomx,zoomy)

def adddt(l,r,vl,vr,func,a,gap,dtmin,color):
    global zoomx,zoomy
    if abs(vr-vl)<=gap or r-l<dtmin:
        return
    m=(l+r)/2
    x=zoomx*(m-int(winsize/2+1))
    #print(func,x,l,m,r,vl,vr)
    try:
        y=eval(func)
        if abs(y)>100000:
            return
        ym=int(int(winsize/2)-zoomy*y+viewpozy)
    except:
        ym=int(winsize/2)
    if ym>=0 and ym<=winsize:
        pygame.draw.circle(screen, (color), (int(m)+viewpozx, ym), 1)
    #print(l,m,r,vl,vr)
    adddt(l,m,vl,ym,func,a,gap,dtmin,color)
    adddt(m,r,ym,vr,func,a,gap,dtmin,color)

def draw(func,a,wait,color):
    global viewpozx,viewpozy

    lst=0
    if wait:
        gap=1
        dtmin=0.00001
    else:
        gap=2
        dtmin=0.1
    #print(eval(func))
    for i in range(-int(winsize/2), int(winsize/2)):
        x = zoomx*(i-viewpozx)
        try:
            y = eval(func)
            trxx = int(i+int(winsize/2))
            tryy = int(int(winsize/2)-zoomy*y)+viewpozy
        except:
            adddt(i+int(winsize/2)-viewpozx,i+int(winsize/2+1)-viewpozx,lst,0,func,a,gap,dtmin,color)
            lst=0
            continue
        if tryy<=winsize and tryy>=0:
            pygame.draw.circle(screen, (color), (trxx, tryy), 1)
            if wait:
                pygame.display.update()
                time.sleep(0.002)

        vl=lst
        vr=tryy
        #print(i,i+1,his[i],his[i+1])
        if vl>winsize and vr>winsize or vl<0 and vr<0:
            continue
        adddt(i+int(winsize/2)-viewpozx,i+int(winsize/2+1)-viewpozx,vl,vr,func,a,gap,dtmin,color)
        lst=tryy

    if wait:
        pygame.display.update()
    #print(his)

def draw3D(func,a,color):
    global viewpozx,viewpozy
    draw("x",0,0,(black))

    func=func+"+z*0.35355339"

    for j in range(-50,50):
        z=zoomx*(j*10-viewpozx)*2.828427124746
        #print(((func.replace("x","(x-z*0.35355339)")).replace("z",str(z))),a,color,z)
        draw(((func.replace("x","(x-z*0.35355339)")).replace("z",str(z))),a,0,color)
    for j in range(-50,50):
        z=zoomx*(j*10-viewpozx)
        #print((func.replace("x",str(z))).replace("z","((x-"+str(z)+")*2.828427124746)"),a,color,z)
        draw((func.replace("x",str(z))).replace("z","((x-"+str(z)+")*2.828427124746)"),a,0,color)
    
    pygame.display.update()

def GO():
    global funclist
    funclistt = ((e1.get("0.0","end").replace(" ","")).replace("_","math.")).split("\n")
    clears()
    drawall(1,0)




def AF(x):
    global auto
    auto=1
    while auto==1:
        global funclist,viewpozyy,viewpozxx
        funclistt = ((e1.get("0.0","end").replace(" ","")).replace("_","math.")).split("\n")
        if funclist!=funclistt or viewpozx!=viewpozxx or viewpozy!=viewpozyy:
            funclist=funclistt
            viewpozyy=viewpozy
            viewpozxx=viewpozx
            clears()
            drawall(0,0)
            pygame.display.update()
        time.sleep(0.1)
    #print("exit")
def toAF(x):
    #print("start")
    _thread.start_new_thread( AF, (1,) )
def cutAF(x):
    global auto
    auto=0


toAF(1)
#$e1.bind('<FocusIn>',toAF)
#$e1.bind('<FocusOut>',cutAF)

def resize():
    global winsize
    winsize=int(e2.get())
    screen = pygame.display.set_mode((winsize,winsize),0,32)
    clears()
    drawall(0,0)
    pygame.display.update()


bi=Button(root,text="Calibrate",command=GO,relief=FLAT,bg="silver")
bi.pack(fill=X)
b3d=Button(root,text="3D(beta)",command=lambda:drawall(0,1),relief=FLAT,bg="silver")
b3d.pack(fill=X)
s1 = Scale( root,from_ = 1, to = 50,orient="horizontal",command=zoom,label="zoom")
s1.set(10)
s1.pack(fill=X)
s2 = Scale(root, from_=-20, to=20,resolution=0.1, orient="horizontal", command=changea,label="value of a")
s2.set(0)
s2.pack(fill=X)
l1=Label(root,text="Size:",width=10)
l1.pack(side='left',fill=X)
e2=Entry(root,width=4)
e2.pack(side='left')
e2.insert(0,winsize)
bi=Button(root,text="resize",command=resize,relief=FLAT,bg="white")
bi.pack(side='right')

running=1
def pygamepro(x):
    global running,viewpozx,viewpozy,zoomx,zoomy
    print(1)
    hold=0
    while running:
        time.sleep(0.1)
        for event in pygame.event.get():
                if event.type == QUIT:
                    print(1)
                    root.destroy()
                    exit()
                m=pygame.mouse.get_pressed()
                #print(m[0])
                if m[0]==1:
                    print(hold)
                    mx,my=pygame.mouse.get_pos()
                    if hold==1:
                        viewpozy+=my-lastpoy
                        viewpozx+=mx-lastpox
                        print(viewpozx,viewpozy)
                        
                    hold=1
                    lastpox=mx
                    lastpoy=my
                elif m[1]==1:
                    mx,my=pygame.mouse.get_pos()
                    print( hold)
                    if hold==2:
                        zm=zoomx*winsize/2
                        zm-=int((my-lastpoy)/2)
                        if(zm<=0):
                            zm=1
                        s1.set(zm)
                        zoom(zm)
                        print(zm)
                        
                    hold=2
                    lastpox=mx
                    lastpoy=my
                else:
                    hold=0              
                

_thread.start_new_thread( pygamepro, (1,) )
def on_closing():
    global running
    running=0
    time.sleep(0.1)
    root.destroy()
    exit()
root.protocol('WM_DELETE_WINDOW', on_closing)
root.mainloop()


#(a*x-1)/(a*x**2+4*a*x+a)
#math.sin(a/x)

#pyinstaller -F grapher xx.py -w -i C:\Users\...