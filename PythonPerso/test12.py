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
    affiche_ennemi(nommap)


def affiche_obj(nom):
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
            est_porte=(num=="12" or num=="15" or num=="16" or num=="17")
            ouvert=False
            if num =="00":
                for monitem in listechangement:
                    if nom_bis==monitem[2]  and monitem[0]==i*16 and monitem[1]==j and (monitem[4]=="05" or monitem[4]=="06" or monitem[4]=="07" or monitem[4]=="08"):
                        if monitem[5]==1:
                            nom="./spriteObjet/objet"+"04"
                            listeitem.append(["04",i*16,j,0,1,[]])
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
                            listeitem.append(["04",i*16,j,0,1,[]])
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
                    if num=="18" or num=="38" or num=="13":
                        listeitem.append([num,i*16,j,0,1,[]])
                        if num=="38" or num=="13":
                            nom="./spriteObjet/objet"+num
                            placer(nom,(i*16),j,0)
                            
                    else :
                        if num=="19" or num=="20":
                            listeitem.append([num,i*16,j,0,1,[]])
                            if interrupteur==1 and num=="20":
                                num+="bis"
                        elif num=="21" and interrupteur==1:
                            listeitem.append([num,i*16,j,0,0,[]])
                            num+="bis"
                        else:
                            listeitem.append([num,i*16,j,0,0,[]])
                        nom="./spriteObjet/objet"+num
                        placer(nom,(i*16),j,2)
            i+=2
        j+=32
    fichier.close()

def affiche_surf(nom):
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
    create_HUD()
    

def placer(nom,x,y,option): #0=Transparent, 1=bloquer, 2=item, 3 =objet
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()
    fig=0
    
    if (option!=0 and option!=3):
        bloque_x.append(x)
        bloque_y.append(y)
        bloque_num.append(nom)
        bloque.append([x,y,nom])

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
        Ennemi[:]=[]
        mon_perso[10]=[0,0,0,0,[],""]
        efface_bloque()
        efface_listeitem()
        nommap2="map"+str(mapx)+"-"+str(mapy)
        if(os.path.isfile("./map/"+nommap2)):
            nommap="./map/map"+str(mapx)+"-"+str(mapy)
        else:
            nommap="./map/bug"
            mon_perso[2]=224
            mon_perso[3]=224
        affiche_terrain(nommap)    
	mouvement_perso()
        verifie_interrupteur()


def efface_bloque():
    bloque_x[:]=[]
    bloque_y[:]=[]
    bloque_num[:]=[]


def bloquer_entite(val_x, val_y,entite):
    est_bloquer=False

    for i in range(len(bloque_x)):
        if(entite[2]>=bloque_x[i] and entite[2]<=bloque_x[i]+31):
            if( entite[3]+16>=bloque_y[i] and  entite[3]+16<=bloque_y[i]+31): #Coin Haut gauche
                entite[3]=val_y
                entite[2]=val_x
                est_bloquer=True
                break
               
            elif( entite[3]+31>=bloque_y[i] and  entite[3]+31<=bloque_y[i]+31): #Coin Bas gauche
                entite[3]=val_y
                entite[2]=val_x
                est_bloquer=True
                break
                
        if( entite[2]+31>=bloque_x[i] and  entite[2]+32<=bloque_x[i]+31):
            if( entite[3]+31>=bloque_y[i] and entite[3]+31<=bloque_y[i]+31): #Coin Bas Droite
                entite[3]=val_y
                entite[2]=val_x
                est_bloquer=True
                break
            
            elif( entite[3]+16>=bloque_y[i] and  entite[3]+16<=bloque_y[i]+31): #Coin Haut Droite
                entite[3]=val_y
                entite[2]=val_x
                est_bloquer=True
                break
            
    if not est_bloquer and entite!=mon_perso:
        for E in Ennemi:
            if(entite[2]>=E[2] and entite[2]<=E[2]+31 and entite!=E and entite!=E):
                if( entite[3]>=E[3] and  entite[3]<=E[3]+31): #Coin Haut gauche
                    entite[3]=val_y
                    entite[2]=val_x
                    break
                
                elif( entite[3]+31>=E[3] and  entite[3]+31<=E[3]+31): #Coin Bas gauche
                    entite[3]=val_y
                    entite[2]=val_x
                    break
                
            if( entite[2]+31>=E[2] and  entite[2]+32<=E[2]+31 and entite!=E and entite!=E):
                if( entite[3]+31>=E[3] and entite[3]+31<=E[3]+31): #Coin Bas Droite
                    entite[3]=val_y
                    entite[2]=val_x
                    break
            
                elif( entite[3]>=E[3] and  entite[3]<=E[3]+31): #Coin Haut Droite
                    entite[3]=val_y
                    entite[2]=val_x
                    break
                
    if(entite[3]>620 or entite[3]<-8 or entite[2]>620 or entite[2]<-8):
        entite[3]=val_y
        entite[2]=val_x
        
