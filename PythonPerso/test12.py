#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from random import *
import os
        
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
            est_coffre=(num=="05" or num=="06" or num=="07" or num=="08")
            est_porte=(num=="12" or num=="15" or num=="16")
            ouvert=False
            if num =="00":
                for monitem in listechangement:
                    if nom_bis==monitem[2]  and monitem[0]==i*16 and monitem[1]==j and (monitem[4]=="05" or monitem[4]=="06" or monitem[4]=="07" or monitem[4]=="08"):
                        if monitem[5]==1:
                            nom="./spriteObjet/objet"+"04"
                            placer(nom,(i*16),j,1)
 
                        else:
                            nom="./spriteObjet/objet"+"02"
                            listeitem.append([monitem[4],i*16,j,0,0,[]])
                            placer(nom,(i*16),j,2)

            else:
                if est_coffre:              
                    for monitem in listechangement:
                        if nom_bis==monitem[2]  and monitem[0]==i*16 and monitem[1]==j:
                            nom="./spriteObjet/objet"+"04"
                            placer(nom,(i*16),j,2)
                            ouvert=True

                    if(not(ouvert)):
                        nom="./spriteObjet/objet"+"02"
                        listeitem.append([num,i*16,j,0,0,[]]) #[numeroItem,posx,posy,cpt,etat,[spriteID]]
                        placer(nom,(i*16),j,2)

                elif est_porte :
                    porte_ouverte=False
                    for monitem in listechangement:
                        if nom_bis==monitem[2] and monitem[0]==i*16 and monitem[1]==j and est_porte:
                            porte_ouverte=True
                            listeitem.append([num,i*16,j,0,1,[]])
                            
                    if(not(porte_ouverte)):            
                        listeitem.append([num,i*16,j,0,0,[]])
                        nom="./spriteObjet/objet"+num
                        placer(nom,(i*16),j,2)                        
                            
                else:
                    if num!="18":
                        listeitem.append([num,i*16,j,0,0,[]])
                        nom="./spriteObjet/objet"+num
                        placer(nom,(i*16),j,2)
                    else :
                        listeitem.append([num,i*16,j,0,1,[]])
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
    liste=[0,0,x,y,[],nom+"B1","Bas",0,int(lignes[0][8]),int(lignes[1][4]),int(lignes[2][8]),0] #[vitessex,vitessey,posx,posy,[sprite],fichier,orientation,cpt,vitesse,vie,dommage]
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
    

def placer(nom,x,y,option): #0=Transparent, 1=bloquer, 2=item, 3 =objet
    global bloque_x
    global bloque_y
    global bloque_num
    global listeitem
    global listeobjet
    
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()
    fig=0
    
    if (option!=0 and option!=3):
        bloque_x.append(x)
        bloque_y.append(y)
        num=nom[len(nom)-2]+nom[len(nom)-1]
        bloque_num.append(num)
        bloquer[x/32+y/32*20].append(x)
        bloquer[x/32+y/32*20].append(y)

    for ligne in lignes:
        for i in range (0,16):
            if ligne[i]!="0":           
                fig=couleur(ligne[i],val_x,val_y)
                if(option==2 and len(listeitem)!=0):
                    listeitem[len(listeitem)-1][5].append(fig)
                elif(option==3 and len(listeobjet)!=0):
                    listeobjet[len(listeobjet)-1][3].append(fig)
                
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
    global nommap2
    
    change=(mon_perso[2]+32>640 or mon_perso[2]<0 or mon_perso[3]+32>640 or mon_perso[3]<0)

    if (mon_perso[2]+32>640):
        mapx+=1
        mon_perso[2]=0
        
    elif(mon_perso[2]<0):
        mapx-=1
        mon_perso[2]=640-32

    elif(mon_perso[3]<0):
        mapy+=1
        mon_perso[3]=640-32
  
    elif(mon_perso[3]+32>640):
        mapy-=1
        mon_perso[3]=0
        
    if change:
        Ennemi=[]
        mon_perso[10]=[0,0,0,0,[],""]
        efface_bloque()
        efface_listeitem()
        nommap2="map"+str(mapx)+"-"+str(mapy)
        nommap="./map/map"+str(mapx)+"-"+str(mapy)
        affiche_terrain(nommap)    
	mouvement_perso()


def efface_bloque():
    global bloque_x
    global bloque_y
    global bloque_num
    
    bloque_x=[]
    bloque_y=[]
    bloque_num=[]


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
        
