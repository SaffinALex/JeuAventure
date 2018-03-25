#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from random import *
        
def affiche_terrain(nom):
    global nommap

    canvas.delete("all")
    nommap=nom
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0
    i=0

    for cpt in range(0,20):
        i=0
        while i<40:
            nom="./spriteSurface/bloc"+lignes[cpt][i]+lignes[cpt][i+1]
            placer(nom,(i*16),j,0)
            i+=2
        j+=32
    fichier.close()
    affiche_surf(nommap)
    affiche_obj(nommap)
    if(attendre == False):
	affiche_ennemi(nommap)


def affiche_obj(nom):

    global listeitem
    global listechangement
    ouvert=False
    porte_ouverte=False
    
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0
    i=0
    nom_bis=nom

    for cpt in range(60,80):
        i=0
        while i<40:
            num=lignes[cpt][i]+lignes[cpt][i+1]
            if num !="00":
                ouvert=False
                if num=="05" or num=="06" or num=="07" or num=="08":              
                    if(len(listechangement) != 0):
                        for k in range (0,len(listechangement)):
                            if nom_bis==listechangement[k][2]  and listechangement[k][0]==i*16 and listechangement[k][1]==j:
                                nom="./spriteObjet/objet"+"04"
                                placer(nom,(i*16),j,2)
                                ouvert=True

                        if(not(ouvert)):
                            nom="./spriteObjet/objet"+"02"
                            listeitem.append([num,i*16,j,0,0,[]])
                            placer(nom,(i*16),j,1)


                    else:
                        nom="./spriteObjet/objet"+"02"
                        listeitem.append([num,i*16,j,0,0,[]])
                        placer(nom,(i*16),j,2)
                elif num=="12" or num=="15" or num=="16" :
                    porte_ouverte=False
                    for k in range (0,len(listechangement)):
                        if nom_bis==listechangement[k][2] and listechangement[k][0]==i*16 and listechangement[k][1]==j and (listechangement[k][4]=="12" or listechangement[k][4]=="15" or listechangement[k][4]=="16"):
                            porte_ouverte=True
                            listeitem.append([num,i*16,j,0,1,[]])
                            
                    if(not(porte_ouverte)):            
                        listeitem.append([num,i*16,j,0,0,[]])
                        nom="./spriteObjet/objet"+num
                        placer(nom,(i*16),j,2)                        
                            
                else:
                    listeitem.append([num,i*16,j,0,0,[]])
                    nom="./spriteObjet/objet"+num
                    placer(nom,(i*16),j,2)
            i+=2

        j+=32
    fichier.close()

def affiche_surf(nom):
    global mapx
    global mapy
    
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0
    i=0

    for cpt in range(20,40):
        i=0
        while i<40:
            num=lignes[cpt][i]+lignes[cpt][i+1]
            if num!="00":
                nom="./spriteDecor/bloc"+num
                placer(nom,(i*16),j,1)
            i+=2
        j+=32
    fichier.close()

def ajout_ennemi(nom,x,y):
    global Ennemi
    
    fichier=open(nom+"-carac","r")
    lignes=fichier.readlines()
    liste=[0,0,x,y,[],nom+"B1","Bas",0,int(lignes[0][8]),int(lignes[1][4]),int(lignes[2][8]),0] #vitesse, vie, dommage.
    Ennemi.append(liste)
    mouvement_ennemi(Ennemi[len(Ennemi)-1])
    fichier.close()
    
def affiche_ennemi(nom):
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0
    i=0

    for cpt in range(40,60):
        i=0
        while i<40:
            num=lignes[cpt][i]+lignes[cpt][i+1]
            if num!="00":
                nom="./spriteEnnemi/ennemi"+num+"/ennemi"+num
                ajout_ennemi(nom,i*16,j)
            i+=2

        j+=32
    fichier.close()
    