def interrupteur_epee(direction):
        if True:
            if direction=="Haut":
                posx=mon_perso[2]
                posy=mon_perso[3]-16
        
            if direction=="Bas":
                posx=mon_perso[2]
                posy=mon_perso[3]+16
                
            if mon_perso[6]=="Gauche":
                posx=mon_perso[2]-16
                posy=mon_perso[3]
 
            if mon_perso[6]=="Droite":
                posx=mon_perso[2]+16
                posy=mon_perso[3]
            
            for E in listeitem:
                if E[0]=="21" or E[0]=="21bis":
                    if E[1]>=posx and E[1]<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
		        active_interrupteur()
                    elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
		        active_interrupteur()
                    elif E[1]>=posx and E[1]<posx+31 and E[2]>=posy and E[2]<posy+31:
                        active_interrupteur()
                    elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]>=posy and E[2]<posy+31:
                        active_interrupteur()
                        
def aff_attaque():
    x=mon_perso[2]
    y=mon_perso[3]
    fichier = open("./Attaque/epee",'r')
    lignes  = fichier.readlines()
    efface(sprite_att)
    if mon_perso[7]==0:
        mon_perso[9][1]=False
    
    else:
        efface(mon_perso[4])
        
        if mon_perso[7]==1:
            touche_interrupteur=True
        else:
            touche_interrupteur=False
        
        if mon_perso[6]=="Bas":
            
            num=0*96+96-mon_perso[7]*32
            for i in range (0,32):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                y+=2
            if touche_interrupteur:
                interrupteur_epee("Bas")
                
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
            if touche_interrupteur:
                interrupteur_epee("Haut")
                
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
            if touche_interrupteur:
                interrupteur_epee("Droite")
                
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
            if touche_interrupteur:
                interrupteur_epee("Gauche")


        mon_perso[7]-=1
    
def aff_arc():

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
            if fleche[1]==0 and fleche[0]==0 and mon_perso[7]==3:
                fleche[1]=8
                fleche[2]=mon_perso[2]
                fleche[3]=mon_perso[3]
                fleche[5]="Bas"
                inventaire[0]-=1
                create_HUD()
            
                
        elif mon_perso[6]=="Haut":
            num=16
            for i in range (0,16):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32                
                y+=2
            if fleche[1]==0 and fleche[0]==0 and mon_perso[7]==3:
                fleche[1]=-8
                fleche[2]=mon_perso[2]
                fleche[3]=mon_perso[3]
                fleche[5]="Haut"
                inventaire[0]-=1
                create_HUD()
                
        elif mon_perso[6]=="Droite":
            num=48
            for i in range (0,16):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                y+=2
            if fleche[1]==0 and fleche[0]==0 and mon_perso[7]==3:
                fleche[0]=8
                fleche[2]=mon_perso[2]
                fleche[3]=mon_perso[3]
                fleche[5]="Droite"
                inventaire[0]-=1
                create_HUD()
                
        elif mon_perso[6]=="Gauche":
            num=32
            for i in range (0,16):
                ligne=lignes[i+num]
                for j in range(0,16):
                    placer_attaque(ligne[j],x,y)
                    x+=2
                x-=32
                y+=2
            if fleche[1]==0 and fleche[0]==0 and mon_perso[7]==3:
                fleche[0]=-8
                fleche[2]=mon_perso[2]
                fleche[3]=mon_perso[3]
                fleche[5]="Gauche"
                inventaire[0]-=1
                create_HUD()


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

    elif num=="E":
        hexa="#261f2f" #bleu/foncéé/gris
    elif num=="F":
        hexa="#c66f04" #orange   

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
    if num!="0":           
        fig=couleur(num,val_x,val_y)
        sprite_att.append(fig)
        
