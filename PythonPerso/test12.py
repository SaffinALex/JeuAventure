#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from random import *
        
def affiche_terrain():
    global mapx
    global mapy
    
    canvas.delete("all")
    affiche_surf()
    nom="./map/map"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for ligne in lignes:
        for i in range (0,20):
            if(ligne[i]!="0"):
                nom="./spriteDecor/bloc"+ligne[i]
                placer(nom,(i*32),j,1)
        j+=32
    fichier.close()
    affiche_ennemi()


def affiche_obj():
    global mapx
    global mapy
    
    nom="./map/mapobj"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for ligne in lignes:
        for i in range (0,20):
            if ligne[i]!="0":
                nom="./spriteObjet/objet"+ligne[i]
                placer(nom,(i*32),j,1)

        j+=32
    fichier.close()

def affiche_surf():
    global mapx
    global mapy
    
    nom="./map/mapsurf"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for ligne in lignes:
        for i in range (0,20):
            nom="./spriteDecor/bloc"+ligne[i]
            placer(nom,(i*32),j,0)

        j+=32
    fichier.close()

def ajout_ennemi(nom,x,y):
    global Ennemi
    
    fichier=open(nom+"-carac","r")
    lignes=fichier.readlines()
    liste=[0,0,x,y,[],nom+"B1","Bas",0,int(lignes[0][8]),int(lignes[1][4]),int(lignes[2][8])]
    Ennemi.append(liste)
    mouvement_ennemi(Ennemi[len(Ennemi)-1])
    fichier.close()
    
def affiche_ennemi():
    Ennemi
    nom="./map/mapennemi"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for ligne in lignes:
        for i in range (0,20):
            if(ligne[i]!="0"):
                nom="./spriteEnnemi/ennemi"+ligne[i]
                ajout_ennemi(nom,i*32,j)

        j+=32
    fichier.close()
    

def placer(nom,x,y,option):
    global bloque_x
    global bloque_y
    
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()
    
    if (option!=0):
        bloque_x.append(x)
        bloque_y.append(y)

    for ligne in lignes:
        for i in range (0,16):
            if ligne[i]=="1":
                canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="green",outline="") #vert
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
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#96c14b",outline="") #vertClaire
            elif ligne[i]=="9":
                 canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="white",outline="") #Blanc
            val_x+=2

        val_y+=2
        val_x=x
    fichier.close()
           
def changeMap():
    global mon_perso
    global Ennemi
    global mapx
    global mapy

    if (mon_perso[2]+32>640):
        mapx+=1
        mon_perso[2]=0
        Ennemi=[]
        efface_bloque()
        affiche_terrain()
	affiche_obj()
        mouvement_perso()
        
    elif(mon_perso[2]<0):
        mapx-=1
        mon_perso[2]=640-32
        Ennemi=[]
        efface_bloque()
        affiche_terrain()
	affiche_obj()
        mouvement_perso()
        
    elif(mon_perso[3]<0):
        mapy+=1
        mon_perso[3]=640-32
        Ennemi=[]
        efface_bloque()
        affiche_terrain()
	affiche_obj()        
	mouvement_perso()
        
    elif(mon_perso[3]+32>640):
        mapy-=1
        mon_perso[3]=0
        Ennemi=[]
        efface_bloque()
        affiche_terrain()
	affiche_obj()        
	mouvement_perso()

def efface_bloque():
    global bloque_x
    global bloque_y
    
    while len(bloque_x)>0:
        del bloque_x[len(bloque_x)-1]
        del bloque_y[len(bloque_y)-1]


def bloquer_entite(val_x, val_y,entite):
    global bloque_x
    global bloque_y

    for i in range(0,len(bloque_x)):
        
        if(entite[2]>=bloque_x[i] and entite[2]<=bloque_x[i]+31):
            if( entite[3]>=bloque_y[i] and  entite[3]<=bloque_y[i]+31): #Coin Haut gauche
                entite[3]=val_y
                entite[2]=val_x
               
            elif( entite[3]+31>=bloque_y[i] and  entite[3]+31<=bloque_y[i]+31): #Coin Bas gauche
                entite[3]=val_y
                entite[2]=val_x
                
        if( entite[2]+31>=bloque_x[i] and  entite[2]+32<=bloque_x[i]+31):
            if( entite[3]+31>=bloque_y[i] and entite[3]+31<=bloque_y[i]+31): #Coin Haut Droite
                entite[3]=val_y
                entite[2]=val_x
                
            elif( entite[3]>=bloque_y[i] and  entite[3]<=bloque_y[i]+31): #Coin Bas Droite
                entite[3]=val_y
                entite[2]=val_x
                
        if(entite[3]>620 or entite[3]<-8 or entite[2]>620 or entite[2]<-8):
            entite[3]=val_y
            entite[2]=val_x
                
def frame():
    global Ennemi
    global mon_perso

    #print mon_perso[0]
    evenement()
    mouvement_perso()
    changeMap()
    for i in range(0,len(Ennemi)):
        mouvement_ennemi(Ennemi[i])
        
    if(len(Ennemi)>0):
        toucher(mon_perso)
        
    canvas.after(50,frame)