def placer(nom,x,y,option): #0=Transparent, 1=bloquer, 2=item
    global bloque_x
    global bloque_y
    global bloquer
    global listeitem
    
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()
    fig=0
    
    if (option!=0):
        bloque_x.append(x)
        bloque_y.append(y)
        bloquer[x/32+y/32*20].append(x)
        bloquer[x/32+y/32*20].append(y)

    for ligne in lignes:
        for i in range (0,16):
            if ligne[i]=="1":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0a650a",outline="") #vert
            elif ligne[i]=="2":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="") #noir
            elif ligne[i]=="3":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="") #bleu
            elif ligne[i]=="4":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#808180",outline="") #gris
            elif ligne[i]=="5":
                 fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#614919",outline="") #marron
            elif ligne[i]=="6":
                 fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="") #rouge 
            elif ligne[i]=="7":
                 fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#d4a566",outline="") #beige
            elif ligne[i]=="8":
                 fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0dac07",outline="") #vertClaire
            elif ligne[i]=="9":
                 fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="white",outline="") #Blanc
            elif ligne[i]=="A":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#6d5331",outline="") #MarronClaire
            elif ligne[i]=="B":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#383837",outline="") #NOIRCLAIRE(OMBRE)
            elif ligne[i]=="C":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#e3e570",outline="") #JAUNECLAIRE
            elif ligne[i]=="D": #BleuGlace 
               fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#b2d5f6",outline="")
            elif ligne[i]=="E":
               fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#261f2f",outline="") #BleuFoncée/Gris

               

            if(option==2 and ligne[i]!=0 and len(listeitem)!=0):
                listeitem[len(listeitem)-1][5].append(fig)

                
            val_x+=2

        val_y+=2
        val_x=x
    fichier.close()
           
def changeMap():
    global mon_perso
    global Ennemi
    global mapx
    global mapy
    global nommap

    if (mon_perso[2]+32>640):
        mapx+=1
        mon_perso[2]=0
        Ennemi=[]
        mon_perso[10]=[0,0,0,0,[],""]
        efface_bloque()
        efface_listeitem()
        nommap="./map/map"+str(mapx+1)+str(mapy)
        affiche_terrain(nommap)
        mouvement_perso()
        
    elif(mon_perso[2]<0):
        mapx-=1
        mon_perso[2]=640-32
        Ennemi=[]
        mon_perso[10]=[0,0,0,0,[],""]
        efface_bloque()
        efface_listeitem()
        nommap="./map/map"+str(mapx-1)+str(mapy)
        affiche_terrain(nommap)
        mouvement_perso()
        
    elif(mon_perso[3]<0):
        mapy+=1
        mon_perso[3]=640-32
        Ennemi=[]
        mon_perso[10]=[0,0,0,0,[],""]
        efface_bloque()
        efface_listeitem()
        nommap="./map/map"+str(mapx)+str(mapy-1)
        affiche_terrain(nommap)
	mouvement_perso()
        
    elif(mon_perso[3]+32>640):
        mapy-=1
        mon_perso[3]=0
        Ennemi=[]
        mon_perso[10]=[0,0,0,0,[],""]
        efface_bloque()
        efface_listeitem()
        nommap="./map/map"+str(mapx)+str(mapy+1)
        affiche_terrain(nommap)    
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


    for i in range(len(bloque_x)):
        if(entite[2]>=bloque_x[i] and entite[2]<=bloque_x[i]+31):
            if( entite[3]+16>=bloque_y[i] and  entite[3]+16<=bloque_y[i]+31): #Coin Haut gauche
                entite[3]=val_y
                entite[2]=val_x
                break
               
            elif( entite[3]+31>=bloque_y[i] and  entite[3]+31<=bloque_y[i]+31): #Coin Bas gauche
                entite[3]=val_y
                entite[2]=val_x
                break
                
        if( entite[2]+31>=bloque_x[i] and  entite[2]+32<=bloque_x[i]+31):
            if( entite[3]+31>=bloque_y[i] and entite[3]+31<=bloque_y[i]+31): #Coin Bas Droite
                entite[3]=val_y
                entite[2]=val_x
                break
            
            elif( entite[3]+16>=bloque_y[i] and  entite[3]+16<=bloque_y[i]+31): #Coin Haut Droite
                entite[3]=val_y
                entite[2]=val_x
                break
                
    if(entite[3]>620 or entite[3]<-8 or entite[2]>620 or entite[2]<-8):
        entite[3]=val_y
        entite[2]=val_x