def ramasse_objet():

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
        if E[0]=="00" and inventaire[4]<FLECHE_MAX:
            inventaire[4]+=1
        elif E[0]=="01":
            inventaire[4]+=5
        elif E[0]=="02":
            inventaire[5]+=5
        elif E[0]=="03":
            inventaire[1]+=3
            if inventaire[1]>VIE_MAX:
                inventaire[1]=VIE_MAX
        elif E[0]=="04":
            inventaire[0]+=1
        efface(E[3])
        del listeobjet[i]
        create_HUD()
              
def frame():
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
            if mon_perso[9][1]:
                toucher(mon_perso)
            if mon_perso[10][0]!=0 or mon_perso[10][1]!=0:
                toucher_fleche(mon_perso[10])
            
        for liste in listeitem:
            if(liste[3]>0):
                compt(liste)
        
        canvas.after(30,frame)
        
def teleportation():
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
        est_porte=(liste[0]=="12" or liste[0]=="15" or liste[0]=="16" or liste[0]=="17" or liste[0]=="18" or liste[0]=="38" or liste[0]=="13")
        nom=("./tp/"+nommap2+"."+liste[0]+"."+str(liste[1])+"."+str(liste[2]))     
        if os.path.isfile(nom) and liste[4]==1 and est_porte:
            
            if liste[1]>=posx and liste[1]<posx+31 and liste[2]+31>=posy and liste[2]+31<posy+5:
                tp=True
                num=liste[0]
                break
            elif liste[1]+31>=posx and liste[1]+31<posx+31 and liste[2]+31>=posy and liste[2]+31<posy+5:
                tp=True
                num=liste[0]
                break
            elif liste[1]>=posx and liste[1]<posx+16 and liste[2]>=posy and liste[2]<posy+5:
                tp=True
                num=liste[0]
                break
            elif liste[1]+31>=posx and liste[1]+31<posx+31 and liste[2]>=posy and liste[2]<posy+5:
                tp=True
                num=liste[0]
                break

    if tp:
        fichier=open(nom,"r")
        lignes=fichier.readlines()
        mon_perso[2]=int(lignes[1])
        mon_perso[3]=int(lignes[2])
        if num!="38":
            nommap2=lignes[0][:len(lignes[0])-1]
            canvas.delete("all")
            mon_perso[10]=[0,0,0,0,[],""]
            efface_bloque()
            efface_listeitem()
            nommap="./map/"+nommap2
            Ennemi[:]=[]
            affiche_terrain(nommap)    
	    mouvement_perso()
            verifie_interrupteur()

def interrupteur_boucle(liste,num):
    fichier = open("./spriteObjet/objet"+num,'r')
    lignes  = fichier.readlines()
    val_x=liste[1]
    val_y=liste[2]
    for ligne in lignes:
        for i in range(0,16):
            if ligne[i]!="0":           
                fig=couleur(ligne[i],val_x,val_y)
                liste[5].append(fig)
            val_x+=2
        val_y+=2
        val_x=liste[1]

    fichier.close()