def couleur(num,val_x,val_y):
    hexa=""
    if num=="1":
        hexa="#0a650a" #vert
    elif num=="2":
        hexa="black" #noir
    elif num=="3":
        hexa="blue" #bleu
    elif num=="4":
        hexa="#808180" #gris
    elif num=="5":
        hexa="#614919" #marron
    elif num=="6":
        hexa="red" #rouge 
    elif num=="7":
        hexa="#d4a566" #beige
    elif num=="8":
        hexa="#0dac07" #vertClaire
    elif num=="9":
        hexa="white" #Blanc
    elif num=="A":
        hexa="#6d5331" #MarronClaire
    elif num=="B":
        hexa="#383837" #NOIRCLAIRE(OMBRE)
    elif num=="C":
        hexa="#e3e570" #JAUNECLAIRE
    elif num=="D": 
        hexa="#b2d5f6" #BleuClaire
        
    if num!="0":
        fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill=hexa,outline="")
        return fig
    
def placer_fleche(nom,x,y,sprite):
    efface(sprite)
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in range(0,16):
            if ligne[i]!="0":           
                fig=couleur(ligne[i],val_x,val_y)
                sprite.append(fig)
                
            val_x+=2
        val_y+=2
        val_x=x
    fichier.close()
        
def placer_attaque(num,val_x,val_y):
    global sprite_att
    if num!="0":           
        fig=couleur(num,val_x,val_y)
        sprite_att.append(fig)
        
def ramasse_objet():
    global inventaire
    global listeobjet
    global mon_perso
    global nommap2

    posx=mon_perso[2]
    posy=mon_perso[3]
    i=0
    ramasse=False
    
    for E in listeobjet:
            if E[1]>=posx and E[1]<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
                ramasse=True
                break
            elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
                ramasse=True
                break
            elif E[1]>=posx and E[1]<posx+31 and E[2]>=posy and E[2]<posy+31:
                ramasse=True
                break
            elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]>=posy and E[2]<posy+31:
                ramasse=True
                break
            i+=1
    if ramasse:
        num=E[0]
        if E[0]=="00":
            inventaire[4]+=1
            print inventaire
        elif E[0]=="01":
            inventaire[4]+=5
            print inventaire
        elif E[0]=="02":
            inventaire[5]+=5
            print inventaire
        elif E[0]=="03":
            inventaire[1]+=3
            if inventaire[1]>10:
                inventaire[1]=10
            print inventaire
        elif E[0]=="04":
            inventaire[0]+=1
            print inventaire
        efface(E[3])
        del listeobjet[i]
              
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

        for i in range(0,len(Ennemi)):
            if Ennemi[i][9]<=0:
                item_aleatoire(Ennemi[i][2],Ennemi[i][3])
                efface.append(i)
        mort(efface)
        
        if mon_perso[9][1]:
            if mon_perso[9][0]==0:
                if mon_perso[9][2]=="Epee":
                    aff_attaque()
                    couper_herbe()
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
            
        for E in Ennemi:
            mouvement_ennemi(E)
        
        if(len(Ennemi)>0):             
            if mon_perso[9][1] and (mon_perso[10][1]==0 and mon_perso[10][0]==0):
                toucher(mon_perso)
            elif mon_perso[10][0]!=0 or mon_perso[10][1]!=0:
                toucher_fleche(mon_perso[10])
            
        for liste in listeitem:
            if(liste[3]>0):
                compt(liste)
        
        canvas.after(30,frame)
        
def teleportation():
    global mon_perso
    global listeitem
    global Ennemi
    global nommap2
    global nommap

    if mon_perso[6]=="Haut":
        posx=mon_perso[2]
        posy=mon_perso[3]+16
    else:
        posx=mon_perso[2]
        posy=mon_perso[3]
    tp=False
    for liste in listeitem:
        est_porte=(liste[0]=="12" or liste[0]=="15" or liste[0]=="16" or liste[0]=="17" or liste[0]=="18")
        nom=("./tp/"+nommap2+"."+liste[0]+"."+str(liste[1])+"."+str(liste[2]))     
        if os.path.isfile(nom) and liste[4]==1 and est_porte:
            
            if liste[1]>=posx and liste[1]<posx+31 and liste[2]+31>=posy and liste[2]+31<posy+5:
                tp=True
                break
            elif liste[1]+31>=posx and liste[1]+31<posx+31 and liste[2]+31>=posy and liste[2]+31<posy+5:
                tp=True
                break
            elif liste[1]>=posx and liste[1]<posx+16 and liste[2]>=posy and liste[2]<posy+5:
                tp=True
                break
            elif liste[1]+31>=posx and liste[1]+31<posx+31 and liste[2]>=posy and liste[2]<posy+5:
                tp=True           
                break

    if tp:
        fichier=open(nom,"r")
        lignes=fichier.readlines()
        nommap2=lignes[0][:len(lignes[0])-1]
        mon_perso[2]=int(lignes[1])
        mon_perso[3]=int(lignes[2])
        
        canvas.delete("all")
        Ennemi=[]
        mon_perso[10]=[0,0,0,0,[],""]
        efface_bloque()
        efface_listeitem()
        nommap="./map/"+nommap2
        affiche_terrain(nommap)    
	mouvement_perso()

