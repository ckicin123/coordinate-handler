from pynput.mouse import Button,Controller
import time
import math
import random
mouse=Controller()
addaxis=True
plotsize=10
global angle
angle=0
runtime=5
def plotpoint(x,ps):
    mouse.position=x
    mouse.position=(x[0]+ps,x[1]-ps)
    mouse.press(Button.left)
    mouse.position=(x[0]-ps,x[1]+ps)
    mouse.release(Button.left)
    mouse.position=(x[0]-ps,x[1]-ps)
    mouse.press(Button.left)
    mouse.position=(x[0]+ps,x[1]+ps)
    mouse.release(Button.left)
    mouse.position=x
def processinstruction(orderofop):
    global angle
    for i in orderofop:
        if i[0]=="plot":
            plotpoint((i[1][0]+650,500-i[1][1]),plotsize)
        if i[0]=="drawrandom":
            mouse.press(Button.left)
            mouse.position=((random.randint(-300,300)+650),(500-random.randint(-200,200)))
            mouse.release(Button.left)
            print("trur")
        elif i[0]=="moveto":
            mouse.position=(i[1][0]+650,500-i[1][1])
        elif i[0]=="setangle":
            angle=i[1]
            while angle>360:
                angle-=360
        elif i[0]=="addangle":
            angle+=i[1]
            while angle>360:
                angle-=360
        elif i[0]=="drawto":
            mouse.press(Button.left)
            mouse.position=(i[1][0]+650,500-i[1][1])
            mouse.release(Button.left)
        elif i[0]=="iterate":
            for purple in range(i[1]):
                processinstruction(i[2])
        elif i[0]=="drawforward":
            mouse.press(Button.left)
            if angle%90!=0:
                gradient=math.tan(math.radians(90+angle))
                x=((i[1]**2)/(1+(gradient**2)))**(1/2)
                y=(i[1]**2-x**2)**(1/2)
                anglecopy=angle
                pon=["-","-"] #y,x
                inc=0
                while anglecopy>90:
                    anglecopy-=90
                    if pon[inc]=="+":
                        pon[inc]="-"
                    else:
                        pon[inc]="+"
                    if inc==0:
                        inc=1
                    else:
                        inc=0
                if pon[0]=="+":
                    ycoor=mouse.position[1]+y
                else:
                    ycoor=mouse.position[1]-y
                if pon[1]=="+":
                    xcoor=mouse.position[0]+x
                else:
                    xcoor=mouse.position[0]-x
                mouse.position=(xcoor,ycoor)
                mouse.release(Button.left)
            else:
                inct=angle/90
                if inct%2==1:
                    if inct==1:
                        mouse.position=(mouse.position[0]-i[1],mouse.position[1])
                    else:
                        mouse.position=(mouse.position[0]+i[1],mouse.position[1])
                else:
                    if inct==0 or inct==4:
                        mouse.position=(mouse.position[0],mouse.position[1]-i[1])
                    else:
                        mouse.position=(mouse.position[0],mouse.position[1]+i[1])
            mouse.release(Button.left)
time.sleep(2)
if addaxis:
    mouse.position=(250,500)
    mouse.press(Button.left)
    mouse.position=(1500,500)
    mouse.release(Button.left)
    mouse.position=(500,500)
    mouse.press(Button.left)
    mouse.position=(100,500)
    mouse.release(Button.left)
    mouse.position=(650,300)
    mouse.press(Button.left)
    mouse.position=(650,700)
    mouse.release(Button.left) 



for cata in range(1,361,5):
    #orderofop=[["moveto",[cata-400,0]],["setangle",cata/2],["iterate",cata%25,[["addangle",cata/5],["drawforward",20]]]]
    #orderofop=[["moveto",[180,50]],["setangle",cata],["iterate",6,[["addangle",cata/6],["drawforward",cata/5]]]]
    orderofop=[["moveto",[100,50]],["iterate",5,[["drawforward",30],["addangle",cata/5]]]]
    #orderofop=[["moveto",[180,50]],["setangle",cata**3],["iterate",5,[["addangle",72],["drawforward",cata/3]]]]
    #orderofop=[["moveto",[0,0]],["drawrandom"]]
    processinstruction(orderofop)
    time.sleep(0.1)