def aff_attaque():
    global mon_perso
    global sprite_att

    x=mon_perso[2]
    y=mon_perso[3]
    fichier = open("./Attaque/epee",'r')
    lignes  = fichier.readlines()
    efface(sprite_att)
    if mon_perso[7]==0:
        mon_perso[9][1]=False
    
    else:
        efface(mon_perso[4])

        if mon_perso[6]=="Bas":
            
            num=0*96+96-mon_perso[7]*32
            for i in range (0,32):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                y+=2
                
        elif mon_perso[6]=="Haut":
            num=1*96+96-mon_perso[7]*32
            for i in range (0,32):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                if(y>mon_perso[3]+31):
                    y-=64
                    
                y+=2
                
        elif mon_perso[6]=="Droite":
            num=2*96+96-mon_perso[7]*32
            for i in range (0,32):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                if(y>mon_perso[3]+31):
                    y-=32
                    x+=32
                    
                y+=2
        elif mon_perso[6]=="Gauche":
            num=3*96+96-mon_perso[7]*32
            for i in range (0,32):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                if(y>mon_perso[3]+31):
                    y-=32
                    x-=32
                    
                y+=2


        mon_perso[7]-=1
    
def aff_arc():
    global mon_perso
    global sprite_att

    x=mon_perso[2]
    y=mon_perso[3]
    fleche=mon_perso[10]
    fichier = open("./Attaque/arc/arc",'r')
    lignes  = fichier.readlines()
    efface(sprite_att)
    if mon_perso[7]==0:
        mon_perso[9][1]=False
    
    else:
        efface(mon_perso[4])

        if mon_perso[6]=="Bas":
            num=0
            for i in range (0,16):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                y+=2
            if fleche[1]==0 and fleche[0]==0:
                fleche[1]=8
                fleche[2]=mon_perso[2]
                fleche[3]=mon_perso[3]
                fleche[5]="Bas"
            
                
        elif mon_perso[6]=="Haut":
            num=16
            for i in range (0,16):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32                
                y+=2
            if fleche[1]==0 and fleche[0]==0:
                fleche[1]=-8
                fleche[2]=mon_perso[2]
                fleche[3]=mon_perso[3]
                fleche[5]="Haut"
                
        elif mon_perso[6]=="Droite":
            num=48
            for i in range (0,16):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                y+=2
            if fleche[1]==0 and fleche[0]==0:
                fleche[0]=8
                fleche[2]=mon_perso[2]
                fleche[3]=mon_perso[3]
                fleche[5]="Droite"
                
        elif mon_perso[6]=="Gauche":
            num=32
            for i in range (0,16):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                y+=2
            if fleche[1]==0 and fleche[0]==0:
                fleche[0]=-8
                fleche[2]=mon_perso[2]
                fleche[3]=mon_perso[3]
                fleche[5]="Gauche"


        mon_perso[7]-=1

def placer_fleche(nom,x,y,sprite):
    efface(sprite)
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range(0,16):
    
            if ligne[i]=="1":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0a650a",outline="") #vert
            elif ligne[i]=="2":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="") #noir
            elif ligne[i]=="3":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="") #bleu
            elif ligne[i]=="4":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#808180",outline="") #gris
            elif ligne[i]=="5":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#614919",outline="") #marron
            elif ligne[i]=="6":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="") #rouge 
            elif ligne[i]=="7":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#d4a566",outline="") #beige
            elif ligne[i]=="8":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0dac07",outline="") #vertClaire
            elif ligne[i]=="9":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="white",outline="") #Blanc
            elif ligne[i]=="A":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#6d5331",outline="") #MarronClaire
            elif ligne[i]=="B":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#383837",outline="") #NOIRCLAIRE(OMBRE)
            elif ligne[i]=="C":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#e3e570",outline="") #JAUNECLAIRE
            elif ligne[i]=="D": #BleuGlace 
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#b2d5f6",outline="")
                
            if ligne[i]!="0":
                sprite.append(fig)
            val_x+=2

        val_y+=2
        val_x=x
    fichier.close()
        
def placer_attaque(num,val_x,val_y):
    global sprite_att
    
    if num=="1":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0a650a",outline="") #vert
    elif num=="2":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="") #noir
    elif num=="3":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="") #bleu
    elif num=="4":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#808180",outline="") #gris
    elif num=="5":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#614919",outline="") #marron
    elif num=="6":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="") #rouge 
    elif num=="7":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#d4a566",outline="") #beige
    elif num=="8":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0dac07",outline="") #vertClaire
    elif num=="9":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="white",outline="") #Blanc
    elif num=="A":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#6d5331",outline="") #MarronClaire
    elif num=="B":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#383837",outline="") #NOIRCLAIRE(OMBRE)
    elif num=="C":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#e3e570",outline="") #JAUNECLAIRE
    elif num=="D": #BleuGlace 
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#b2d5f6",outline="")

    if num!="0":
        sprite_att.append(fig)
    
                
