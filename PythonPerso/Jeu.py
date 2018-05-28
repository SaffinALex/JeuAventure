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
            est_coffre=(num=="05" or num=="06" or num=="07" or num=="08" or num=="70")
            est_porte=(num=="12" or num=="15" or num=="16" or num=="17" or num=="11")
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
    liste=[0,0,x,y,[],nom+"B1","Bas",0,int(lignes[0][8]),int(lignes[1][4:]),int(lignes[2][8]),0] #[vitessex,vitessey,posx,posy,[sprite],fichier,orientation,cpt,vitesse,vie,dommage]
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
    if not titre and not introactive:
        create_HUD()
    

def placer(nom,x,y,option): #0=Transparent, 1=bloquer, 2=item, 3 =objet
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()
    fig=0
    
    if (option!=0 and option!=3):
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
    
    change=(mon_perso[2]+32>640 or mon_perso[2]<0 or mon_perso[3]+32>640 or mon_perso[3]<60)

    if (mon_perso[2]+32>640):
        mapx+=1
        mon_perso[2]=0
        
    elif(mon_perso[2]<0):
        mapx-=1
        mon_perso[2]=640-32

    elif(mon_perso[3]<60):
        mapy+=1
        mon_perso[3]=600
 
  
    elif(mon_perso[3]+32>640):
        mapy-=1
        mon_perso[3]=60
        
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
            nommap2="bug"
            mon_perso[2]=224
            mon_perso[3]=224
        affiche_terrain(nommap)    
	mouvement_perso()
        verifie_interrupteur()


def efface_bloque():
    bloque[:]=[]

def bloquer_entite(val_x, val_y,entite):
    est_bloquer=False
    bloque_x=False
    bloque_y=False
    for liste in bloque:
        if entite[0]!=0:
            if(entite[2]>=liste[0] and entite[2]<=liste[0]+31):
                if( val_y+16>=liste[1] and  val_y+16<=liste[1]+31): #Coin Haut gauche
                    est_bloquer=True
                    bloque_x=True
                    break
               
                elif( val_y+31>=liste[1] and  val_y+31<=liste[1]+31): #Coin Bas gauche
                    bloque_x=True
                    est_bloquer=True
                    break
                
            if( entite[2]+31>=liste[0] and  entite[2]+32<=liste[0]+31):
                if( val_y+31>=liste[1] and val_y+31<=liste[1]+31): #Coin Bas Droite
                    est_bloquer=True
                    bloque_x=True
                    break
                
                elif( val_y+16>=liste[1] and  val_y+16<=liste[1]+31): #Coin Haut Droite
                    est_bloquer=True
                    bloque_x=True
                    break

    for liste in bloque:
        if entite[1]!=0:
            if(val_x>=liste[0] and val_x<=liste[0]+31):
                if( entite[3]+16>=liste[1] and  entite[3]+16<=liste[1]+31): #Coin Haut gauche
                    est_bloquer=True
                    bloque_y=True
                    break
               
                elif( entite[3]+31>=liste[1] and  entite[3]+31<=liste[1]+31): #Coin Bas gauche
                    bloque_y=True
                    est_bloquer=True
                    break
                
            if( val_x+31>=liste[0] and  val_x+32<=liste[0]+31):
                if( entite[3]+31>=liste[1] and entite[3]+31<=liste[1]+31): #Coin Bas Droite
                    est_bloquer=True
                    bloque_y=True
                    break
                
                elif( entite[3]+16>=liste[1] and  entite[3]+16<=liste[1]+31): #Coin Haut Droite
                    est_bloquer=True
                    bloque_y=True
                    break

    if bloque_x:
        entite[2]=val_x
    if bloque_y:
        entite[3]=val_y
            
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
    for liste in bloque:
        if(entite[2]>=liste[0] and entite[2]<=liste[0]+31):
            if( entite[3]+16>=liste[1] and  entite[3]+16<=liste[1]+31): #Coin Haut gauche
                est_bloquer=True
                bloque_x=True
                break
               
            elif( entite[3]+31>=liste[1] and  entite[3]+31<=liste[1]+31): #Coin Bas gauche
                bloque_x=True
                est_bloquer=True
                break
                
        if( entite[2]+31>=liste[0] and  entite[2]+32<=liste[0]+31):
            if( entite[3]+31>=liste[1] and entite[3]+31<=liste[1]+31): #Coin Bas Droite
                est_bloquer=True
                bloque_x=True
                break
            
            elif( entite[3]+16>=liste[1] and  entite[3]+16<=liste[1]+31): #Coin Haut Droite
                est_bloquer=True
                bloque_x=True
                break
            
    if(entite[3]>620 or entite[3]<48 or entite[2]>620 or entite[2]<-8):
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
        hexa="#b81e1e" #rouge 
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
    elif num=="G":
        hexa="#5a2a10" #pourpre
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
        if E[0]=="00":
            inventaire[4]+=5
        elif E[0]=="01":
            inventaire[4]+=10
        elif E[0]=="02":
            inventaire[5]+=1
        elif E[0]=="03":
            inventaire[1]+=3
            if inventaire[1]>VIE_MAX:
                inventaire[1]=VIE_MAX
        elif E[0]=="04"  and inventaire[0]<FLECHE_MAX :
            inventaire[0]+=1
        efface(E[3])
        del listeobjet[i]
        create_HUD()
              
def frame():
    efface=[]
    if(not attendre and not achat and not message_active and not fin and not titre and not introactive):
        changeMap()
        joueur_toucher()

        joueur_mort()
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
            
        for E in Ennemi:
            mouvement_ennemi(E)

        if(not mon_perso[9][1]):
            mouvement_perso()
        
        if(len(Ennemi)>0):             
            if mon_perso[9][1]:
                toucher(mon_perso)
            if mon_perso[10][0]!=0 or mon_perso[10][1]!=0:
                toucher_fleche(mon_perso[10])
            
        for liste in listeitem:
            if(liste[3]>0):
                compt(liste)
        evenement()
        canvas.after(30,frame)
    if titre:
        ecran_titre()
    if introactive:
        introduction()
        