def verifie_interrupteur():
    if interrupteur==1:
        for liste in listeitem:
            if liste[0]=="19" and liste[4]==1:
                for i in range (0,len(bloque_x)):
                    if bloque_x[i]==liste[1] and bloque_y[i]==liste[2]:
                        del bloque_x[i]
                        del bloque_y[i]
                        del bloque_num[i]
                        break
                liste[4]=0
                efface(liste[5])
                interrupteur_boucle(liste,"19bis")
                    
            if liste[0]=="20" and liste[4]==0:
                bloque_x.append(liste[1])
                bloque_y.append(liste[2])
                bloque_num.append("./spriteObjet/objet20")
                liste[4]=1
                efface(liste[5])
                interrupteur_boucle(liste,"20bis")

    elif interrupteur==0:
        for liste in listeitem:
            if liste[0]=="19" and  liste[4]==0:
                    bloque_x.append(liste[1])
                    bloque_y.append(liste[2])
                    bloque_num.append("./spriteObjet/objet19")
                    liste[4]=1
                    efface(liste[5])
                    interrupteur_boucle(liste,"19")
                
            if liste[0]=="20" and liste[4]==1:
                for i in range (0,len(bloque_x)):
                    if bloque_x[i]==liste[1] and bloque_y[i]==liste[2]:
                        del bloque_x[i]
                        del bloque_y[i]
                        del bloque_num[i]
                        break
                    
                liste[4]=0
                efface(liste[5])
                interrupteur_boucle(liste,"20")
                
def active_interrupteur():
    global interrupteur
    if interrupteur==0 and not(verifie_bloquer()) :
        interrupteur+=1
        for liste in listeitem:
            if liste[0]=="21":
                efface(liste[5])
                placer("./spriteObjet/objet21bis",liste[1],liste[2],0)
        verifie_interrupteur()
    elif interrupteur>0 and not(verifie_bloquer()):
        interrupteur=0
        for liste in listeitem:
            if liste[0]=="21":
                efface(liste[5])
                placer("./spriteObjet/objet21",liste[1],liste[2],0)
        verifie_interrupteur()

def verifie_bloquer():
    posx=mon_perso[2]
    posy=mon_perso[3]+16
    est_bloque=False
    for E in listeitem:
        if E[0]=="20" or E[0]=="20bis" or E[0]=="19" or E[0]=="19bis":
            if E[1]>=posx and E[1]<posx+31 and E[2]+31>=posy and E[2]+31<posy+16:
		est_bloque=True
                break
            elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]+31>=posy and E[2]+31<posy+16:
		est_bloque=True
                break
            elif E[1]>=posx and E[1]<posx+31 and E[2]>=posy and E[2]<posy+16:
		est_bloque=True
                break
            elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]>=posy and E[2]<posy+16:
		est_bloque=True
                break
    return est_bloque
            
def bloquer_fleche(entite):
    global interrupteur
    for i in range(len(bloque_x)):
        if bloque_num[i]!="./spriteDecor/bloc40" and bloque_num[i]!="./spriteDecor/bloc54" and bloque_num[i]!="./spriteDecor/bloc55" :
            if(entite[2]>=bloque_x[i] and entite[2]<=bloque_x[i]+31):
                if( entite[3]+16>=bloque_y[i] and  entite[3]+16<=bloque_y[i]+31): #Coin Haut gauche
                    efface(entite[4])
                    mon_perso[10]=[0,0,0,0,[],""]
                    if bloque_num[i]=="./spriteObjet/objet21" or bloque_num[i]=="./spriteObjet/objet21bis":
                        active_interrupteur()
                    break
               
                elif( entite[3]+31>=bloque_y[i] and  entite[3]+31<=bloque_y[i]+31): #Coin Bas gauche
                    efface(entite[4])
                    mon_perso[10]=[0,0,0,0,[],""]
                    if bloque_num[i]=="./spriteObjet/objet21" or bloque_num[i]=="./spriteObjet/objet21bis":
                        active_interrupteur()
                    break
                
            if( entite[2]+31>=bloque_x[i] and  entite[2]+32<=bloque_x[i]+31):
                if( entite[3]+31>=bloque_y[i] and entite[3]+31<=bloque_y[i]+31): #Coin Bas Droite
                    efface(entite[4])
                    mon_perso[10]=[0,0,0,0,[],""]
                    if bloque_num[i]=="./spriteObjet/objet21" or bloque_num[i]=="./spriteObjet/objet21bis":
                        active_interrupteur()
                    break
            
                elif( entite[3]+16>=bloque_y[i] and  entite[3]+16<=bloque_y[i]+31): #Coin Haut Droite
                    efface(entite[4])
                    mon_perso[10]=[0,0,0,0,[],""]
                    if bloque_num[i]=="./spriteObjet/objet21" or bloque_num[i]=="./spriteObjet/objet21bis":
                        active_interrupteur()
                    break
                
    if(entite[3]>620 or entite[3]<-8 or entite[2]>620 or entite[2]<-8):
        efface(entite[4])
        mon_perso[10]=[0,0,0,0,[],""]
        