def toucher(entite):

    global Ennemi
    effaces=[]

    for i in range(len(Ennemi)):

        if(entite[2]>=Ennemi[i][2] and entite[2]<=Ennemi[i][2]+31):
            if( entite[3]>=Ennemi[i][3] and  entite[3]<=Ennemi[i][3]+31): #Coin Haut gauche
                effaces.append(i)
        
            elif( entite[3]+31>=Ennemi[i][3] and  entite[3]+31<Ennemi[i][3]+31): #Coin Bas gauche
                effaces.append(i)
                
        if( entite[2]+31>=Ennemi[i][2] and  entite[2]+32<=Ennemi[i][2]+31):
            if( entite[3]+31>=Ennemi[i][3] and entite[3]+31<=Ennemi[i][3]+31): #Coin Haut Droite
                effaces.append(i)
                
            elif( entite[3]>=Ennemi[i][3] and  entite[3]<=Ennemi[i][3]+31): #Coin Bas Droite
                effaces.append(i)
                
    for i in range(len(effaces)):
        efface(Ennemi[effaces[i]][4])
        del Ennemi[effaces[i]]
            
                    
def mouvement_perso():
    global mon_perso
           
    val_x=mon_perso[2]
    val_y=mon_perso[3] 
    mon_perso[2]+=mon_perso[0]
    mon_perso[3]+=mon_perso[1]
    orientation(mon_perso)
    bloquer_entite(val_x,val_y,mon_perso)
    bouger_sprite(mon_perso[4],mon_perso[5],mon_perso[2],mon_perso[3])

def orientation(entite) : 
	sprite=""
	numero=len(entite[5])
	for i in range (0,numero-2) : 
		sprite+=entite[5][i]

	numero=int(entite[5][numero-1])
        lettre=entite[5][len(entite[5])-2]
        

	if entite[0]>0 :
            entite[6]="Droite"
            numero+=1
            entite[5]=sprite+"D"+str(numero)
            lettre="D"
            
        elif entite[0]<0 : 
    	    entite[6]="Gauche"
            numero+=1
            entite[5]=sprite+"G"+str(numero)
            lettre="G"
   
        elif entite[1]>0 : 
    	    entite[6]="Bas"
            numero+=1
            entite[5]=sprite+"B"+str(numero)
            lettre="B"
    	
        elif entite[1]<0 : 
    	    entite[6]="Haut"
            numero+=1
            entite[5]=sprite+"H"+str(numero)
            lettre="H"
        
        elif (entite[1]==0 and entite[0]==0) : 
    	    entite[5]=sprite+lettre+str(1)
            
        if numero>3 : 
    	    entite[5]=sprite+lettre+str(1)


    	
def mouvement_ennemi(mon_ennemi):

    if(mon_ennemi[7]<=0):
        chiffre=randint(0,4)
        mon_ennemi[0]=0
        mon_ennemi[1]=0
        
        if(chiffre==0):
            mon_ennemi[0]+=mon_ennemi[8]
            mon_ennemi[6]="Droite"
        elif(chiffre==1):
            mon_ennemi[0]-=mon_ennemi[8]
            mon_ennemi[6]="Gauche"
        elif(chiffre==2):
            mon_ennemi[1]+=mon_ennemi[8]
            mon_ennemi[6]="Bas"
        elif(chiffre==3):
            mon_ennemi[1]-=mon_ennemi[8]
            mon_ennemi[6]="Haut"
        mon_ennemi[7]=10

    mon_ennemi[2]+=mon_ennemi[0]
    mon_ennemi[3]+=mon_ennemi[1]
    orientation(mon_ennemi)
    bloquer_entite(mon_ennemi[2]-mon_ennemi[0],mon_ennemi[3]-mon_ennemi[1],mon_ennemi)
    bouger_sprite(mon_ennemi[4],mon_ennemi[5],mon_ennemi[2],mon_ennemi[3])
    mon_ennemi[7]-=1

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

def evenement():
    global mapx
    global mapy
    global coffre1
    global ferme1
    global Ennemi

    if(mapx==1 and mapy==1):
        if(coffre1==False):
            if(not(len(Ennemi)>0)):
                
                #fichier=open("./map/mapobj1-1","r")
                #lignes=fichier.readlines()
                #newligne=""

                #for i in range(len(lignes[1])):
                 #   if(i==5):
                 #       newligne+="2"
                  #  else:
                   #     newligne+=lignes[1][i]
               # lignes[1]=newligne

                #fichier.close()
                
                #fichier=open("./map/mapobj1-1","w")
                #fichier.close()
                
                #fichier=open("./map/mapobj1-1","a")
               # for i in range(0,16):
                #    fichier.write(lignes[i]) 
                    
                coffre1=True
                placer("./spriteObjet/objet2",160,32,1)
                #fichier.close()
                

        
        

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
                 pos= canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#96c14b",outline="") #vertClaire
            elif ligne[i]=="9":
                 pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="white",outline="")
                 
            if ligne[i]!="0":
                sprite_pos.append(pos)

                
            val_x+=2

        val_y+=2
        val_x=x
        fichier.close()

def efface(liste):
    while len(liste)>0:
        canvas.delete(liste[len(liste)-1])
        del liste[len(liste)-1]


        
fenetre = Tk()

canvas = Canvas(fenetre, width=640, height=639, background="#219a21")
mapx=1
mapy=1
deplacement=0
mon_perso=[0,0,96,96,[],"./spritePerso/PersoB1","Bas"]
Ennemi=[]
bloque_y=[]
bloque_x=[]
coffre1=False


affiche_terrain()
affiche_obj()
frame()

canvas.pack()
canvas.focus_set()
canvas.bind("<Key>", vitesse)
canvas.bind("<KeyRelease>", stop)

        
fenetre.mainloop()
    