def frame():
    global Ennemi
    global mon_perso
    global listeitem
    global attendre
    global joueur_touche

    efface=[]
    if(not attendre):

        evenement()
        changeMap()
        joueur_toucher()
	test_changement_map(listeitem)

        for i in range(0,len(Ennemi)):
            if Ennemi[i][9]<=0:
                efface.append(i)
        mort(efface)
        
        if mon_perso[9][1]:
            if mon_perso[9][0]==0:
                if mon_perso[9][2]=="Epee":
                    aff_attaque()
                elif mon_perso[9][2]=="Arc":
                    aff_arc()
                mon_perso[9][0]=1
            else:
                mon_perso[9][0]-=1
                
        if(mon_perso[10][1] != 0 or mon_perso[10][0] != 0):
            mon_perso[10][2]+=mon_perso[10][0]
            mon_perso[10][3]+=mon_perso[10][1]
            placer_fleche("./Attaque/arc/fleche"+mon_perso[10][5][0],mon_perso[10][2],mon_perso[10][3],mon_perso[10][4])
            bloquer_fleche(mon_perso[10])
                
        if(not mon_perso[9][1]):
            mouvement_perso()
            
        for i in range(0,len(Ennemi)):
            mouvement_ennemi(Ennemi[i])
        
        if(len(Ennemi)>0):             
            if mon_perso[9][1] and (mon_perso[10][1]==0 and mon_perso[10][0]==0):
                toucher(mon_perso)
            elif mon_perso[10][0]!=0 or mon_perso[10][1]!=0:
                toucher_fleche(mon_perso[10])
            
        for i in range(0,len(listeitem)):
            if(listeitem[i][3]>0):
                compt(listeitem[i])
        
        canvas.after(30,frame)

def bloquer_fleche(entite):
    global bloque_x
    global bloque_y
    global mon_perso


    for i in range(len(bloque_x)):
        if(entite[2]>=bloque_x[i] and entite[2]<=bloque_x[i]+31):
            if( entite[3]+16>=bloque_y[i] and  entite[3]+16<=bloque_y[i]+31): #Coin Haut gauche
                efface(entite[4])
                mon_perso[10]=[0,0,0,0,[],""]
                break
               
            elif( entite[3]+31>=bloque_y[i] and  entite[3]+31<=bloque_y[i]+31): #Coin Bas gauche
                efface(entite[4])
                mon_perso[10]=[0,0,0,0,[],""]
                break
                
        if( entite[2]+31>=bloque_x[i] and  entite[2]+32<=bloque_x[i]+31):
            if( entite[3]+31>=bloque_y[i] and entite[3]+31<=bloque_y[i]+31): #Coin Bas Droite
                efface(entite[4])
                mon_perso[10]=[0,0,0,0,[],""]
                break
            
            elif( entite[3]+16>=bloque_y[i] and  entite[3]+16<=bloque_y[i]+31): #Coin Haut Droite
                efface(entite[4])
                mon_perso[10]=[0,0,0,0,[],""]
                break
                
    if(entite[3]>620 or entite[3]<-8 or entite[2]>620 or entite[2]<-8):
        efface(mon_perso[4])
        mon_perso[10]=[0,0,0,0,[],""]
        
def mort(effaces):
    global Ennemi
    for i in range(0,len(effaces)):
        efface(Ennemi[effaces[len(effaces)-1]][4])
        del Ennemi[effaces[len(effaces)-1]]
        del effaces[len(effaces)-1]

