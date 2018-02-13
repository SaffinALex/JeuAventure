#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from random import *
        
def affiche_terrain():
    global mapx
    global mapy

    canvas.delete("all")
    nom="map"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for ligne in lignes:
        for i in range (0,20):
            placer_bloc(ligne[i],(i*32),j)

        j+=32

def placer_bloc(nbr,x,y):
    global bloque_x
    global bloque_y
    
    val_x=x
    val_y=y
    nom_bloc="bloc"+str(nbr)
    fichier = open(nom_bloc,'r')
    lignes  = fichier.readlines()
    
    if not(nom_bloc=="bloc0"):
        bloque_x.append(x)
        bloque_y.append(y)

        
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
        

           
def changeMap():
    global mon_perso
    global mapx
    global mapy

    if (mon_perso[2]+32>640):
        mapx+=1
        mon_perso[2]=0
        efface_bloque()
        affiche_terrain()
        mouvement_perso()
        
    elif(mon_perso[2]<0):
        mapx-=1
        mon_perso[2]=640-32
        efface_bloque()
        affiche_terrain()
        mouvement_perso()
        
    elif(mon_perso[3]<0):
        mapy+=1
        mon_perso[3]=640-32
        efface_bloque()
        affiche_terrain()
        mouvement_perso()
        
    elif(mon_perso[3]+32>640):
        mapy-=1
        mon_perso[3]=0
        efface_bloque()
        affiche_terrain()
        mouvement_perso()

def efface_bloque():
    global bloque_x
    global bloque_y
    
    while len(bloque_x)>0:
        del bloque_x[len(bloque_x)-1]
        del bloque_y[len(bloque_y)-1]


def bloquer_perso(val_x, val_y):
    global bloque_x
    global bloque_y
    global mon_perso
    
    for i in range(0,len(bloque_x)-1):
        
        if(mon_perso[2]>=bloque_x[i] and mon_perso[2]<=bloque_x[i]+31):
            if(mon_perso[3]>=bloque_y[i] and mon_perso[3]<=bloque_y[i]+31): #Coin Haut gauche
               mon_perso[3]=val_y
               mon_perso[2]=val_x
               
            elif(mon_perso[3]+31>=bloque_y[i] and mon_perso[3]+31<=bloque_y[i]+31): #Coin Bas gauche
               mon_perso[3]=val_y
               mon_perso[2]=val_x
                
        if(mon_perso[2]+31>=bloque_x[i] and mon_perso[2]+32<=bloque_x[i]+31):
            if(mon_perso[3]+31>=bloque_y[i] and mon_perso[3]+31<=bloque_y[i]+31): #Coin Haut Droite
               mon_perso[3]=val_y
               mon_perso[2]=val_x

            elif(mon_perso[3]>=bloque_y[i] and mon_perso[3]<=bloque_y[i]+31): #Coin Bas Droite
               mon_perso[3]=val_y
               mon_perso[2]=val_x

def bloquer_ennemi(val_x, val_y):
    global bloque_x
    global bloque_y
    global mon_ennemi
    global deplacement
    
    for i in range(0,len(bloque_x)-1):
        
        if(mon_ennemi[2]>=bloque_x[i] and mon_ennemi[2]<=bloque_x[i]+31):
            if(mon_ennemi[3]>=bloque_y[i] and mon_ennemi[3]<=bloque_y[i]+31): #Coin Haut gauche
                mon_ennemi[3]=val_y
                mon_ennemi[2]=val_x
                deplacement=0

            elif(mon_ennemi[3]+31>=bloque_y[i] and mon_ennemi[3]+31<=bloque_y[i]+31): #Coin Bas gauche
                mon_ennemi[3]=val_y
                mon_ennemi[2]=val_x
                deplacement=0
                
        if(mon_ennemi[2]+31>=bloque_x[i] and mon_ennemi[2]+32<=bloque_x[i]+31):
            if(mon_ennemi[3]+31>=bloque_y[i] and mon_ennemi[3]+31<=bloque_y[i]+31): #Coin Haut Droite
                mon_ennemi[3]=val_y
                mon_ennemi[2]=val_x
                deplacement=0
                
            elif(mon_ennemi[3]>=bloque_y[i] and mon_ennemi[3]<=bloque_y[i]+31): #Coin Bas Droite
                mon_ennemi[3]=val_y
                mon_ennemi[2]=val_x
                deplacement=0



    