def mort(effaces):
    for i in range(0,len(effaces)):
        efface(Ennemi[effaces[len(effaces)-1]][4])
        del Ennemi[effaces[len(effaces)-1]]
        del effaces[len(effaces)-1]
    
def recule(E):
    if E[3]>mon_perso[3] and E[2]>mon_perso[2]:
        E[0]=4
        E[1]=4
    elif E[3]<=mon_perso[3] and E[2]>mon_perso[2]:
        E[0]=4
        E[1]=-4
    elif E[3]<=mon_perso[3] and E[2]<=mon_perso[2]:
        E[0]=-4
        E[1]=-4
    elif E[3]>mon_perso[3] and E[2]<=mon_perso[2]:
        E[0]=-4
        E[1]=4
def joueur_toucher():
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
            if mon_perso[11]<=0:
                inventaire[1]-=E[10]
            recule(E)
            break
        elif posx2+31>=posx and posx2+31<posx+31 and posy2+16>=posy and posy2+16<posy+31:
            touche=True
            if mon_perso[11]<=0:
                inventaire[1]-=E[10]
            recule(E)
            break       
        elif posx2>=posx and posx2<posx+31 and posy2>=posy and posy2<posy+31:
            touche=True
            if mon_perso[11]<=0:
                inventaire[1]-=E[10]
            recule(E)
            break   
        elif posx2+31>=posx and posx2+31<posx+31 and posy2>=posy and posy2<posy+31:
            touche=True
            if mon_perso[11]<=0:
                inventaire[1]-=E[10]
            recule(E)
            break       
                
    if(touche):
            sprite=""
            E=mon_perso
	    for j in range (0,len(mon_perso[5])-2) :
		sprite+=mon_perso[5][j]
                
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
            create_HUD()

def toucher_fleche(fleche):
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
	effaces=[]	
	
	posx=mon_perso[2]
	posy=mon_perso[3]
        sprite="./spriteSurface/bloc05"
        i=0
        
        if True:
            if mon_perso[6]=="Haut":
                posx=mon_perso[2]
                posy=mon_perso[3]-16
        
            if mon_perso[6]=="Bas":
                posx=mon_perso[2]
                posy=mon_perso[3]+16
                
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
    
	for i in range(0, len(bloque_x)):
		for j in effaces:
			if (bloque_x[i] == j[1] and bloque_y[i] == j[2]):
				nul.append(i)
                                break
        if len(nul)!=0:
            bouger_sprite(mon_perso[4],mon_perso[5],mon_perso[2],mon_perso[3])
            for n in range(0,len(nul)):
                del bloque_x[nul[len(nul)-1]]
                del bloque_y[nul[len(nul)-1]]
                del bloque_num[nul[len(nul)-1]]
                del nul[len(nul)-1]

def item_aleatoire(posx,posy):
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
    global rectangle
    global idmessage
    global attendre
    global message_active

    touche=event.keysym
    if(not attendre and not message_active):
        if mon_perso[11]<=0:
            if touche=="Up":
                mon_perso[1]=-8
            if touche=="Down":
                mon_perso[1]=8
            if touche=="Right":
                mon_perso[0]=8
            if touche=="Left":
                mon_perso[0]=-8

        if(touche=="b"):
            attaque("Epee")
            mon_perso[11]=0
        elif(touche=="c" and inventaire[0]>0):
            attaque("Arc")
            mon_perso[11]=0
        if touche=="Escape":
            menu()
        if(touche=="a"):
            interagir()
            
    elif (attendre):
        if touche=="Escape":
            attendre=False
            lemenu[2][1]=280
            lemenu[2][0]=485
            lemenu[3]=0
            efface(lemenu[2][2])
            efface(lemenu[0])
            efface(lemenu[1])
            frame()
            
        if touche=="Up":
            efface(lemenu[2][2])
            lemenu[2][1]-=28
            lemenu[3]-=1
            if(lemenu[2][1]<280):
                lemenu[2][1]+=28*3
                lemenu[3]=2
            placer_curseur()
        if touche=="Down":
            efface(lemenu[2][2])
            lemenu[2][1]+=28
            lemenu[3]+=1
            if(lemenu[2][1]>336):
                lemenu[2][1]-=28*3
                lemenu[3]=0
            placer_curseur()
        if touche=="Return":
            efface(lemenu[2][2])
            efface(lemenu[0])
            efface(lemenu[1])
            attendre=False
            if lemenu[3]==0:
                sauvegarder()
            elif lemenu[3]==2:
                charger()
            elif lemenu[3]==1:
                fenetre.destroy()
                attendre=True
            frame()
            
    elif message_active:
        if(touche=="a"):
            message_active = False
	    canvas.delete(rectangle)
	    canvas.delete(idmessage)