def joueur_toucher():
    global mon_perso
    global Ennemi
    touche=False
    posx=mon_perso[2]
    posy=mon_perso[3]
    for i in range(0,len(Ennemi)):
        if(Ennemi[i][6]=="Haut"):
            posx2=Ennemi[i][2]
            posy2=Ennemi[i][3]+16
        else:
            posx2=Ennemi[i][2]
            posy2=Ennemi[i][3]
            
        if posx2>=posx and posx2<posx+31 and posy2+31>=posy and posy2+16<posy+31:
            touche=True
            ennemi=Ennemi[i]
            break
        elif posx2+31>=posx and posx2+31<posx+31 and posy2+16>=posy and posy2+16<posy+31:
            touche=True
            ennemi=Ennemi[i]
            break       
        elif posx2>=posx and posx2<posx+31 and posy2>=posy and posy2<posy+31:
            touche=True
            ennemi=Ennemi[i]
            break   
        elif posx2+31>=posx and posx2+31<posx+31 and posy2>=posy and posy2<posy+31:
            touche=True
            ennemi=Ennemi[i]
            break       
                
    if(touche):
            sprite=""
            E=mon_perso
	    for j in range (0,len(mon_perso[5])-2) :
		sprite+=mon_perso[5][j]
                
            if E[11]<=0:
                E[11]=5
                
            if(E[6]=="Bas"):
                E[1]=-8
                E[0]=0
                E[5]=sprite+"B4"            
            elif(E[6]=="Haut"):
                E[1]=8
                E[0]=0
                E[5]=sprite+"H4"
            elif(E[6]=="Droite"):
                E[0]=-8
                E[1]=0
                E[5]=sprite+"D4"
            elif(E[6]=="Gauche"):
                E[0]=8
                E[1]=0
                E[5]=sprite+"G4"

def toucher_fleche(fleche):
    global Ennemi
    global mon_perso
    effaces=[]
    if fleche[0]!=0 or fleche[1]!=0:
        posx=fleche[2]
        posy=fleche[3]
        for i in range(0,len(Ennemi)):
            if Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
                effaces.append(i)
            elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
                effaces.append(i)               
            elif Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
                effaces.append(i)            
            elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
                effaces.append(i)
           
    if(len(effaces)>0):
        mon_perso[10]=[0,0,0,0,[],"Bas"]
        efface(fleche[4])
        for i in range(0, len(effaces)):
            E=Ennemi[effaces[len(effaces)-1]]
            sprite=""
	    for j in range (0,len(E[5])-2) :
		sprite+=E[5][j]
            if E[11]<=0:
                E[9]-=1
                E[11]=5
            if(fleche[5]=="Bas"):
                E[1]=8
                E[0]=0
                E[5]=sprite+"B4"  
            elif(fleche[5]=="Haut"):
                E[1]=-8
                E[0]=0
                E[5]=sprite+"H4"
            elif(fleche[5]=="Droite"):
                E[0]=8
                E[1]=0
                E[5]=sprite+"D4"
            elif(fleche[5]=="Gauche"):
                E[0]=-8
                E[1]=0
                E[5]=sprite+"G4"
            del effaces[len(effaces)-1]

        
def toucher(entite):

    global Ennemi
    effaces=[]

    if entite[6]=="Haut" or entite[6]=="Bas":
        if entite[6]=="Haut":
            posx=entite[2]
            posy=entite[3]
        
        if entite[6]=="Bas":
            posx=entite[2]
            posy=entite[3]+16
            
        for i in range(0,len(Ennemi)):
            if Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
                effaces.append(i)
                
            elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
                effaces.append(i)
                
            elif Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
                effaces.append(i)
                
            elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
                effaces.append(i)
                
    if entite[6]=="Droite" or entite[6]=="Gauche":
        if entite[6]=="Gauche":
            posx=entite[2]-16
            posy=entite[3]
            
        if entite[6]=="Droite":
            posx=entite[2]+16
            posy=entite[3]

            
        for i in range(0,len(Ennemi)):
            if Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
                effaces.append(i)
                
            elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
                effaces.append(i)
                
            elif Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
                effaces.append(i)
                
            elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
                effaces.append(i)
                
    if(len(effaces)>0):
        for i in range(0, len(effaces)):
            E=Ennemi[effaces[len(effaces)-1]]
            sprite=""
	    for j in range (0,len(E[5])-2) :
		sprite+=E[5][j]
            if E[11]<=0:
                E[9]-=1
                E[11]=5
                
            if(entite[6]=="Bas"):
                E[1]=8
                E[0]=0
                E[5]=sprite+"B4"            
            elif(entite[6]=="Haut"):
                E[1]=-8
                E[0]=0
                E[5]=sprite+"H4"
            elif(entite[6]=="Droite"):
                E[0]=8
                E[1]=0
                E[5]=sprite+"D4"
            elif(entite[6]=="Gauche"):
                E[0]=-8
                E[1]=0
                E[5]=sprite+"G4"
            del effaces[len(effaces)-1]

            
                    
