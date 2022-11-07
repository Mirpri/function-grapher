import pygame
from pygame.locals import *
import time
import tkinter
from tkinter import *
from tkinter.ttk import *
import math
import _thread
import random
import base64
import os

black=(100,100,100)
white=(255,255,255)
#green=(0,155,0)
#pingreen=(100,200,100)
#yellow=(155,155,0)
#purple=(155,0,155)

img = b'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'

root = tkinter.Tk()
root.title("function grapher")
winsize=500
pygame.init()
pygame.display.set_caption('graph')
screen = pygame.display.set_mode((winsize,winsize))

tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("tmp.ico")
os.remove("tmp.ico")

funclist=[]
colist=[]
ran=random.randint(0,5)
tzb="0123456789abcdef"
viewpozx=0
viewpozxx=0
viewpozy=0
viewpozxx=0


def clears():
    global viewpozx,viewpozy,winsize
    screen.fill((white))
    pygame.draw.rect(screen, (black), (winsize/2-1+viewpozx, 0, 2, winsize), 0)
    pygame.draw.rect(screen, (black), (0, winsize/2-1+viewpozy, winsize, 2), 0)
    #pygame.display.update()
clears()
pygame.display.update()


fentry=Frame(root)
e1=Text(fentry,height=5,width=24,font=("Consolas",12,'bold'),bd=0)
e1.pack(side='left',fill=BOTH,expand=Y)
s = Scrollbar(fentry, orient=VERTICAL, command=e1.yview)
s.pack(fill=Y,expand=Y)
fentry.pack(expand=Y,fill=BOTH,side='left')
e1['yscrollcommand'] = s.set



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
    zm = int(float(zm))
    zm*=2
    zoomx = zm/winsize
    zoomy = winsize/zm
    clears()
    drawall(0,0)
    pygame.display.update()


def changea(a):
    global consa
    consa=round(float(a),3)
    clears()
    drawall(0,0)
    pygame.display.update()
    la.config(text="a="+str(consa))

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
        if ym>=0 and ym<=winsize:
            pygame.draw.circle(screen, (color), (int(m)+viewpozx, ym), 1)
    except:
        ym=int(winsize/2+viewpozy)
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

fwids=Frame(root)
bi=Button(fwids,text="Calibrate",command=GO)
bi.pack(fill=X)
b3d=Button(fwids,text="3D(beta)",command=lambda:drawall(0,1))
b3d.pack(fill=X)

fscale1=Frame(fwids)
Label(fscale1,text="zoom ").pack(side='left',fill=X)
s1 = Scale( fscale1,from_ = 1, to = 50,orient="horizontal",command=zoom)
s1.set(10)
s1.pack(fill=X,pady=3)
fscale1.pack(fill=X)

fscale2=Frame(fwids)
la=Label(fscale2,text="a=0.000",width=8)
la.pack(side='left',fill=X)
s2 = Scale(fscale2, from_=-10, to=10, orient="horizontal", command=changea)
s2.set(0)
s2.pack(fill=X,pady=3)
fscale2.pack(fill=X)

fsize=Frame(fwids)
Label(fsize,text="Size:").pack(side='left',fill=X)
e2=Spinbox(fsize,width=6,from_=100,to=1000)
e2.pack(side='left')
e2.insert(0,winsize)
bi=Button(fsize,text="resize",command=resize)
bi.pack(side='right')
fsize.pack()
fwids.pack(fill=BOTH,padx=10,pady=10)

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
                else:
                    hold=0
                if event.type==MOUSEBUTTONUP:
                    if event.button==4:
                        zm=zoomx*500/2
                        zm+=1
                        s1.set(zm)
                        zoom(zm)
                        print(zm)
                    elif event.button==5:
                        zm=zoomx*500/2
                        zm-=1
                        if(zm<=0):
                            zm=1
                        s1.set(zm)
                        zoom(zm)
                        print(zm)
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