def menu():
    
    global attendre
    mon_fichier = open("menu", "r")
    message = mon_fichier.read()	
    attendre = True
    lemenu[0].append(canvas.create_rectangle(440, 190, 560, 410,width=1, fill='white'))
    lemenu[0].append(canvas.create_rectangle(450, 200, 550, 400,width=5, fill='white'))
    lemenu[1].append(canvas.create_text(500, 300, text = message))
    mon_fichier.close()
    placer_curseur()
    
def placer_curseur():
    fichier=open("curseur","r")
    lignes=fichier.readlines()
    val_x=lemenu[2][0]
    val_y=lemenu[2][1]
    for ligne in lignes:
        for num in ligne:
            if num=="1":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="")
                lemenu[2][2].append(fig)
            val_x+=2

        val_y+=2
        val_x=lemenu[2][0]
    fichier.close()

def attaque(arme):
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
    global coffre1

    if(nommap2=="tuto3"):
        if(coffre1==False):
            if(not(len(Ennemi)>0)):                 
                coffre1=True
                listeitem.append(["07",256,224,0,0,[]])
                listechangement.append([256,224,nommap,0,"07",0])
                placer("./spriteObjet/objet02",256,224,2)


def bouger_sprite(sprite_pos,nom,x,y):
    efface(sprite_pos)
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()

    for ligne in lignes:
        for i in ligne:
            if i!="0":           
                fig=couleur(i,val_x,val_y)
                sprite_pos.append(fig)
                
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

    listeitem[:]=[]
    listeobjet[:]=[]
    listecassable[:]=[]

def efface_item(liste):
    for ele in liste[5]:
        canvas.delete(ele)
        del ele

def interaction(liste):
    global idmessage
    global rectangle
    global attendre
    global nommap
    global nommap2
    global message_active
    global VIE_MAX

    numero_eff=[]
    existe=False
    
    if liste[0]=="05" or liste[0]=="06" or liste[0]=="07" or liste[0]=="08":
        if liste[4]!=1:
            liste[3]=10
            liste[4]=1
            for item in listechangement:
                if item[0]==liste[1] and item[1]==liste[2] and item[2]==nommap:
                    item[5]=1
                    existe=True
                    break
            if not existe:
                listechangement.append([liste[1],liste[2],nommap,0,liste[0],1])
            placer("./spriteObjet/objet"+liste[0],liste[1],liste[2],0)
            if liste[0]=="05":
                inventaire[4]+=1
            elif liste[0]=="06":
                inventaire[4]+=5
            elif liste[0]=="07":
                inventaire[5]+=1
            elif liste[0]=="08":
                set_coeur()
                inventaire[1]=VIE_MAX
            create_HUD()

            
    if (liste[0]=="12" or liste[0]=="16" or liste[0]=="15" or liste[0]=="17") and inventaire[5]>0 and liste[4]!=1:
        
        inventaire[5]-=1
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
        create_HUD()

                
    else:
        nom=("./messages/"+nommap2+"."+liste[0]+"."+str(liste[1])+"."+str(liste[2]))
        if os.path.isfile(nom):
	    mon_fichier = open(nom, "r")
	    message = mon_fichier.read()	
	    message_active = True
	    rectangle = canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white')
	    idmessage = canvas.create_text(320, 590, text = message)
        