def mouvement_perso():
    global mon_perso
           
    val_x=mon_perso[2]
    val_y=mon_perso[3] 
    mon_perso[2]+=mon_perso[0]
    mon_perso[3]+=mon_perso[1]
    if mon_perso[11]>0:
        mon_perso[11]-=1
        if mon_perso[11]==0:
            mon_perso[0]=0
            mon_perso[1]=0
    else:
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
    if mon_ennemi[11]>0:
        mon_ennemi[11]-=1
        if mon_ennemi[11]==0:
            mon_ennemi[7]=0
    else:
        mon_ennemi[7]-=1
        orientation(mon_ennemi)
    bouger_sprite(mon_ennemi[4],mon_ennemi[5],mon_ennemi[2],mon_ennemi[3])
    bloquer_entite(mon_ennemi[2]-mon_ennemi[0],mon_ennemi[3]-mon_ennemi[1],mon_ennemi)

def vitesse(event):
    global mon_perso
    global rectangle
    global idmessage
    global attendre

    touche=event.keysym
    if mon_perso[11]<=0:
        if touche=="Up":
            mon_perso[1]=-8

        if touche=="Down":
            mon_perso[1]=8

        if touche=="Right":
            mon_perso[0]=8

        if touche=="Left":
            mon_perso[0]=-8

        
    if(touche=="a"):
	if(attendre == True):
		attendre = False
		canvas.delete(rectangle)
		canvas.delete(idmessage)
		frame()
	else:
		interagir()
    if(touche=="b"):
        attaque("Epee")
    elif(touche=="c"):
        attaque("Arc")

def attaque(arme):
    global mon_perso
    if not mon_perso[9][1]:
        mon_perso[9][1]=True
        mon_perso[9][0]=0
        mon_perso[9][2]=arme
        mon_perso[7]=3


def placer_sol(x,y):
    canvas.create_rectangle(x,y,x+32,y+32,fill="#219a21",outline="") #vert


def stop(event):
    touche=event.keysym
    if mon_perso[11]<=0:
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
    global listeitem

    if(mapx==1 and mapy==1):
        if(coffre1==False):
            if(not(len(Ennemi)>0)):                 
                coffre1=True
                listeitem.append(["07",256,224,0,0,[]])
                placer("./spriteObjet/objet02",256,224,2)
                

        
        

def bouger_sprite(sprite_pos,nom,x,y):
    efface(sprite_pos)
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range (0,16):                
            if ligne[i]=="1":
                pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0a650a",outline="")
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

def compt(liste):
    if liste[0]=="05" or liste[0]=="06" or liste[0]=="07" or liste[0]=="08":
        liste[3]-=1
        if liste[3]==0:
            placer("./spriteObjet/objet04",liste[1],liste[2],0)
            
def efface_listeitem():
    global listeitem
    while len(listeitem)>0:
        del listeitem[len(listeitem)-1]

def efface_item(liste):
    for i in range(0,len(liste[5])):
        canvas.delete(liste[5][0])
        del liste[5][0]

def test_changement_map(liste):
	global idmap
	global fichier
	global mon_perso
	global nommap
	for i in range (0,len(listeitem)) : 
		  if((liste[i][0]=="12" or liste[i][0]=="16" or liste[i][0]=="15" or liste[i][0]=="D") and listeitem[i][4] == 1 ):			
			if(mon_perso[2]+16>listeitem[i][1] and mon_perso[2]+16<listeitem[i][1]+31 and mon_perso[3]+16>listeitem[i][2] and mon_perso[3]+16<listeitem[i][2]+32):
				tp = str(mapx)+str(mapy)+str(liste[i][1])+str(liste[i][2])


				print(tp)
				nom="./tp/"+str(tp)
    				fichier=open(nom,"r")
				lignes = fichier.readlines()
				map_tp1 = lignes[0]
				mon_perso[2] = int(lignes[1])
				mon_perso[3] = int(lignes[2])
				map_tp = "./map/"+str(map_tp1[:(len(map_tp1)-1)])
				nommap = map_tp


				efface_bloque()
        			efface_listeitem()
				affiche_terrain(map_tp)
				mouvement_perso()
				

