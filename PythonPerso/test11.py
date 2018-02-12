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
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#F5F5DC",outline="")
            elif ligne[i]=="3":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="")
                
            val_x+=2

        val_y+=2
        val_x=x
        
def afficheTerrain():
    global mapx
    global mapy
    
    nom="map"+str(mapy)+"-"+str(mapx)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for ligne in lignes:
        for i in range (0,19):
            if i>0:
                placerBloc(ligne[i],(i*32)-1,j)
            else:
                placerBloc(ligne[i],i,j)
            
        j+=32


def Bloquer(val_x, val_y):
    global Bloque_x
    global Bloque_y
    global MonPerso
    
    for i in range(0,len(Bloque_x)-1):
        
        if(MonPerso[2]>=Bloque_x[i] and MonPerso[2]<=Bloque_x[i]+32):
            if(MonPerso[3]>=Bloque_y[i] and MonPerso[3]<=Bloque_y[i]+32):
                MonPerso[3]=val_y
                MonPerso[2]=val_x
                
        if(MonPerso[2]+32>=Bloque_x[i] and MonPerso[2]+16<=Bloque_x[i]+32):
            if(MonPerso[3]+32>=Bloque_y[i] and MonPerso[3]+16<=Bloque_y[i]+32):
                MonPerso[3]=val_y
                MonPerso[2]=val_x

        if(MonPerso[2]+32>=Bloque_x[i] and MonPerso[2]+16<=Bloque_x[i]+32):
            if(MonPerso[3]>=Bloque_y[i] and MonPerso[3]<=Bloque_y[i]+32):
                MonPerso[3]=val_y
                MonPerso[2]=val_x

        if(MonPerso[2]>=Bloque_x[i] and MonPerso[2]<=Bloque_x[i]+32):
            if(MonPerso[3]+16>=Bloque_y[i] and MonPerso[3]+16<=Bloque_y[i]+32):
                MonPerso[3]=val_y
                MonPerso[2]=val_x
           

def mouvement_perso():
    global x
    global y
    global MonPerso
    global MonEnnemi
    global Deplacement
    global Joueur
    global Ennemi

    canvas.delete(Joueur)
    
    MonPerso[2]+=MonPerso[0]
    MonPerso[3]+=MonPerso[1]
    val_x=MonPerso[2]-MonPerso[0]
    val_y=MonPerso[3]-MonPerso[1]

    Bloquer(val_x,val_y)
    
    Joueur=canvas.create_rectangle(MonPerso[2],MonPerso[3],MonPerso[2]+32,MonPerso[3]+32,fill="blue",outline="")

    if(Deplacement==0):
        chiffre=randint(0,4)
        MonEnnemi[0]=0
        MonEnnemi[1]=0
        
        if(chiffre==0):
            MonEnnemi[0]+=2
        elif(chiffre==1):
            MonEnnemi[0]-=2
        elif(chiffre==2):
            MonEnnemi[1]+=2
        elif(chiffre==3):
            MonEnnemi[1]-=2
        Deplacement=10

    MonEnnemi[2]+=MonEnnemi[0]
    MonEnnemi[3]+=MonEnnemi[1]
    placerSkin(1,MonEnnemi[2],MonEnnemi[3])
    print MonEnnemi[0]
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
        
def effaceSkin(nbr,x,y):
    global Ennemi
    while len(Ennemi)>0:
        canvas.delete(Ennemi[len(Ennemi)-1])
        del Ennemi[len(Ennemi)-1]
    

def placerSkin(nbr,x,y):
    global Ennemi
    effaceSkin(nbr,x,y)
    val_x=x
    val_y=y
    nomEnnemi="ennemi"+str(nbr)
    fichier = open(nomEnnemi,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range (0,16):
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

        
fenetre = Tk()

canvas = Canvas(fenetre, width=640, height=639, background="#F5F5DC")
mapx=1
mapy=1
Deplacement=0
MonPerso=[0,0,32,0]
MonEnnemi=[0,0,100,150]
Bloque_y=[]
Bloque_x=[]
Ennemi=[]
Joueur=canvas.create_rectangle(MonPerso[2],MonPerso[3],MonPerso[2]+32,MonPerso[3]+32,fill="blue",outline="")
afficheTerrain()
mouvement_perso()
canvas.pack()
canvas.focus_set()
canvas.bind("<Key>", bouger)
canvas.bind("<KeyRelease>", stop)

        
fenetre.mainloop()