def interagir():
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


def create_HUD():
    
    for id in HUD:
        for id2 in id:
            canvas.delete(id2)
    HUD[:]=[[],[]]
                
    HUD[0].append(canvas.create_text(55,30, text = "x" + str(mon_perso[8][1]),fill='white'))
    HUD[0].append(canvas.create_text(150 ,30, text = "x" + str(mon_perso[8][4]),fill='white'))
    HUD[0].append(canvas.create_text(250 ,30, text = "x" + str(mon_perso[8][0]),fill='white'))
    HUD[0].append(canvas.create_text(350 ,30, text = "x" + str(mon_perso[8][5]),fill='white'))
    HUD[0].append(canvas.create_text(450 ,30, text = "\"c\"",fill='white'))
    HUD[0].append(canvas.create_text(550 ,30, text = "\"b\"",fill='white'))
    placerHUD()

def placerHUD():

    HUD[1].append(canvas.create_rectangle(5,5,635,45,fill='',outline='white'))
    placer_HUD2("./item/item05",7,7)
    placer_HUD2("./item/item00",107,7)
    placer_HUD2("./item/item04",207,7)
    placer_HUD2("./item/item02",307,7)
    placer_HUD2("./item/item06",407,10)
    placer_HUD2("./item/item07",507,10)
        
def placer_HUD2(nom,x,y):
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()
    fig=0
    for ligne in lignes:
        for i in range (0,16):
            if ligne[i]!="0":           
                fig=couleur(ligne[i],val_x,val_y)
                HUD[1].append(fig)
            val_x+=2
        val_y+=2
        val_x=x
    fichier.close()
def set_coeur():
    global VIE_MAX
    VIE_MAX+=10

def set_fleche():
    global FLECHE_MAX
    FLECHE_MAX+=20
    
def sauvegarder():
    fichier=open("./save/save1","w")
    for change in listechangement:
        fichier.write("[")
        for e in change:
            fichier.write(str(e))
            fichier.write(",")
        fichier.write("]\n")
    fichier.write(nommap+","+nommap2+","+str(mon_perso[2])+","+str(mon_perso[3])+","+str(mapx)+","+str(mapy)+","+str(interrupteur)+","+"]"+"\n")
    fichier.write("[")
    for i in inventaire:
        fichier.write(str(i))
        fichier.write(",")
    fichier.write("]\n")
    for i in Ennemi:
        mot="["+str(i[2])+","+str(i[3])+","+str(i[9])+","+i[5]+","+str(i[8])+","+str(i[10])+",]\n"
        fichier.write(mot)  
    fichier.close()