def interaction(liste):
    global inventaire
    global listechangement
    global bloque_x
    global bloque_y
    numero_eff=[]
    global idmessage
    global rectangle
    global attendre
    global nommap
    if liste[0]=="05" or liste[0]=="06" or liste[0]=="07" or liste[0]=="08":
        if liste[4]!=1:
            liste[3]=10
            liste[4]=1
            listechangement.append([liste[1],liste[2],nommap,0,liste[0]])
            placer("./spriteObjet/objet"+liste[0],liste[1],liste[2],0)
            if liste[0]=="05":
                inventaire[0]+=1
                print inventaire[0]
            elif liste[0]=="06":
                inventaire[0]+=5
                print inventaire[0]
            elif liste[0]=="07":
                inventaire[1]+=1

            
    if (liste[0]=="12" or liste[0]=="16" or liste[0]=="15") and inventaire[1]>0 and liste[4]!=1:
        
        inventaire[1]-=1
        print inventaire[1]
        listechangement.append([liste[1],liste[2],mapx,mapy,liste[0]])
        
        for i in range(0,len(bloque_x)):
            if(bloque_x[i]==liste[1] and bloque_y[i]==liste[2]):
                numero_eff.append(i)
                liste[4]=1
                efface_item(liste)

                
        if len(numero_eff)!=0:
            for j in range(0, len(numero_eff)):
                del bloque_x[numero_eff[len(numero_eff)-1]]
                del bloque_y[numero_eff[len(numero_eff)-1]]
                del numero_eff[len(numero_eff)-1]
                
    if liste[0]=="10":
	fichier = str(mapx)+str(mapy)+str(liste[1])+str(liste[2])
	chemin = "messages/sign/"+fichier
	mon_fichier = open(chemin, "r")
	message = mon_fichier.read()	
	attendre = True
	rectangle = canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white')
	idmessage = canvas.create_text(320, 590, text = message)
        
def interagir():
    global listeitem
    global mon_perso
    
    taille=len(listeitem)
    posx=mon_perso[2]+16
    posy=mon_perso[3]+16

    for i in range(0,taille):
        
        if mon_perso[6]=="Bas":
            if mon_perso[3]+33>=listeitem[i][2] and mon_perso[3]+33<=listeitem[i][2]+32 and posx>listeitem[i][1] and posx<listeitem[i][1]+32:
                interaction(listeitem[i])
                break
                
        elif mon_perso[6]=="Haut":
            if mon_perso[3]+16>=listeitem[i][2]and mon_perso[3]+16<=listeitem[i][2]+32 and posx>listeitem[i][1] and posx<listeitem[i][1]+32:
                interaction(listeitem[i])
                break


        elif mon_perso[6]=="Gauche":
            if mon_perso[2]-1>=listeitem[i][1] and mon_perso[2]-1<=listeitem[i][1]+32 and posy>=listeitem[i][2] and posy<listeitem[i][2]+32:
                interaction(listeitem[i])
                break

        elif mon_perso[6]=="Droite":
            if mon_perso[2]+33>=listeitem[i][1] and mon_perso[2]+33<=listeitem[i][1]+32 and posy>listeitem[i][2] and posy<listeitem[i][2]+32:
                interaction(listeitem[i])
                break


    

fenetre = Tk()

canvas = Canvas(fenetre, width=640, height=639, background="black")
mapx=1
mapy=1
nommap="./map/map1-1"
deplacement=0
mon_perso=[0,0,320,400,[],"./spritePerso/PersoB1","Bas",0,0,[0,False,""],[0,0,0,0,[],"Bas"],0] #[vitessex,vitessey,posx,posy,idsprite,sprite,orientation,d,d,[Epee],[Fleche],compteurDegat]
Ennemi=[]
bloque_y=[]
bloque_x=[]
cpt=0
bloquer=[]
for i in range(0,20*20):
    bloquer.append([])

rectangle = 1
idmessage = 0

sprite_att=[]
coffre1=False
attendre = False
attendre_principal = False
premier_passage = False
listeitem=[]
joueur_touche=False
listecassable=[]
listechangement=[]
inventaire=[0,0]
#accueil()
affiche_terrain(nommap)
frame()


canvas.pack()
canvas.focus_set()
canvas.bind("<Key>", vitesse)
canvas.bind("<KeyRelease>", stop)
        
fenetre.mainloop()
    