def frame():

    mouvement_perso()
    changeMap()
    mouvement_ennemi()
    canvas.after(70,frame)

def mouvement_perso():
    global mon_perso
    
    mon_perso[2]+=mon_perso[0]
    mon_perso[3]+=mon_perso[1]
    val_x=mon_perso[2]-mon_perso[0]
    val_y=mon_perso[3]-mon_perso[1]
    if mon_perso[1]!=0 or mon_perso[0]!=0:
        if mon_perso[5]=="Perso1":
            mon_perso[5]="Perso2"
            
        elif mon_perso[5]=="Perso2":
            mon_perso[5]="Perso3"
            
        elif mon_perso[5]=="Perso3":
            mon_perso[5]="Perso1"
    else:
            mon_perso[5]="Perso1"

    bloquer_perso(val_x,val_y)
    bouger_sprite(mon_perso[4],mon_perso[5],mon_perso[2],mon_perso[3])

def mouvement_ennemi():
    global deplacement
    global mon_ennemi

    if(deplacement<=0):
        chiffre=randint(0,4)
        mon_ennemi[0]=0
        mon_ennemi[1]=0
        
        if(chiffre==0):
            mon_ennemi[0]+=4
            
        elif(chiffre==1):
            mon_ennemi[0]-=4
        elif(chiffre==2):
            mon_ennemi[1]+=4
        elif(chiffre==3):
            mon_ennemi[1]-=4
        deplacement=10

    mon_ennemi[2]+=mon_ennemi[0]
    mon_ennemi[3]+=mon_ennemi[1]
    bloquer_ennemi(mon_ennemi[2]-mon_ennemi[0],mon_ennemi[3]-mon_ennemi[1])
    bouger_sprite(mon_ennemi[4],mon_ennemi[5],mon_ennemi[2],mon_ennemi[3])
    deplacement-=1
    

def vitesse(event):
    global mon_perso

    touche=event.keysym
    
    if touche=="Up":
        mon_perso[1]=-8
    if touche=="Down":
        mon_perso[1]=8            
    if touche=="Right":
        mon_perso[0]=8
    if touche=="Left":
        mon_perso[0]=-8

def stop(event):
    touche=event.keysym
    if(touche=="Up" or touche=="Down"):
        mon_perso[1]=0

    if(touche=="Right" or touche=="Left"):
        mon_perso[0]=0
        
        

def bouger_sprite(sprite_pos,nom,x,y):
    efface(sprite_pos)
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range (0,16):
            if ligne[i]=="1":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="green",outline="")
            elif ligne[i]=="2":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="")
            elif ligne[i]=="3":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="")
            elif ligne[i]=="4":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#808180",outline="")
            elif ligne[i]=="5":
                 pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#614919",outline="")
            elif ligne[i]=="6":
                 pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="")
            elif ligne[i]=="7":
                 pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#d4a566",outline="")
            elif ligne[i]=="8":
                 pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="white",outline="")
                 
            if ligne[i]!="0":
                sprite_pos.append(pos)

                
            val_x+=2

        val_y+=2
        val_x=x

def efface(liste):
    while len(liste)>0:
        canvas.delete(liste[len(liste)-1])
        del liste[len(liste)-1]


        
fenetre = Tk()

canvas = Canvas(fenetre, width=640, height=639, background="#219a21")
mapx=1
mapy=1
deplacement=0
mon_perso=[0,0,96,96,[],"Perso1"]
mon_ennemi=[0,0,64,64,[],"ennemi1"]
bloque_y=[]
bloque_x=[]


affiche_terrain()
frame()

canvas.pack()
canvas.focus_set()
canvas.bind("<Key>", vitesse)
canvas.bind("<KeyRelease>", stop)

        
fenetre.mainloop()
