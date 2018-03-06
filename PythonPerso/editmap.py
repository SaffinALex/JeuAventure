#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from random import *

def placer(nom,x,y,canvas):
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range (0,16):
            if ligne[i]=="1":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0a650a",outline="") #vert
            elif ligne[i]=="2":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="") #noir
            elif ligne[i]=="3":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="") #bleu
            elif ligne[i]=="4":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#808180",outline="") #gris
            elif ligne[i]=="5":
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#614919",outline="") #marron
            elif ligne[i]=="6":
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="") #rouge 
            elif ligne[i]=="7":
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#d4a566",outline="") #beige
            elif ligne[i]=="8":
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0dac07",outline="") #vertClaire
            elif ligne[i]=="9":
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="white",outline="") #Blanc
            elif ligne[i]=="A":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#6d5331",outline="") #MarronClaire
            elif ligne[i]=="B":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#383837",outline="") #NOIRCLAIRE(OMBRE)
            elif ligne[i]=="C":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#e3e570",outline="") #JAUNECLAIRE


                
            val_x+=2
        val_y+=2
        val_x=x
    fichier.close()

def bougerCurseur1():
    global curseur1
    global selection
    curseur1[2]+=curseur1[0]
    curseur1[3]+=curseur1[1]
    if len(curseur1[4])>0:
        canvass.delete(curseur1[4][0])
        del curseur1[4][0]
    curseur1[4].append(canvass.create_rectangle(curseur1[2],curseur1[3],curseur1[2]+32,curseur1[3]+32,fill=''))

    
def bougerCurseur2():
    global curseur2
    global selection
    curseur2[2]+=curseur2[0]
    curseur2[3]+=curseur2[1]
    if len(curseur2[4])>0 :
        canvas.delete(curseur2[4][0])
        del curseur2[4][0]
    curseur2[4].append(canvas.create_rectangle(curseur2[2],curseur2[3],curseur2[2]+32,curseur2[3]+32,fill=''))

    selection=(curseur2[2]/32)+(curseur2[3]*10)



def frame():

    bougerCurseur1()
    bougerCurseur2()

    canvas.after(100,frame)

def vitesse(event):

    touche=event.keysym
    
    if touche=="Up":
        curseur1[1]=-32
    if touche=="Down":
        curseur1[1]=32          
    if touche=="Right":
        curseur1[0]=32
    if touche=="Left":
        curseur1[0]=-32
        
    if touche=="z":
        curseur2[1]=-32
    if touche=="s":
        curseur2[1]=32         
    if touche=="d":
        curseur2[0]=32
    if touche=="q":
        curseur2[0]=-32
        
    if touche=="Return":
        nom="./spriteDecor/bloc"+Bloc[selection]
        canvas.delete
        placer(nom,curseur1[2],curseur1[3],canvass)
        
   

def stop(event):
    
    touche=event.keysym
    if(touche=="Up" or touche=="Down"):
        curseur1[1]=0

    if(touche=="Right" or touche=="Left"):
        curseur1[0]=0
        
    if(touche=="z" or touche=="s"):
        curseur2[1]=0

    if(touche=="d" or touche=="q"):
        curseur2[0]=0


        
fenetre = Tk()
canvass = Canvas(fenetre, width=640, height=640, background="#219a21")
canvas = Canvas(fenetre, width=640, height=300)
curseur1=[0,0,0,0,[]]
curseur2=[0,0,0,0,[]]
posx=0
posy=0
selection=0
Finit=True
Bloc="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
canvas.pack()
canvas.focus_set()
canvass.pack()
canvass.focus_set()

for i in range(0,len(Bloc)):
    nom="./spriteDecor/bloc"+Bloc[i]
    placer(nom,posx,posy,canvas)
    
    if(posx>=608):
        posx=0
        posy+=32
    else:
        posx+=32


frame()


    
canvass.bind("<Key>", vitesse)
canvass.bind("<KeyRelease>", stop)
        
fenetre.mainloop()
    