def charger():
    global nommap
    global nommap2
    global mapx
    global mapy
    global interrupteur

    listechangement[:]=[]
    cpt=0
    fichier=open("./save/save1")
    lignes=fichier.readlines()
    est_changement=False
    arret=False
    finit_changement=False
    finit_inventaire=False
    finit_option2=False
    finit_option1=False
    i=0
    mot=""
    inventaire[:]=[]
    Ennemi2=[]
    for ligne in lignes:
        if finit_option1:
            finit_option2=True
            
        if not finit_changement:
            for c in ligne: 
                if c!="\n" and est_changement==False and c!="[":
                    finit_changement=True
                    break
                elif c=="[":
                    listechangement.append([])
                    mot=""
                    est_changement=True
                elif c=="]":
                    cpt=0
                    i+=1
                    est_changement=False
                    
                elif c==",":
                    if(cpt==0 or cpt==1 or cpt==3 or cpt==5):
                        listechangement[i].append(int(mot))
                    else:
                        listechangement[i].append(mot)
 
                    mot=""
                    cpt+=1

                elif est_changement:
                    mot+=c
                    
                              
        if not finit_option1 and finit_changement:
            est_changement=True
            for c in ligne:
                if c==",":
                    if cpt==0:
                        nommap=mot
                    elif cpt==1:
                        nommap2=mot
                    elif cpt==2:
                        mon_perso[2]=int(mot)
                    elif cpt==3:
                        mon_perso[3]=int(mot)
                    elif cpt==4:
                        mapx=int(mot)
                    elif cpt==5:
                        mapy=int(mot)
                    elif cpt==6:
                        interrupteur=int(mot)
                    mot=""
                    est_changement=True
                    cpt+=1
                    
                elif c=="]":
                    finit_option1=True
                    cpt=0
                    i=0
                    mot=""
                    break
                
                elif est_changement:
                    mot+=c

        if finit_option2 and finit_changement and not finit_inventaire:
            for c in ligne: 
                if c=="[":
                    mot=""
                elif c=="]":
                    finit_inventaire=True
                    cpt=0
                    i=0
                    mon_perso[8]=inventaire
                    mot=""
                    break
                elif c==",":
                    if(cpt==0 or cpt==1 or cpt==4 or cpt==5):
                        inventaire.append(int(mot))
                    else:
                        if mot=="True":
                            inventaire.append(True)
                        elif mot=="False":
                            inventaire.append(False)
                        else:
                            inventaire.append(mot)
                    mot=""
                    cpt+=1

                else:
                    mot+=c
        elif finit_inventaire:
            for c in ligne: 
                if c!="\n" and est_changement==False and c!="[":
                    finit_ennemi=True
                    break
                elif c=="[":
                    Ennemi2.append([])
                    mot=""
                    est_changement=True
                elif c=="]":
                    cpt=0
                    i+=1
                    est_changement=False
                    
                elif c==",":
                    if(cpt!=3):
                        Ennemi2[i].append(int(mot))
                    else:
                        Ennemi2[i].append(mot)
 
                    mot=""
                    cpt+=1

                elif est_changement:
                    mot+=c
    Ennemi[:]=[]
    mon_perso[10]=[0,0,0,0,[],"Bas"]
    efface_bloque()
    efface_listeitem()
    canvas.delete("all")
    affiche_terrain(nommap)
    copie=[]
    for j in range(0,len(Ennemi2)):
        copie.append(Ennemi[j])
        copie[j][2]=Ennemi2[j][0]
        copie[j][3]=Ennemi2[j][1]
        copie[j][5]=Ennemi2[j][3]
        copie[j][9]=Ennemi2[j][2]
        copie[j][8]=Ennemi2[j][4]
        copie[j][10]=Ennemi2[j][5]
    for e in Ennemi:
        efface(e[4])
    Ennemi[:]=copie
    create_HUD()
    mouvement_perso()
    verifie_interrupteur()
                        

fenetre = Tk()
canvas = Canvas(fenetre, width=640, height=640, background="black")

mapx=1
mapy=1

nommap="./map/tuto1"
nommap2="tuto1"

inventaire=[30,10,True,True,0,0]#[fleche,vie,Epee,Arc,Gold,clef]
mon_perso=[0,0,320,400,[],"./spritePerso/PersoB1","Bas",0,inventaire,[0,False,""],[0,0,0,0,[],"Bas"],0] #[vitessex,vitessey,posx,posy,idsprite,sprite,orientation,d,[Inventaire],[Epee],[Fleche],compteurDegat]

Ennemi=[]

bloque_y=[]
bloque_x=[]
bloque_num=[]

bloque=[]

HUD=[[],[]]
    
lemenu=[[],[],[485,280,[]],0] # Menu,Option,Curseur,Num_Option

rectangle = 0
idmessage = 0
interrupteur=0

message_active=False
coffre1=False
attendre = False
listeitem=[]

sprite_att=[]
listeobjet=[]
listecassable=[]
listechangement=[]

VIE_MAX=10
FLECHE_MAX=40

affiche_terrain(nommap)
verifie_interrupteur()
frame()


canvas.pack()
canvas.focus_set()
canvas.bind("<Key>", vitesse)
canvas.bind("<KeyRelease>", stop)
        
fenetre.mainloop()


# REGLER MONSTRE, sauvegarde(booleen evenement+Herbe)+ REGLER BLOCAGE(pas activé interrupteur si dessus)+ COMMENCER FICHIER NOMBRE MAGIQUE+ MAPPIN MAISON+ VIDE+HITBOX.