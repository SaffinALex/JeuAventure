#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from random import *

def placerBloc(nbr,x,y):
    val_x=x
    val_y=y
    nomBloc="bloc"+str(nbr)
    fichier = open(nomBloc,'r')
    lignes  = fichier.readlines()
    
    if not(nomBloc=="bloc0"):
        Bloque_x.append(x)
        Bloque_y.append(y)

        
    for ligne in lignes:
        for i in range (0,16):
            if ligne[i]=="1":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="green",outline="")
            elif ligne[i]=="2":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="")
            elif ligne[i]=="0":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#219a21",outline="")
            elif ligne[i]=="3":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="")
            elif ligne[i]=="4":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#808180",outline="")
            elif ligne[i]=="5":
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#614919",outline="")
            elif ligne[i]=="6":
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="")
                 
            val_x+=2

        val_y+=2
        val_x=x
        
def afficheTerrain():
    global mapx
    global mapy
    
    nom="map"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for ligne in lignes:
        for i in range (0,20):
            placerBloc(ligne[i],(i*32),j)

        j+=32
        
def ZeroBloque():
    global Bloque_x
    global Bloque_y
    
    while len(Bloque_x)>0:
        del Bloque_x[len(Bloque_x)-1]
        del Bloque_y[len(Bloque_y)-1]


def BloquerPerso(val_x, val_y):
    global Bloque_x
    global Bloque_y
    global MonPerso
    
    for i in range(0,len(Bloque_x)-1):
        
        if(MonPerso[2]>=Bloque_x[i] and MonPerso[2]<=Bloque_x[i]+31):
            if(MonPerso[3]>=Bloque_y[i] and MonPerso[3]<=Bloque_y[i]+31): #Coin Haut gauche
                MonPerso[3]=val_y
                MonPerso[2]=val_x
                
        if(MonPerso[2]+31>=Bloque_x[i] and MonPerso[2]+32<=Bloque_x[i]+31):
            if(MonPerso[3]+31>=Bloque_y[i] and MonPerso[3]+31<=Bloque_y[i]+31): #Coin Haut Droite
                MonPerso[3]=val_y
                MonPerso[2]=val_x

        if(MonPerso[2]+31>=Bloque_x[i] and MonPerso[2]+31<=Bloque_x[i]+31):
            if(MonPerso[3]>=Bloque_y[i] and MonPerso[3]<=Bloque_y[i]+31): #Coin Bas Droite
                MonPerso[3]=val_y
                MonPerso[2]=val_x

        if(MonPerso[2]>=Bloque_x[i] and MonPerso[2]<=Bloque_x[i]+31):
            if(MonPerso[3]+31>=Bloque_y[i] and MonPerso[3]+31<=Bloque_y[i]+31): #Coin Bas gauche
                MonPerso[3]=val_y
                MonPerso[2]=val_x

def BloquerEnnemi(val_x, val_y):
    global Bloque_x
    global Bloque_y
    global MonEnnemi
    global Deplacement
    
    for i in range(0,len(Bloque_x)-1):
        
        if(MonEnnemi[2]>=Bloque_x[i] and MonEnnemi[2]<=Bloque_x[i]+31):
            if(MonEnnemi[3]>=Bloque_y[i] and MonEnnemi[3]<=Bloque_y[i]+31): #Coin Haut gauche
                MonEnnemi[3]=val_y
                MonEnnemi[2]=val_x
                Deplacement=0
                
        if(MonEnnemi[2]+31>=Bloque_x[i] and MonEnnemi[2]+32<=Bloque_x[i]+31):
            if(MonEnnemi[3]+31>=Bloque_y[i] and MonEnnemi[3]+31<=Bloque_y[i]+31): #Coin Haut Droite
                MonEnnemi[3]=val_y
                MonEnnemi[2]=val_x
                Deplacement=0

        if(MonEnnemi[2]+31>=Bloque_x[i] and MonEnnemi[2]+31<=Bloque_x[i]+31):
            if(MonEnnemi[3]>=Bloque_y[i] and MonEnnemi[3]<=Bloque_y[i]+31): #Coin Bas Droite
                MonEnnemi[3]=val_y
                MonEnnemi[2]=val_x
                Deplacement=0

        if(MonEnnemi[2]>=Bloque_x[i] and MonEnnemi[2]<=Bloque_x[i]+31):
            if(MonEnnemi[3]+31>=Bloque_y[i] and MonEnnemi[3]+31<=Bloque_y[i]+31): #Coin Bas gauche
                MonEnnemi[3]=val_y
                MonEnnemi[2]=val_x
                Deplacement=0
           