def bloquer_fleche(entite):
    global bloque_x
    global bloque_y
    global mon_perso
    global bloque_num


    for i in range(len(bloque_x)):
        if bloque_num[i]!="40":
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
        efface(entite[4])
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
    global inventaire
    touche=False

    if mon_perso[6]=="Haut":
        posx=mon_perso[2]
        posy=mon_perso[3]+16
    else:
        posx=mon_perso[2]
        posy=mon_perso[3]
        
    for E in Ennemi:
        if(E[6]=="Haut"):
            posx2=E[2]
            posy2=E[3]+16
        else:
            posx2=E[2]
            posy2=E[3]
            
        if posx2>=posx and posx2<posx+31 and posy2+31>=posy and posy2+16<posy+31:
            touche=True
            inventaire[1]-=E[10]
            print inventaire
            break
        elif posx2+31>=posx and posx2+31<posx+31 and posy2+16>=posy and posy2+16<posy+31:
            touche=True
            inventaire[1]-=E[10]
            print inventaire
            break       
        elif posx2>=posx and posx2<posx+31 and posy2>=posy and posy2<posy+31:
            touche=True
            inventaire[1]-=E[10]
            print inventaire
            break   
        elif posx2+31>=posx and posx2+31<posx+31 and posy2>=posy and posy2<posy+31:
            touche=True
            inventaire[1]-=E[10]
            print inventaire
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
        for E in Ennemi:
            if E[2]>=posx and E[2]<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                effaces.append(E)
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                effaces.append(E)               
            elif E[2]>=posx and E[2]<posx+31 and E[3]>=posy and E[3]<posy+31:
                effaces.append(E)            
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]>=posy and E[3]<posy+31:
                effaces.append(E)
           
    if(len(effaces)>0):
        mon_perso[10]=[0,0,0,0,[],"Bas"]
        efface(fleche[4])
        for E in effaces:
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
            del effaces[0]

def couper_herbe():
	global listeitem
	global mon_perso
	effaces=[]	
	
	posx=mon_perso[2]
	posy=mon_perso[3]
        sprite="./spriteSurface/bloc05"
        i=0
        
        if mon_perso[6]=="Haut" or mon_perso[6]=="Bas":
            if mon_perso[6]=="Haut":
                posx=mon_perso[2]
                posy=mon_perso[3]-16
        
            if mon_perso[6]=="Bas":
                posx=mon_perso[2]
                posy=mon_perso[3]+16
            
            for E in listeitem:
                if E[0]=="09":
                    if E[1]>=posx and E[1]<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]>=posx and E[1]<posx+31 and E[2]>=posy and E[2]<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]>=posy and E[2]<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                i+=1
                    
        if mon_perso[6]=="Droite" or mon_perso[6]=="Gauche":
            if mon_perso[6]=="Gauche":
                posx=mon_perso[2]-16
                posy=mon_perso[3]
 
            if mon_perso[6]=="Droite":
                posx=mon_perso[2]+16
                posy=mon_perso[3]

            for E in listeitem:
                if E[0]=="09":
                    if E[1]>=posx and E[1]<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]>=posx and E[1]<posx+31 and E[2]>=posy and E[2]<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]>=posy and E[2]<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                i+=1
        nul=[]
    
	for i in range(0, len(bloque_x)-1):
		for j in effaces:
			if (bloque_x[i] == j[1] and bloque_y[i] == j[2]):
				nul.append(i)
                                break
        if len(nul)!=0:
            bouger_sprite(mon_perso[4],mon_perso[5],mon_perso[2],mon_perso[3])
            for n in range(0,len(nul)):
                del bloque_x[nul[len(nul)-1]]
                del bloque_y[nul[len(nul)-1]]
                del nul[len(nul)-1]

def item_aleatoire(posx,posy):
    global listeobjet
    chiffre=randint(0,1)
    if chiffre==0 :
        chiffre=randint(0,10)
        if chiffre % 3==0:
            chiffre=randint(0,3)
            if chiffre==0:
                listeobjet.append(["01",posx,posy,[]])
                placer("./item/item01",posx,posy,3)
            elif chiffre==1 or chiffre==2:
                listeobjet.append(["03",posx,posy,[]])
                placer("./item/item03",posx,posy,3)
                
        elif chiffre % 2==0:
            chiffre=randint(0,1)
            if chiffre==0:
                listeobjet.append(["00",posx,posy,[]])
                placer("./item/item00",posx,posy,3)
            elif chiffre==1:
                listeobjet.append(["04",posx,posy,[]])
                placer("./item/item04",posx,posy,3)
            