def teleportation():
    global nommap2
    global nommap
    global mapx
    global mapy


    posx=mon_perso[2]+16
    posy=mon_perso[3]+30
        
    tp=False
    for liste in listeitem:
        est_porte=(liste[0]=="11" or liste[0]=="12" or liste[0]=="15" or liste[0]=="16" or liste[0]=="17" or liste[0]=="18" or liste[0]=="38" or liste[0]=="13")
        nom=("./tp/"+nommap2+"."+liste[0]+"."+str(liste[1])+"."+str(liste[2]))     
        if os.path.isfile(nom) and liste[4]==1 and est_porte:
            if posx>=liste[1] and posx<=liste[1]+31 and posy>=liste[2] and posy<=liste[2]+32:
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
            if nommap2[:3]=="map":
                num=nommap2[3:]
                if num[0]=="-":
                    mapx=int(num[1])*-1
                    if num[3]=="-":
                        mapy=int(num[4])*-1
                    else:
                        mapy=int(num[3])
                else:
                    mapx=int(num[0])
                    if num[2]=="-":
                        mapy=int(num[3])*-1
                    else:
                        mapy=int(num[2])
                nommap2="map"+str(mapx)+"-"+str(mapy)
            canvas.delete("all")
            mon_perso[10]=[0,0,0,0,[],""]
            efface_bloque()
            efface_listeitem()
            nommap="./map/"+nommap2
            Ennemi[:]=[]
            affiche_terrain(nommap)    
	    mouvement_perso()
            verifie_interrupteur()
            sequence_joueur[:]=[]

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
                for b in bloque:
                    if b[0]==liste[1] and b[1]==liste[2]:
                        bloque.remove(b)
                        break
                    
                liste[4]=0
                efface(liste[5])
                interrupteur_boucle(liste,"19bis")
                    
            if liste[0]=="20" and liste[4]==0:
                bloque.append([liste[1],liste[2],"./spriteObjet/objet20"])
                liste[4]=1
                efface(liste[5])
                interrupteur_boucle(liste,"20bis")

    elif interrupteur==0:
        for liste in listeitem:
            
            if liste[0]=="19" and  liste[4]==0:
                bloque.append([liste[1],liste[2],"./spriteObjet/objet19"])
                liste[4]=1
                efface(liste[5])
                interrupteur_boucle(liste,"19")
                
            if liste[0]=="20" and liste[4]==1:
                for b in bloque:
                    if b[0]==liste[1] and b[1]==liste[2]:
                        bloque.remove(b)
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
            if E[1]>=posx and E[1]<=posx+31 and E[2]+31>=posy and E[2]+31<=posy+16:
		est_bloque=True
                break
            elif E[1]+31>=posx and E[1]+31<=posx+31 and E[2]+31>=posy and E[2]+31<=posy+16:
		est_bloque=True
                break
            elif E[1]>=posx and E[1]<=posx+31 and E[2]>=posy and E[2]<=posy+16:
		est_bloque=True
                break
            elif E[1]+31>=posx and E[1]+31<=posx+31 and E[2]>=posy and E[2]<=posy+16:
		est_bloque=True
                break
    return est_bloque
            
def bloquer_fleche(entite):
    global interrupteur
    for liste in bloque:
        if liste[2]!="./spriteDecor/bloc40" and liste[2]!="./spriteDecor/bloc54" and liste[2]!="./spriteDecor/bloc55" :
            if(entite[2]>=liste[0] and entite[2]<=liste[0]+31):
                if( entite[3]+16>=liste[1] and  entite[3]+16<=liste[1]+31): #Coin Haut gauche
                    efface(entite[4])
                    mon_perso[10]=[0,0,0,0,[],""]
                    if liste[2]=="./spriteObjet/objet21" or liste[2]=="./spriteObjet/objet21bis":
                        active_interrupteur()
                    break
               
                elif( entite[3]+31>=liste[1] and  entite[3]+31<=liste[1]+31): #Coin Bas gauche
                    efface(entite[4])
                    mon_perso[10]=[0,0,0,0,[],""]
                    if liste[2]=="./spriteObjet/objet21" or liste[2]=="./spriteObjet/objet21bis":
                        active_interrupteur()
                    break
                
            if( entite[2]+31>=liste[0] and  entite[2]+32<=liste[0]+31):
                if( entite[3]+31>=liste[1] and entite[3]+31<=liste[1]+31): #Coin Bas Droite
                    efface(entite[4])
                    mon_perso[10]=[0,0,0,0,[],""]
                    if liste[2]=="./spriteObjet/objet21" or liste[2]=="./spriteObjet/objet21bis":
                        active_interrupteur()
                    break
            
                elif( entite[3]+16>=liste[1] and  entite[3]+16<=liste[1]+31): #Coin Haut Droite
                    efface(entite[4])
                    mon_perso[10]=[0,0,0,0,[],""]
                    if liste[2]=="./spriteObjet/objet21" or liste[2]=="./spriteObjet/objet21bis":
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
    posx=E[2]
    posy=E[3]
    if E[3]>mon_perso[3] and E[2]>mon_perso[2]:
        E[1]=6
        mouvement_ennemi(E)
        if E[3]==posy:
            E[0]=-6
            E[1]=0
    elif E[3]<=mon_perso[3] and E[2]>mon_perso[2]:
        E[1]=-6
        mouvement_ennemi(E)
        if E[3]==posy:
            E[0]=6
            E[1]=0
    elif E[3]<=mon_perso[3] and E[2]<=mon_perso[2]:
        E[1]=-6
        mouvement_ennemi(E)
        if E[3]==posy:
            E[0]=-6
            E[1]=0
    elif E[3]>mon_perso[3] and E[2]<=mon_perso[2]:
        E[1]=6
        mouvement_ennemi(E)
        if E[3]==posy:
            E[0]=6
            E[1]=0
def joueur_toucher():
    touche=False
    if mon_perso[6]=="Haut":
        posx=mon_perso[2]
        posy=mon_perso[3]+16
    else:
        posx=mon_perso[2]
        posy=mon_perso[3]+16
        
    for E in Ennemi:
        if(E[6]=="Haut"):
            posx2=E[2]
            posy2=E[3]+16
        else:
            posx2=E[2]
            posy2=E[3]
        if E[11]==0:
            if posx2>=posx and posx2<posx+32 and posy2>=posy and posy2<posy+16:
                touche=True
                if mon_perso[11]<=0:
                    inventaire[1]-=E[10]
                ennemi=E
                recule(E)
                break
            elif posx2+32>=posx and posx2+32<posx+32 and posy2>=posy and posy2<posy+16:
                touche=True
                if mon_perso[11]<=0:
                    inventaire[1]-=E[10]
                ennemi=E
                recule(E)
                break       
            elif posx2>=posx and posx2<posx+32 and posy2+32>=posy and posy2+32<posy+16:
                touche=True
                if mon_perso[11]<=0:
                    inventaire[1]-=E[10]
                ennemi=E
                recule(E)
                break   
            elif posx2+32>=posx and posx2+32<posx+32 and posy2+32>=posy and posy2+32<posy+16:
                touche=True
                if mon_perso[11]<=0:
                    inventaire[1]-=E[10]
                ennemi=E
                recule(E)
                break
                
    if(touche):
            sprite=""
            E=mon_perso
	    for j in range (0,len(mon_perso[5])-2) :
		sprite+=mon_perso[5][j]
                
            E[11]=5
            if(E[6]=="Bas"):
                E[5]=sprite+"B4"            
            elif(E[6]=="Haut"):
                E[5]=sprite+"H4"
            elif(E[6]=="Droite"):
                E[5]=sprite+"D4"
            elif(E[6]=="Gauche"):
                E[5]=sprite+"G4"
            recule_perso(ennemi)
            create_HUD()
            
def recule_perso(E):
    posx=mon_perso[2]
    posy=mon_perso[3]
    if mon_perso[3]>E[3] and mon_perso[2]>E[2]:
        mon_perso[1]=+8
        mouvement_perso()
        mon_perso[1]=0
        if mon_perso[3]==posy:
            mon_perso[0]=-8
            mouvement_perso()
            mon_perso[0]=0
    elif mon_perso[3]<=E[3] and mon_perso[2]>E[2]:
        mon_perso[1]=-8
        mouvement_perso()
        mon_perso[1]=0
        if mon_perso[3]==posy:
            mon_perso[0]=8
            mouvement_perso()
            mon_perso[0]=0
    elif mon_perso[3]<=E[3] and mon_perso[2]<=E[2]:
        mon_perso[1]=-8
        mouvement_perso()
        mon_perso[1]=0
        if mon_perso[3]==posy:
            mon_perso[0]=-8
            mouvement_perso()
            mon_perso[0]=0
    elif mon_perso[3]>E[3] and mon_perso[2]<=E[2]:
        mon_perso[1]=8
        mouvement_perso()
        mon_perso[1]=0
        if mon_perso[3]==posy:
            mon_perso[0]=8
            mouvement_perso()
            mon_perso[0]=0
            