def mouvement_perso():
    global x
    global y
    global MonPerso
    global MonEnnemi
    global Deplacement
    global Perso
    global Ennemi
    global mapx
    global mapy

    MonPerso[2]+=MonPerso[0]
    MonPerso[3]+=MonPerso[1]
    val_x=MonPerso[2]-MonPerso[0]
    val_y=MonPerso[3]-MonPerso[1]

    BloquerPerso(val_x,val_y)
    
    mouvePerso(MonPerso[2],MonPerso[3])
    
    if (MonPerso[2]+32>640):
        mapx+=1
        MonPerso[2]=0
        ZeroBloque()
        afficheTerrain()
        mouvePerso(MonPerso[2],MonPerso[3])
        
    elif(MonPerso[2]<0):
        mapx-=1
        MonPerso[2]=640-32
        ZeroBloque()
        afficheTerrain()
        mouvePerso(MonPerso[2],MonPerso[3])
        
    elif(MonPerso[3]<0):
        mapy+=1
        MonPerso[3]=640-32
        ZeroBloque()
        afficheTerrain()
        mouvePerso(MonPerso[2],MonPerso[3])
        
    elif(MonPerso[3]+32>640):
        mapy-=1
        MonPerso[3]=0
        ZeroBloque()
        afficheTerrain()
        mouvePerso(Perso,"Perso",MonPerso[2],MonPerso[3])
                
        

    if(Deplacement<=0):
        chiffre=randint(0,4)
        MonEnnemi[0]=0
        MonEnnemi[1]=0
        
        if(chiffre==0):
            MonEnnemi[0]+=4
        elif(chiffre==1):
            MonEnnemi[0]-=4
        elif(chiffre==2):
            MonEnnemi[1]+=4
        elif(chiffre==3):
            MonEnnemi[1]-=4
        Deplacement=10

    MonEnnemi[2]+=MonEnnemi[0]
    MonEnnemi[3]+=MonEnnemi[1]
    BloquerEnnemi(MonEnnemi[2]-MonEnnemi[0],MonEnnemi[3]-MonEnnemi[1])
    bouger_sprite(Ennemi,"ennemi1",MonEnnemi[2],MonEnnemi[3])

    Deplacement-=1

        


    
    canvas.after(50,mouvement_perso)

    
    

def bouger(event):
    global MonPerso

    touche=event.keysym
    
    if touche=="Up":
        MonPerso[1]=-8
    if touche=="Down":
        MonPerso[1]=8
    if touche=="Right":
        MonPerso[0]=8
    if touche=="Left":
        MonPerso[0]=-8

def stop(event):
    touche=event.keysym
    if(touche=="Up" or touche=="Down"):
        MonPerso[1]=0
    if(touche=="Right" or touche=="Left"):
        MonPerso[0]=0
        
def effaceEnnemi():
    global Ennemi
    while len(Ennemi)>0:
        canvas.delete(Ennemi[len(Ennemi)-1])
        del Ennemi[len(Ennemi)-1]

def effacePerso():
    global Perso
    while len(Perso)>0:
        canvas.delete(Perso[len(Perso)-1])
        del Perso[len(Perso)-1]

def efface(Perso):
    while len(Perso)>0:
        canvas.delete(Perso[len(Perso)-1])
        del Perso[len(Perso)-1]
    

def mouveEnnemi(nbr,x,y):
    global Ennemi
    effaceEnnemi()
    val_x=x
    val_y=y
    nomEnnemi="ennemi"+str(nbr)
    fichier = open(nomEnnemi,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range (0,17):
            if ligne[i]=="1":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="green",outline="")
                Ennemi.append(pos)
            elif ligne[i]=="2":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="")
                Ennemi.append(pos)
            elif ligne[i]=="3":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="")
                Ennemi.append(pos)
                
            val_x+=2


        val_y+=2
        val_x=x
        
def bouger_sprite(sprite_pos,nom,x,y):
    efface(sprite_pos)
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range (0,17):
            if ligne[i]=="1":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="green",outline="")
                sprite_pos.append(pos)
            elif ligne[i]=="2":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="")
                sprite_pos.append(pos)
            elif ligne[i]=="3":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="")
                sprite_pos.append(pos)
                
            val_x+=2


        val_y+=2
        val_x=x

def mouvePerso(x,y):
    global Perso
    effacePerso()
    val_x=x
    val_y=y
    fichier = open("Perso",'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range (0,17):
            if ligne[i]=="1":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="green",outline="")
                Perso.append(pos)
            elif ligne[i]=="2":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="")
                Perso.append(pos)
            elif ligne[i]=="3":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="")
                Perso.append(pos)
                
            val_x+=2


        val_y+=2
        val_x=x

        
fenetre = Tk()

canvas = Canvas(fenetre, width=640, height=639, background="#219a21")
mapx=1
mapy=1
Deplacement=0
MonPerso=[0,0,96,96]
MonEnnemi=[0,0,64,64]
Bloque_y=[]
Bloque_x=[]
Ennemi=[]
Perso=[]
afficheTerrain()
mouvement_perso()
canvas.pack()
canvas.focus_set()
canvas.bind("<Key>", bouger)
canvas.bind("<KeyRelease>", stop)

        
fenetre.mainloop()