def toucher(entite):

    global Ennemi
    effaces=[]

    if entite[6]=="Haut" or entite[6]=="Bas":
        if entite[6]=="Haut":
            posx=entite[2]
            posy=entite[3]-16
        
        if entite[6]=="Bas":
            posx=entite[2]
            posy=entite[3]+16
            
        for E in Ennemi:
            if E[2]>=posx and E[2]<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                effaces.append(E)
                
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                effaces.append(E)
                
            elif E[2]>=posx and E[2]<posx+31 and E[3]>=posy and E[3]<posy+31:
                effaces.append(E)
                
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]>=posy and E[3]<posy+31:
                effaces.append(E)
                
    if entite[6]=="Droite" or entite[6]=="Gauche":
        if entite[6]=="Gauche":
            posx=entite[2]-16
            posy=entite[3]
            
        if entite[6]=="Droite":
            posx=entite[2]+16
            posy=entite[3]

            
        for E in Ennemi:
            if E[2]>=posx and E[2]<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                effaces.append(E)
                
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                effaces.append(E)
                
            elif E[2]>=posx and E[2]<posx+31 and E[3]>=posy and E[3]<posy+31:
                effaces.append(E)
                
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]>=posy and E[3]<posy+31:
                effaces.append(E)
                
    if(len(effaces)>0):
        for E in effaces:
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
            del effaces[0]

            
                    
def mouvement_perso():
    global mon_perso
    global inventaire
           
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
    teleportation()
    if len(inventaire)>0:
        ramasse_objet()

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
    global listeobjet
    listeitem=[]
    listeobjet=[]

def efface_item(liste):
    for i in range(0,len(liste[5])):
        canvas.delete(liste[5][0])
        del liste[5][0]

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
            listechangement.append([liste[1],liste[2],nommap,0,liste[0],1])
            placer("./spriteObjet/objet"+liste[0],liste[1],liste[2],0)
            if liste[0]=="05":
                inventaire[4]+=1
                print inventaire[0]
            elif liste[0]=="06":
                inventaire[4]+=5
                print inventaire[0]
            elif liste[0]=="07":
                inventaire[5]+=1

            
    if (liste[0]=="12" or liste[0]=="16" or liste[0]=="15") and inventaire[5]>0 and liste[4]!=1:
        
        inventaire[5]-=1
        print liste[1]
        print liste[2]
        listechangement.append([liste[1],liste[2],nommap,mapy,liste[0],1])
        
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
                
    if liste[0]=="A":
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
    
    posx=mon_perso[2]+16
    posy=mon_perso[3]+16

    for liste in listeitem:
        
        if mon_perso[6]=="Bas":
            if mon_perso[3]+33>=liste[2] and mon_perso[3]+33<=liste[2]+32 and posx>liste[1] and posx<liste[1]+32:
                interaction(liste)
                break
                
        elif mon_perso[6]=="Haut":
            if mon_perso[3]+16>=liste[2]and mon_perso[3]+16<=liste[2]+32 and posx>liste[1] and posx<liste[1]+32:
                interaction(liste)
                break


        elif mon_perso[6]=="Gauche":
            if mon_perso[2]-1>=liste[1] and mon_perso[2]-1<=liste[1]+32 and posy>=liste[2] and posy<liste[2]+32:
                interaction(liste)
                break

        elif mon_perso[6]=="Droite":
            if mon_perso[2]+33>=liste[1] and mon_perso[2]+33<=liste[1]+32 and posy>liste[2] and posy<liste[2]+32:
                interaction(liste)
                break


    

fenetre = Tk()

canvas = Canvas(fenetre, width=640, height=639, background="black")
mapx=1
mapy=1
nommap="./map/map1-1"
nommap2="map1-1"
deplacement=0
inventaire=[0,10,True,True,0,0]#[fleche,vie,Epee,Arc,Gold,clef]
mon_perso=[0,0,320,400,[],"./spritePerso/PersoB1","Bas",0,inventaire,[0,False,""],[0,0,0,0,[],"Bas"],0] #[vitessex,vitessey,posx,posy,idsprite,sprite,orientation,d,[Inventaire],[Epee],[Fleche],compteurDegat]
Ennemi=[]
bloque_y=[]
bloque_x=[]
bloque_num=[]
cpt=0
bloquer=[]

for i in range(0,20*20):
    bloquer.append([])

rectangle = 1
idmessage = 0

sprite_att=[]
listeobjet=[]
coffre1=False
attendre = False
attendre_principal = False
premier_passage = False
listeitem=[]
joueur_touche=False
listecassable=[]
listechangement=[]
#accueil()
affiche_terrain(nommap)
frame()


canvas.pack()
canvas.focus_set()
canvas.bind("<Key>", vitesse)
canvas.bind("<KeyRelease>", stop)
        
fenetre.mainloop()
    