def mini_boss2(entite,fleche,liste):
    if entite[11]==5:
        if entite[6]=="Bas" and fleche[5]=="Bas":
            entite[9]-=1
            liste.append(entite)
        elif entite[6]=="Droite" and fleche[5]=="Droite":
            entite[9]-=1
            liste.append(entite)
        elif entite[6]=="Gauche" and fleche[5]=="Gauche":
            entite[9]-=1
            liste.append(entite)
        elif entite[6]=="Haut" and fleche[5]=="Haut":
            entite[9]-=1
            liste.append(entite)
        
def toucher_fleche(fleche):
    effaces=[]
    if fleche[0]!=0 or fleche[1]!=0:
        posx=fleche[2]
        posy=fleche[3]
        for E in Ennemi:
            if E[2]>=posx and E[2]<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss2(E,fleche,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss2(E,fleche,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
            elif E[2]>=posx and E[2]<posx+31 and E[3]>=posy and E[3]<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss2(E,fleche,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]>=posy and E[3]<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss2(E,fleche,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
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
                        listecassable.append([str(E[1]),str(E[2])])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]+31>=posy and E[2]+31<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        listecassable.append([str(E[1]),str(E[2])])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]>=posx and E[1]<posx+31 and E[2]>=posy and E[2]<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        listecassable.append([str(E[1]),str(E[2])])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                    elif E[1]+31>=posx and E[1]+31<posx+31 and E[2]>=posy and E[2]<posy+31:
		        effaces.append(E)
		        efface(E[5])
                        listecassable.append([str(E[1]),str(E[2])])
                        placer(sprite,E[1],E[2],0)
                        item_aleatoire(E[1],E[2])
		        del listeitem[i]
                i+=1
                    
	for liste in bloque:
            for j in effaces:
		if (liste[0] == j[1] and liste[1] == j[2]):
		    bloque.remove(liste)
                    break


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
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss(E,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
                
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss(E,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
                
            elif E[2]>=posx and E[2]<posx+31 and E[3]>=posy and E[3]<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss(E,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
                
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]>=posy and E[3]<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss(E,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
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
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss(E,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
                
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]+31>=posy and E[3]+31<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss(E,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
                    
            elif E[2]>=posx and E[2]<posx+31 and E[3]>=posy and E[3]<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss(E,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
                    effaces.append(E)
                    
            elif E[2]+31>=posx and E[2]+31<posx+31 and E[3]>=posy and E[3]<posy+31:
                if E[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
                    mini_boss(E,effaces)
                if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                    toucher_cristal(E)
                else:
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

def mini_boss(entite,liste):
    if entite[11]==5:
        if entite[6]=="Bas" and mon_perso[6]=="Bas" and mon_perso[3]<=entite[3]:
            entite[9]-=1
            liste.append(entite)
        elif entite[6]=="Droite" and mon_perso[6]=="Droite" and mon_perso[2]<=entite[2]:
            entite[9]-=1
            liste.append(entite)
        elif entite[6]=="Gauche" and mon_perso[6]=="Gauche" and mon_perso[2]>=entite[2]:
            entite[9]-=1
            liste.append(entite)
        elif entite[6]=="Haut" and mon_perso[6]=="Haut" and mon_perso[3]>=entite[3]:
            entite[9]-=1
            liste.append(entite)
                    
def mouvement_perso():
    val_x=mon_perso[2]
    val_y=mon_perso[3] 
    mon_perso[2]+=mon_perso[0]
    mon_perso[3]+=mon_perso[1]
    if mon_perso[11]>0:
        mon_perso[11]-=1
        # if mon_perso[11]==0:
        #     mon_perso[0]=0
        #     mon_perso[1]=0
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

def aleatoire(chiffre,mon_ennemi):
    diffx=mon_perso[2]-mon_ennemi[2]
    diffy=mon_perso[3]-mon_ennemi[3]
    if (not (-160<diffx<160 and -160<diffy<160)):
        chiffre=randint(0,4)
    
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
    if mon_ennemi[5][:32]=="./spriteEnnemi/ennemi10/ennemi10":
        mon_ennemi[7]=30
    else:
        mon_ennemi[7]=10
    	
def mouvement_ennemi(mon_ennemi):

    if(mon_ennemi[7]<=0):
        mon_ennemi[0]=0
        mon_ennemi[1]=0
        if mon_perso[2]<mon_ennemi[2]:
            chiffre=randint(0,2)
            if mon_perso[3]>mon_ennemi[3]:
                if chiffre==1:
                    aleatoire(2,mon_ennemi)
            else:
                if chiffre==1:
                    aleatoire(3,mon_ennemi)
            if chiffre==2:
                aleatoire(1,mon_ennemi)

        else:
            chiffre=randint(0,2)
            if mon_perso[3]>mon_ennemi[3]:
                if chiffre==1:
                    aleatoire(2,mon_ennemi)
            else:
                if chiffre==1:
                    aleatoire(3,mon_ennemi)
            if chiffre==2:
                aleatoire(0,mon_ennemi)

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
    global achat
    global introactive
    touche=event.keysym
    if(not attendre and not message_active and not achat and not titre):
        if touche=="z" or touche=="Z":
            mon_perso[1]=-8
        if touche=="s"or touche=="S":
            mon_perso[1]=8
        if touche=="d"or touche=="D":
            mon_perso[0]=8
        if touche=="q"or touche=="Q":
            mon_perso[0]=-8

        if(touche=="n" or touche=="N"):
            attaque("Epee")
            mon_perso[11]=0
        elif(touche=="k" or touche=="K" and inventaire[0]>0):
            attaque("Arc")
            mon_perso[11]=0
        if touche=="Escape" and not save_desactive:
            menu()
        if(touche=="space"):
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
                if titre:
                    introactive=True
                else:
                    sauvegarder()
            elif lemenu[3]==2:
                charger()
            elif lemenu[3]==1:
                fenetre.destroy()
                attendre=True
            frame()

    elif message_active:
        if(touche=="space"):
            if len(boss)>0:
                for i in boss:
                    canvas.delete(i)
                boss[:]=[]
                message_active=False
                frame()
    
            else:
                message_active = False
	        canvas.delete(rectangle)
	        canvas.delete(idmessage)
                frame()
    elif achat:
        selection_achat(touche)

def selection_achat(touche):
    global achat
    fichier=open("./menu/marchand2","r")
    lignes=fichier.readlines()

    if touche=="Up":
        efface(lemarchand[2][2])
        lemarchand[2][1]-=28
        lemarchand[3]-=1
        if(lemarchand[2][1]<240):
            lemarchand[2][1]+=28*6
            lemarchand[3]=5
        placer_curseurmarchand()
        canvas.delete(lemarchand[4])
        lemarchand[4]= canvas.create_text(320, 590,justify="center", text = lignes[lemarchand[3]])
        
    if touche=="Down":
        efface(lemarchand[2][2])
        lemarchand[2][1]+=28
        lemarchand[3]+=1
        if(lemarchand[2][1]>380):
            lemarchand[2][1]-=28*6
            lemarchand[3]=0
        placer_curseurmarchand()
        canvas.delete(lemarchand[4])
        lemarchand[4]= canvas.create_text(320, 590,justify="center", text = lignes[lemarchand[3]])
        
    if touche=="Return":
        if lemarchand[3]==0 and inventaire[4]>=300:
            set_coeur()
            inventaire[4]-=300
            inventaire[1]=VIE_MAX
        elif lemarchand[3]==1 and inventaire[4]>=100:
            set_fleche()
            inventaire[4]-=100
            inventaire[0]=FLECHE_MAX
        elif lemarchand[3]==2 and inventaire[4]>=2:
            inventaire[4]-=2
            inventaire[0]+=5
            if inventaire[0]>FLECHE_MAX:
                inventaire[0]=FLECHE_MAX
        elif lemarchand[3]==3 and inventaire[4]>=10:
            inventaire[4]-=10
            inventaire[1]+=10
            if inventaire[1]>VIE_MAX:
                inventaire[1]=VIE_MAX
        elif lemarchand[3]==4:
            canvas.delete(lemarchand[4])
            lemarchand[4]=canvas.create_text(320, 590,justify="center", text ="Je ne suis qu'un marchand itinérant.")
            
        elif lemarchand[3]==5:
            efface(lemarchand[2][2])
            efface(lemarchand[0])
            efface(lemarchand[1])
            canvas.delete(lemarchand[4])
            achat=False         
            frame()
        create_HUD()

def menu():
    
    global attendre
    if titre:
        mon_fichier = open("./menu/titre", "r")
    else:
        mon_fichier = open("./menu/menu", "r")
    message = mon_fichier.read()	
    attendre = True
    lemenu[0].append(canvas.create_rectangle(440, 190, 560, 410,width=1, fill='white'))
    lemenu[0].append(canvas.create_rectangle(450, 200, 550, 400,width=5, fill='white'))
    lemenu[1].append(canvas.create_text(500, 300, text = message))
    mon_fichier.close()
    placer_curseur()
    
def placer_curseur():
    fichier=open("./menu/curseur","r")
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
    if(touche=="z" or touche=="s" or touche=="S" or touche=="Z"):
        mon_perso[1]=0
    if(touche=="d" or touche=="q" or touche=="Q" or touche=="D" ):
        mon_perso[0]=0
        
def boss_phase3():
    global messageflamme4
    global message_active
    global save_desactive
    global cptboss
    global fin

    save_desactive=True

    if not messageflamme4:
            boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
            boss.append(canvas.create_text(320, 590, text = "Voix: Maintenant que le cristal n'est plus, cette île va disparaitre.\nTu dois fuir d'ici ! "))
            message_active=True
            messageflamme4=True
            cptboss=1000
    cptboss-=1
    for j in timer:
        canvas.delete(j)
    timer[:]=[]
    timer.append(canvas.create_rectangle(450, 70,650, 90,fill='white'))
    timer.append(canvas.create_text(550, 80, text = ("Destruction dans : " + str(cptboss/20) )))
    if cptboss==0:
        joueur_mort()
    elif cptboss==-101:
        canvas.delete("all")
        affiche_terrain("./map/end")
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Félicitation vous avez terminé le Jeu !"))
        fin=True

    elif nommap2=="detruit7":
        if 320<=mon_perso[2]<=352 and 416<=mon_perso[3]<=448:
            efface(mon_perso[4])
            placer("./spriteObjet/objet66",320,352,0)
            message_active=True
            boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
            boss.append(canvas.create_text(320, 590, text = "Homme Mystérieux: Bien,il est parti... \nCette Affaire est bien trop préoccupante...\nElle ne doit pas s'ébruiter."))
            cptboss=-100
    
def evenement():
    global coffre1
    global vague1
    global vague2
    global vague3
    global vague4
    global save_desactive
    global message_active
    global messageflamme1
    global messageflamme2
    global messageflamme3
    
    save_desactive=False
    coffrepris=False
    existe=False

    if nommap2=="temple1" and not messageflamme3:
            boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
            boss.append(canvas.create_text(320, 590, text = "Voix: Tu es parvenu jusqu'au temple... \n Maintenant continue ton chemin jusqu'au cristal. "))
            message_active=True
            messageflamme3=True
    if nommap2[:7]=="detruit":
            boss_phase3()
            
    if(nommap2=="tuto3"):
        if(coffre1==False):
            if(not(len(Ennemi)>0)):                 
                coffre1=True
                listeitem.append(["07",256,224,0,0,[]])
                listechangement.append([256,224,nommap,0,"07",0])
                placer("./spriteObjet/objet02",256,224,2)
                
    elif(nommap2=="temple6"):
        if (not vague1):
            save_desactive=True
            for liste in listechangement:
                if liste[4]=="07" and liste[2]==nommap:
                    coffrepris=True
                    break
            for liste in listeitem:
                if liste[0]=="63":
                    existe=True
            if (not coffrepris):
                if not existe:
                    listeitem.append(["63",160,320,0,0,[]])
                    placer("./spriteDecor/bloc63",160,320,2)  
                if(not(len(Ennemi)>0)):                 
                    vague1=True
                    listeitem.append(["07",256,224,0,0,[]])
                    listechangement.append([256,224,nommap,0,"07",0])
                    placer("./spriteObjet/objet02",256,224,2)
        else:
            for E in Ennemi:
                efface(E[4])
            Ennemi[:]=[]
            for liste in bloque:
                if liste[0]==160 and liste[1]==320:
                    bloque.remove(liste)
                    break
    
            for liste in listeitem:
                if liste[0]=="63":
                    efface(liste[5])
                    break
                
    elif(nommap2=="Manoir2"):
        if (not vague3):
            save_desactive=True
            for liste in listechangement:
                if liste[4]=="07" and liste[2]==nommap:
                    coffrepris=True
                    break
            for liste in listeitem:
                if liste[0]=="63":
                    existe=True
            if (not coffrepris):
                if not existe:
                    listeitem.append(["63",96,256,0,0,[]])
                    placer("./spriteDecor/bloc63",96,256,2)  
                if(not(len(Ennemi)>0)):                 
                    vague3=True
                    listeitem.append(["07",256,224,0,0,[]])
                    listechangement.append([256,224,nommap,0,"07",0])
                    placer("./spriteObjet/objet02",256,224,2)
        else:
            for E in Ennemi:
                efface(E[4])
            Ennemi[:]=[]
            for liste in bloque:
                if liste[0]==96 and liste[1]==256:
                    bloque.remove(liste)
                    break
    
            for liste in listeitem:
                if liste[0]=="63":
                    efface(liste[5])
                    break

    elif(nommap2=="Manoir1"):
        if (not vague4):
            save_desactive=True
            for liste in listechangement:
                if liste[4]=="07" and liste[2]==nommap:
                    coffrepris=True
                    break
            for liste in listeitem:
                if liste[0]=="63":
                    existe=True
            if (not coffrepris):
                if not existe:
                    listeitem.append(["63",416,320,0,0,[]])
                    placer("./spriteDecor/bloc63",416,320,2)  
                if(not(len(Ennemi)>0)):                 
                    vague4=True
                    listeitem.append(["07",256,288,0,0,[]])
                    listechangement.append([256,288,nommap,0,"07",0])
                    placer("./spriteObjet/objet02",256,288,2)
        else:
            for E in Ennemi:
                efface(E[4])
            Ennemi[:]=[]
            for liste in bloque:
                if liste[0]==416 and liste[1]==320:
                    bloque.remove(liste)
                    break
    
            for liste in listeitem:
                if liste[0]=="63":
                    efface(liste[5])
                    break
                
    elif nommap2=="Bois":
        active_bois()

    elif nommap2=="boss1":
        save_desactive=True
        combat_boss()
    elif nommap2=="boss" and mon_perso[3]<=320:
        actionne_final()
        save_desactive=True
        
    elif nommap2=="miniboss":
        if (not messageflamme1):
            boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
            boss.append(canvas.create_text(320, 590, text = "INTRUS INTRUS INTRUS ! DETRUIRE INTRUS !"))
            message_active=True
            messageflamme1=True
        elif (not messageflamme2):
            boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
            boss.append(canvas.create_text(320, 590, text = "Voix : Son point faible se trouve derriére son dos. \nProfite de sa lenteur pour l'attaquer au bon moment. "))
            message_active=True
            messageflamme2=True
            
        elif (not vague2):
            save_desactive=True
            for liste in listechangement:
                if liste[4]=="70" and liste[2]==nommap:
                    coffrepris=True
                    break
            for liste in listeitem:
                if liste[0]=="63":
                    existe=True
            if (not coffrepris):
                if not existe:
                    listeitem.append(["63",288,416,0,0,[]])
                    placer("./spriteDecor/bloc63",288,416,2)  
                if(not(len(Ennemi)>0)):                 
                    vague2=True
                    listeitem.append(["70",256,224,0,0,[]])
                    listechangement.append([256,224,nommap,0,"07",0])
                    placer("./spriteObjet/objet02",256,224,2)
        else:
            for E in Ennemi:
                efface(E[4])
            Ennemi[:]=[]
            for liste in bloque:
                if liste[0]==288 and liste[1]==416:
                    bloque.remove(liste)
                    break
            for liste in listeitem:
                if liste[0]=="63":
                    efface(liste[5])
                    break
                
def toucher_cristal(E):
    E[0]=0
    E[1]=0
    if vulnerable and E[11]<=0:
        E[9]-=1
        E[5]="./spriteEnnemi/ennemi09/ennemi09B4"
        E[11]=10
def actionne_final():
    global cptboss2
    global message_active
    global vulnerable
    global cptfinal
    global nommap2
    global nommap
    for j in timer:
        canvas.delete(j)
    timer[:]=[]
    if cptfinal==0:
        timer.append(canvas.create_rectangle(100, 550, 550, 625,fill='white'))
        timer.append(canvas.create_text(320, 590, text = ("Tu es donc parvenu jusqu'ici...")))
        message_active=True
        cptfinal+=1

    elif cptfinal==1:
        timer.append(canvas.create_rectangle(100, 550, 550, 625,fill='white'))
        timer.append(canvas.create_text(320, 590, text = ("T'affronter ici et maintenant ne serait qu'une perte de temps...")))
        message_active=True
        cptfinal+=1
        
    elif cptfinal==2:
        timer.append(canvas.create_rectangle(100, 550, 550, 625,fill='white'))
        timer.append(canvas.create_text(320, 590, text = ("Le rituel n'est pas complet, mais il est suffisant...")))
        for liste in listeitem:
            if liste[0]=="64":
                efface(liste[5])
                listeitem.append(["65",liste[1],liste[2],0,0,[]])
                placer("./spriteObjet/objet65",liste[1],liste[2],2)
                for E in bloque:
                    if E[0]==liste[1] and E[1]==liste[2]:
                        bloque.remove(E)
                        break
                listeitem.remove(liste)
                break
        message_active=True
        cptfinal+=1

    elif cptfinal==3:
        timer.append(canvas.create_rectangle(100, 550, 550, 625,fill='white'))
        timer.append(canvas.create_text(320, 590, text = ("Nous nous reverrons ! Si tu t'en sors vivant.")))
        for liste in listeitem:
            if liste[0]=="65":
                efface(liste[5])
                for E in bloque:
                    if E[0]==liste[1] and E[1]==liste[2]:
                        bloque.remove(E)
                        break
                listeitem.remove(liste)
                break
        placer("./spriteDecor/bloc63",320,352,1)
                
        message_active=True
        cptfinal+=1
    elif cptfinal==4:
        timer.append(canvas.create_rectangle(100, 550, 550, 625,fill='white'))
        timer.append(canvas.create_text(320, 590, text = ("Voix: Le cristal, tu dois le détruire ! \nLe rituel étant incomplet, le cristal aura besoin de temps \npour recharger sa magie.")))
        message_active=True
        cptfinal+=1
        
    elif cptfinal==5:
        cristal_vie=0
        for E in Ennemi:
            if E[5][:32]=="./spriteEnnemi/ennemi09/ennemi09":
                cristal_vie=E[9]
                break
        if cptboss2==0:
            if not vulnerable :
                boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
                boss.append(canvas.create_text(320, 590, text = "Le Cristal est Vulnérable ! Attaque le !"))
                message_active=True
                cptboss2=500
            else:
                cptboss2=1000
            
            vulnerable=not vulnerable

        timer.append(canvas.create_rectangle(20, 70,200, 90,fill='white'))
        timer.append(canvas.create_text(100, 80, text = ("Degat Cristal : " + str(cristal_vie) +"%" )))       
        if not vulnerable:
            timer.append(canvas.create_rectangle(450, 70,650, 90,fill='white'))
            timer.append(canvas.create_text(550, 80, text = ("Cristal Vulnérable Dans : " + str(cptboss2/20) )))
        else:
            timer.append(canvas.create_rectangle(450, 70,650, 90,fill='white'))
            timer.append(canvas.create_text(550, 80, text = ("Cristal Rechargé Dans : " + str(cptboss2/20) )))
        
        if cptboss2==500 or cptboss2==250 or cptboss2==750 or cptboss2==1000 and len(Ennemi)<10:
            chiffre=randint(0,4)
            if chiffre==0:
                ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",384,128)
                ajout_ennemi("./spriteEnnemi/ennemi02/ennemi02",256,128)
                ajout_ennemi("./spriteEnnemi/ennemi02/ennemi02",256,288)
                ajout_ennemi("./spriteEnnemi/ennemi03/ennemi03",384,288)
            elif chiffre==1:
                ajout_ennemi("./spriteEnnemi/ennemi02/ennemi02",256,128)
                ajout_ennemi("./spriteEnnemi/ennemi03/ennemi03",384,128)
                ajout_ennemi("./spriteEnnemi/ennemi02/ennemi02",256,288)
                ajout_ennemi("./spriteEnnemi/ennemi03/ennemi03",384,288)
            elif chiffre==2:
                ajout_ennemi("./spriteEnnemi/ennemi02/ennemi02",256,128)
                ajout_ennemi("./spriteEnnemi/ennemi03/ennemi03",384,128)
                ajout_ennemi("./spriteEnnemi/ennemi08/ennemi08",384,288)
                ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",256,288)
            elif chiffre==3:
                ajout_ennemi("./spriteEnnemi/ennemi08/ennemi08",384,128)
                ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",256,128)
                ajout_ennemi("./spriteEnnemi/ennemi02/ennemi02",256,288)
                ajout_ennemi("./spriteEnnemi/ennemi03/ennemi03",384,288)
            else:
                ajout_ennemi("./spriteEnnemi/ennemi05/ennemi05",384,128)
                ajout_ennemi("./spriteEnnemi/ennemi01/ennemi01",256,128)
                ajout_ennemi("./spriteEnnemi/ennemi02/ennemi02",256,288)
                ajout_ennemi("./spriteEnnemi/ennemi03/ennemi03",384,288)

        cptboss2-=1
        for E in Ennemi:
            if cristal_vie==0:
                canvas.delete("all")
                nommap2="detruit1"
                nommap="./map/detruit1"
                Ennemi[:]=[]
                efface_listeitem()
                bloque[:]=[]
                affiche_terrain(nommap)
            
def combat_boss():
    global boss1
    global boss2
    global boss3
    global boss4
    global cptboss
    global message_active

    existe=False

    for j in timer:
        canvas.delete(j)
    timer[:]=[]
    timer.append(canvas.create_rectangle(450, 70,650, 90,fill='white'))
    timer.append(canvas.create_text(550, 80, text = ("Fin du Rituel dans : " + str(cptboss/20) )))
    
    if cptboss==2000:
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Voix: Tu dois te dépêcher ! "))
        message_active=True

    if cptboss==1500:
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Voix: Le temps s'écoule dépêche toi ! "))
        message_active=True

    if cptboss==500:
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Voix: Dans quelques secondes le rituel sera achevé !"))
        message_active=True
        
    if cptboss==0:
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Voix: C'est terminé..."))
        inventaire[1]=0
        boss1=False
        boss2=False
        boss3=False
        boss4=False
        message_active=True

    if cptboss<0:
        joueur_mort()

    if boss4:
        boss4=True
    elif boss3 and len(Ennemi)==0:
        for liste in bloque:
            if liste[0]==320 and liste[1]==96:
                bloque.remove(liste)
                break
        for liste in listeitem:
            if liste[0]=="63":
                efface(liste[5])
                listeitem.remove(liste)
                break
    elif boss2 and len(Ennemi)==0:
        for liste in bloque:
            if liste[0]==320 and liste[1]==192:
                bloque.remove(liste)
                break
        for liste in listeitem:
            if liste[0]=="63":
                efface(liste[5])
                listeitem.remove(liste)
                break
        if mon_perso[3]<=128:
            ajout_ennemi("./spriteEnnemi/ennemi05/ennemi05",200,150)
            ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",200,280)
            ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",500,532)
            listeitem.append(["63",320,96,0,0,[]])
            placer("./spriteDecor/bloc63",320,96,2)
            boss3=True
    elif boss1 and len(Ennemi)==0:
        for liste in bloque:
            if liste[0]==320 and liste[1]==384:
                bloque.remove(liste)
                break
        for liste in listeitem:
            if liste[0]=="63":
                efface(liste[5])
                listeitem.remove(liste)
                break
        if mon_perso[3]<=224:
            ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",200,280)
            ajout_ennemi("./spriteEnnemi/ennemi06/ennemi06",250,320)
            ajout_ennemi("./spriteEnnemi/ennemi08/ennemi08",500,320)
            ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",500,280)
            listeitem.append(["63",320,192,0,0,[]])
            placer("./spriteDecor/bloc63",320,192,2)
            boss2=True
            
    elif not boss1 and len(Ennemi)==0 and mon_perso[3]<=416:
        ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",250,500)
        ajout_ennemi("./spriteEnnemi/ennemi06/ennemi06",250,540)
        ajout_ennemi("./spriteEnnemi/ennemi06/ennemi06",500,500)
        ajout_ennemi("./spriteEnnemi/ennemi07/ennemi07",500,532)
        listeitem.append(["63",320,384,0,0,[]])
        placer("./spriteDecor/bloc63",320,384,2)
            
        boss1=True
    
    cptboss-=1
    
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
    if liste[0]=="05" or liste[0]=="06" or liste[0]=="07" or liste[0]=="08" or liste[0]=="70":
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
    global achat

    numero_eff=[]
    existe=False
    if liste[0]=="05" or liste[0]=="06" or liste[0]=="07" or liste[0]=="08" or liste[0]=="70":
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
                inventaire[4]+=10
            elif liste[0]=="06":
                inventaire[4]+=100
            elif liste[0]=="07":
                inventaire[5]+=1
            elif liste[0]=="08":
                set_coeur()
                inventaire[1]=VIE_MAX
            elif liste[0]=="70":
                inventaire[6]+=1
            create_HUD()

            
    if (liste[0]=="12" or liste[0]=="16" or liste[0]=="15" or liste[0]=="17") and inventaire[5]>0 and liste[4]!=1:
        
        inventaire[5]-=1
        listechangement.append([liste[1],liste[2],nommap,mapy,liste[0],1])
        
        for b in bloque:
            if(b[0]==liste[1] and b[1]==liste[2]):
                numero_eff.append(b)
                liste[4]=1
                efface_item(liste)

                
        for j in numero_eff:
            bloque.remove(j)
        
        create_HUD()
    if(liste[0]=="11" and liste[4]!=1 and inventaire[6]>0):
        inventaire[6]-=1
        listechangement.append([liste[1],liste[2],nommap,mapy,liste[0],1])
        for b in bloque:
            if(b[0]==liste[1] and b[1]==liste[2]):
                numero_eff.append(b)
                liste[4]=1
                efface_item(liste)

                
        for j in numero_eff:
            bloque.remove(j)
        create_HUD()
            
    if liste[0]=="49" and not achat :
        achat=True
        actionne_marchand()
    if liste[0]=="68" and nommap2=="Bois":
        message=dialogue_bois
	message_active = True
	rectangle = canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white')
	idmessage = canvas.create_text(320, 590, text = message)
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
            if mon_perso[3]+38>=liste[2] and mon_perso[3]+38<=liste[2]+32 and posx>liste[1] and posx<liste[1]+32:
                interaction(liste)
                break
                
        elif mon_perso[6]=="Haut":
            if mon_perso[3]+12>=liste[2]and mon_perso[3]+12<=liste[2]+32 and posx>liste[1] and posx<liste[1]+32:
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
    HUD[0].append(canvas.create_text(140 ,30, text = "x" + str(mon_perso[8][4]),fill='white'))
    HUD[0].append(canvas.create_text(230 ,30, text = "x" + str(mon_perso[8][0]),fill='white'))
    HUD[0].append(canvas.create_text(300 ,30, text = "x" + str(mon_perso[8][5]),fill='white'))
    HUD[0].append(canvas.create_text(400 ,30, text = "x" + str(mon_perso[8][6]),fill='white'))
    HUD[0].append(canvas.create_text(500 ,30, text = "\"k\"",fill='white'))
    HUD[0].append(canvas.create_text(580 ,30, text = "\"n\"",fill='white'))
    placerHUD()

def placerHUD():

    HUD[1].append(canvas.create_rectangle(5,5,635,45,fill='',outline='white'))
    placer_HUD2("./item/item05",7,7)
    placer_HUD2("./item/item00",87,7)
    placer_HUD2("./item/item04",177,7)
    placer_HUD2("./item/item02",267,7)
    placer_HUD2("./item/item09",357,10)    
    placer_HUD2("./item/item06",447,10)
    placer_HUD2("./item/item07",537,10)
        
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
    fichier.write("@\n")
    fichier.write("["+nommap+","+nommap2+","+str(mon_perso[2])+","+str(mon_perso[3])+","+str(mapx)+","+str(mapy)+","+str(interrupteur)+","+str(VIE_MAX)+","+str(FLECHE_MAX)+",]"+"\n")
    fichier.write("@\n")
    fichier.write("[")
    
    for i in inventaire:
        fichier.write(str(i))
        fichier.write(",")
    fichier.write("]\n")
    fichier.write("@\n")
    for i in Ennemi:
        mot=("["+str(i[2])+","+str(i[3])+","+str(i[9])+","+i[5]+","+str(i[8])+","+str(i[10])+",]\n")
        fichier.write(mot)
    fichier.write("@\n")
    for liste in listecassable:
        mot="["+str(liste[0])+","+str(liste[1])+",]\n"
        fichier.write(mot)
    fichier.write("@\n")
    fichier.write("["+str(coffre1)+","+str(vague1)+","+str(vague2)+","+str(vague3)+","+str(vague4)+","+str(messageflamme1)+","+str(messageflamme2)+","+str(messageflamme3)+","+str(messageflamme4)+",]\n")
    fichier.write("@\n")
    fichier.close()
def joueur_mort():
    if inventaire[1]<=0:
        if os.path.isfile("./save/save1"):
            charger()
        else:
            nouvelle_partie()
            
def charger():
    
    global nommap
    global nommap2
    global mapx
    global mapy
    global interrupteur
    global FLECHE_MAX
    global VIE_MAX
    global save_desactive
    global coffre1
    global titre

    global boss1
    global boss2
    global boss3
    global boss4
    global cptboss
    global cptboss2
    global cptfinal
    global vague2
    global vague1
    global vague3
    global vague4
    global messageflamme1
    global messageflamme2
    global messageflamme3
    global messageflamme4
    
    cptboss=2000
    cptboss2=1000
    boss1=False
    boss2=False
    boss3=False
    titre=False
    boss4=False
    vague1=False
    vague2=False
    vague3=False
    vague4=False
    messageflamme1=False
    messageflamme2=False
    messageflamme3=False
    messageflamme4=False   
    cptfinal=0
    
    save_desactive=False
    sequence_joueur[:]=[]
    listechangement[:]=[]
    inventaire[:]=[]
    efface_bloque()
    efface_listeitem()
    Ennemi2=[]
    cpt=0
    fichier=open("./save/save1")
    lignes=fichier.readlines()
    cpt2=0
    i=0
    mot=""
    est_changement=False
    for ligne in lignes:
        if ligne[0]=="@":
            cpt2+=1
            mot=""
            cpt=0
            i=0
        else:    
            if cpt2==0:
                for c in ligne:
                    if c=="[":
                        est_changement=True
                        mot=""
                        listechangement.append([])
                    elif c==",":
                        if(cpt==0 or cpt==1 or cpt==3 or cpt==5):
                            listechangement[i].append(int(mot))
                        else:
                            listechangement[i].append(mot)
                        cpt+=1
                        mot=""
                    elif c=="]":
                        cpt=0
                        i+=1
                        est_changement=False
                    elif est_changement:
                        mot+=c
                        
            elif cpt2==1:           
                for c in ligne:
                    if c=="[":
                        est_changement=True
                        mot=""
                    elif c==",":
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
                        elif cpt==7:
                            VIE_MAX=int(mot)
                        elif cpt==8:
                            FLECHE_MAX=int(mot)
                        mot=""
                        est_changement=True
                        cpt+=1
                    elif c=="]":
                        cpt=0
                        i+=1
                        est_changement=False
                    elif est_changement:
                        mot+=c

            elif cpt2==2:           
                for c in ligne:
                    if c=="[":
                        est_changement=True
                        mot=""
                    elif c==",":
                        if(cpt==0 or cpt==1 or cpt==4 or cpt==5 or cpt==6):
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
                        est_changement=True
                    
                    elif c=="]":
                        cpt=0
                        i+=1
                        est_changement=False
                        
                    elif est_changement:
                        mot+=c

            elif cpt2==3:           
                for c in ligne:
                    if c=="[":
                        est_changement=True
                        mot=""
                        Ennemi2.append([])
                    elif c==",":
                        if(cpt!=3):
                            Ennemi2[i].append(int(mot))
                        else:
                            Ennemi2[i].append(mot)
                        mot=""
                        cpt+=1
                        est_changement=True
                    
                    elif c=="]":
                        cpt=0
                        i+=1
                        est_changement=False
                        
                    elif est_changement:
                        mot+=c
                        
            elif cpt2==4:           
                for c in ligne:
                    if c=="[":
                        est_changement=True
                        mot=""
                        listecassable.append([])
                    elif c==",":
                        listecassable[i].append(int(mot))
                        mot=""
                        cpt+=1
                        est_changement=True
                    
                    elif c=="]":
                        cpt=0
                        i+=1
                        est_changement=False
                        
                    elif est_changement:
                        mot+=c
                        
            elif cpt2==5:           
                for c in ligne:
                    if c=="[":
                        est_changement=True
                        mot=""
                    elif c==",":
                        if cpt==0:
                            if mot[0]=="F":
                                coffre1=False
                            else:
                                coffre1=True             
                        elif cpt==1:
                            if mot[0]=="F":
                                vague1=False
                            else:
                                vague1=True    
                        elif cpt==2:
                            if mot[0]=="F":
                                vague2=False
                            else:
                                vague2=True
                        elif cpt==3:
                            if mot[0]=="F":
                                vague3=False
                            else:
                                vague3=True
                        elif cpt==4:
                            if mot[0]=="F":
                                vague4=False
                            else:
                                vague4=True  
                        elif cpt==5:
                            if mot[0]=="F":
                                messageflamme1=False
                            else:
                                messageflamme1=True    
                        elif cpt==6:
                            if mot[0]=="F":
                                messageflamme2=False
                            else:
                                messageflamme2=True
                        elif cpt==7:
                            if mot[0]=="F":
                                messageflamme3=False
                            else:
                                messageflamme3=True    
                        elif cpt==8:
                            if mot[0]=="F":
                                messageflamme4=False
                            else:
                                messageflamme4=True  
                        mot=""
                        est_changement=True
                        cpt+=1
                    elif c=="]":
                        cpt=0
                        i+=1
                        est_changement=False
                    elif est_changement:
                        mot+=c
            
    Ennemi[:]=[]
    mon_perso[10]=[0,0,0,0,[],"Bas"]
    canvas.delete("all")
    affiche_terrain(nommap)
    copie=[]
    i=0

    for liste in bloque:
        for l in listecassable:
            if l[0]==liste[0] and l[1]==liste[1] and liste[2]=="./spriteObjet/objet09":
                copie.append(liste)
                break
            
    for eff in copie:
        bloque.remove(eff)
        
    copie=[]
    
    for l in listeitem:
        for liste in listecassable:
            if liste[0]==l[1] and liste[1]==l[2]:
        	efface(l[5])
                placer("./spriteSurface/bloc05",l[1],l[2],0)
                copie.append(l)
                break

    for eff in copie:
        listeitem.remove(eff)
        
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
                        
def actionne_marchand():
    global achat

    mon_fichier = open("./menu/marchand", "r")
    message1 = mon_fichier.read()
    lemarchand[2][0]=485
    lemarchand[2][1]=240
    lemarchand[3]=0
    lemarchand[0].append(canvas.create_rectangle(440, 190, 570, 410,width=1, fill='white'))
    lemarchand[0].append(canvas.create_rectangle(450, 200, 560, 400,width=5, fill='white'))
    lemarchand[1].append(canvas.create_text(500, 300, text = message1))
    lemarchand[0].append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
    lemarchand[4]= canvas.create_text(320, 590, text = "Bien le Bonjour, je suis un Marchand intinérant")
    mon_fichier.close()
    placer_curseurmarchand()
    
def placer_curseurmarchand():
    fichier=open("./menu/curseur","r")
    lignes=fichier.readlines()
    val_x=lemarchand[2][0]
    val_y=lemarchand[2][1]
    for ligne in lignes:
        for num in ligne:
            if num=="1":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="")
                lemarchand[2][2].append(fig)
            val_x+=2

        val_y+=2
        val_x=lemarchand[2][0]
    fichier.close()
    
def active_bois():
    global dialogue_bois
    global nommap
    global nommap2
    if 268<=mon_perso[3]<=320 and mon_perso[2]<=96:
        sequence_joueur.append("G")
        mon_perso[2]=544
    if 288<=mon_perso[2]<=320 and mon_perso[3]<=96:
        sequence_joueur.append("H")
        mon_perso[3]=544
    if 288<=mon_perso[2]<=320 and mon_perso[3]>=576:
        sequence_joueur.append("B")
        mon_perso[3]=128
        
    cpt=len(sequence_joueur)
    if cpt>0:
        for i in range(0,cpt):
            if sequence_joueur[i]!=sequence1[i] and sequence_joueur[i]!=sequence2[i] :
                sequence_joueur[:]=[]
                cpt=0
                
    if sequence_joueur==sequence1:
        sequence_joueur[:]=[]
        Ennemi[:]=[]
        canvas.delete("all")
        nommap2="BoisSoluce1"
        nommap="./map/BoisSoluce1"
        efface_listeitem()
        bloque[:]=[]
        affiche_terrain(nommap)
        mon_perso[3]=544
        mon_perso[2]=320

    if sequence_joueur==sequence2:
        mon_perso[3]=544
        mon_perso[2]=320
        sequence_joueur[:]=[]
        Ennemi[:]=[]
        canvas.delete("all")
        nommap2="BoisSoluce2"
        nommap="./map/BoisSoluce2"
        efface_listeitem()
        bloque[:]=[]
        affiche_terrain(nommap)
        #["G","H","G","G","H","B","G","H","B","H"]
    if cpt==0:
        dialogue_bois="Prend d'abord à l'Ouest puis ensuite vers le Sud\nUn des Fantôme ment Toujours."
    elif cpt==1:
        dialogue_bois="Le Premier Fantôme Confond Nord et Sud, \nLe sixiéme Fantôme dit toujours la vérité."
    elif cpt==2:
        dialogue_bois="Dirige toi Deux Fois vers l'Ouest, mais attention\ncar le septiéme Fantôme ment"
    elif cpt==3:
        dialogue_bois="le Deuxiéme et Cinquiéme Fantôme Mentent"
    elif cpt==4:
        dialogue_bois="Dirige toi vers le Nord"
    elif cpt==5:
        dialogue_bois="Dirige toi Vers le Sud \nLe Troisiéme Fantome déteste le Septiéme. "
    elif cpt==6:
        dialogue_bois="Dirige toi vers l'Ouest, puis vers le Nord \nle Neuviéme Fantome inverse les direction"
    elif cpt==7:
        dialogue_bois="Il existe un Chemin caché dans cette forêt"
    elif cpt==8:
        dialogue_bois="Va vers le Nord"
    elif cpt==9:
        dialogue_bois="Dirige toi vers la Cinquiéme direction que tu as choisit.."
    else:
        dialogue_bois="Si tu es ici par hasard, Bravo."

def ecran_titre():
    global titre
    global attendre
    canvas.delete("all")
    affiche_terrain("./map/Cinematique")
    attendre=True
    titre = True
    menu()
 
def nouvelle_partie():
    global nommap
    global nommap2
    global titre
    global boss1
    global boss2
    global boss3
    global boss4
    global cptboss
    global cptboss2
    global cptfinal
    global vague2
    global vague1
    global vague3
    global vague4
    global messageflamme1
    global messageflamme2
    global messageflamme3
    global messageflamme4
    global introd

    cptboss=2000
    cptboss2=1000
    boss1=False
    boss2=False
    boss3=False
    boss4=False
    vague1=False
    vague2=False
    vague3=False
    vague4=False
    messageflamme1=False
    messageflamme2=False
    messageflamme3=False
    messageflamme4=False   
    cptfinal=0

    canvas.delete("all")
    inventaire[:]=[20,20,True,True,0,0,0]#[fleche,vie,Epee,Arc,Gold,clef,Grande Clef]
    mon_perso[:]=[0,0,320,392,[],"./spritePerso/PersoB1","Bas",0,inventaire,[0,False,""],[0,0,0,0,[],"Bas"],0] #[vitessex,vitessey,posx,posy,idsprite,sprite,orientation,d,[Inventaire],[Epee],[Fleche],compteurDegat]
    nommap="./map/tuto1"
    nommap2="tuto1"
    titre=False
    Ennemi[:]=[]
    bloque[:]=[]
    introd=0
    affiche_terrain(nommap)
    verifie_interrupteur()

def introduction():
    global introd
    global titre
    global attendre
    global message_active
    global introactive
    message_active=True
    titre=False
    attendre=False
    canvas.delete("all")
    boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
    
    if introd==0:
        boss.append(canvas.create_text(320, 590, text = "Les légendes racontent qu'autrefois il existait un Royaume trés avancé. "))
        introd+=1
    elif introd==1:
        affiche_terrain("./map/intro1")
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Mais un jour ce Royaume disparu de la carte.\nLaissant derriére lui 6 Critaux au pouvoir incommensurable. "))
        introd+=1
    elif introd==2:
        affiche_terrain("./map/intro3")
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "En prévention, ils furent cachés dans 6 lieux différents. "))
        introd+=1
    elif introd==3:
        affiche_terrain("./map/intro2")
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Et des gardiens furent désigner pour veilleur sur les critaux."))
        introd+=1
    elif introd==4:
        affiche_terrain("./map/Cinematique")
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Mais Aujourd'hui les cristaux sont en danger !"))
        introd+=1
    elif introd==5:
        mouvement_perso()
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Et c'est toi qui a été choisit pour éviter \nqu'ils ne tombent entre de mauvaise main."))
        introd+=1
    elif introd==6:
        introactive=False
        nouvelle_partie()
        boss.append(canvas.create_rectangle(100, 550, 550, 625, width=5, fill='white'))
        boss.append(canvas.create_text(320, 590, text = "Va et accomplis ta mission !"))

        
fenetre = Tk()
canvas = Canvas(fenetre, width=640, height=640, background="black")

mapx=1
mapy=1

nommap="./map/tuto1"
nommap2="tuto1"

inventaire=[20,20,True,True,0,0,0]#[fleche,vie,Epee,Arc,Gold,clef,Grande Clef]
mon_perso=[0,0,320,392,[],"./spritePerso/PersoB1","Bas",0,inventaire,[0,False,""],[0,0,0,0,[],"Bas"],0] #[vitessex,vitessey,posx,posy,idsprite,sprite,orientation,d,[Inventaire],[Epee],[Fleche],compteurDegat]

Ennemi=[]
bloque=[]

HUD=[[],[]]

lemenu=[[],[],[485,280,[]],0] # Menu,Option,Curseur,Num_Option
lemarchand=[[],[],[485,240,[]],0,""] #MenuMarchand+fenetredialogue,Option,Curseur,Num_option,Dialogue 

rectangle = 0
idmessage = 0
interrupteur=0
sequence1=["G","H","G","G","H","B","G","H","B","H"]
sequence2=["G","H","G","G","G","H","G","B","H"]
sequence_joueur=[]
dialogue_bois=""

introd=0
introactive=False
message_active=False
coffre1=False
attendre = False
achat=False
vague2=False
vague1=False
vague3=False
vague4=False
save_desactive=False
messageflamme1=False
messageflamme2=False
messageflamme3=False
messageflamme4=False
boss1=False
boss2=False
boss3=False
boss4=False
vulnerable=False
titre=True
fin=False

boss=[]
cptboss=2000
cptboss2=1000
cptfinal=0
timer=[]

listeitem=[]

sprite_att=[]
listeobjet=[]
listecassable=[]
listechangement=[]

VIE_MAX=20
FLECHE_MAX=20


frame()


canvas.pack()
canvas.focus_set()
canvas.bind("<Key>", vitesse)
canvas.bind("<KeyRelease>", stop)
        
fenetre.mainloop()

