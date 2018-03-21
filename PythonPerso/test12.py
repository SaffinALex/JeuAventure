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

    for cpt in range(0,20):
        for i in range (0,20):
            nom="./spriteSurface/bloc"+lignes[cpt][i]
            placer(nom,(i*32),j,0)
        j+=32
    fichier.close()
    affiche_surf()
    affiche_obj()
    if(attendre == False):
	affiche_ennemi()


def affiche_obj():
    global mapx
    global mapy
    global listeitem
    global listechangement
    ouvert=False
    porte_ouverte=False
    
    nom="./map/map"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for cpt in range(60,80):
        for i in range (0,20):
            if lignes[cpt][i]!="0":
                ouvert=False
                if lignes[cpt][i]=="5" or lignes[cpt][i]=="6" or lignes[cpt][i]=="7" or lignes[cpt][i]=="8":              
                    if(len(listechangement) != 0):
                        for k in range (0,len(listechangement)):
                            if mapx==listechangement[k][2] and mapy==listechangement[k][3] and listechangement[k][0]==i*32 and listechangement[k][1]==j:
                                nom="./spriteObjet/objet"+"4"
                                placer(nom,(i*32),j,2)
                                ouvert=True

                        if(not(ouvert)):
                            nom="./spriteObjet/objet"+"2"
                            listeitem.append([lignes[cpt][i],i*32,j,0,0,[]])
                            placer(nom,(i*32),j,1)


                    else:
                        nom="./spriteObjet/objet"+"2"
                        listeitem.append([lignes[cpt][i],i*32,j,0,0,[]])
                        placer(nom,(i*32),j,2)
                elif lignes[cpt][i]=="C":
                    porte_ouverte=False
                    for k in range (0,len(listechangement)):
                        if mapx==listechangement[k][2] and mapy==listechangement[k][3] and listechangement[k][0]==i*32 and listechangement[k][1]==j and listechangement[k][4]=="C":
                            porte_ouverte=True
                            
                    if(not(porte_ouverte)):            
                        listeitem.append([lignes[cpt][i],i*32,j,0,0,[]])
                        nom="./spriteObjet/objet"+lignes[cpt][i]
                        placer(nom,(i*32),j,2)                        
                            
                else:
                    listeitem.append([lignes[cpt][i],i*32,j,0,0,[]])
                    nom="./spriteObjet/objet"+lignes[cpt][i]
                    placer(nom,(i*32),j,2)       

        j+=32
    fichier.close()

def affiche_surf():
    global mapx
    global mapy
    
    nom="./map/map"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for cpt in range(20,40):
        for i in range (0,20):
            if lignes[cpt][i]!="0":
                nom="./spriteDecor/bloc"+lignes[cpt][i]
                placer(nom,(i*32),j,1)

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
    nom="./map/map"+str(mapx)+"-"+str(mapy)
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0

    for cpt in range(40,60):
        for i in range (0,20):
            if lignes[cpt][i]!="0":
                nom="./spriteEnnemi/ennemi"+lignes[cpt][i]
                ajout_ennemi(nom,i*32,j)

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

    if (mon_perso[2]+32>640):
        mapx+=1
        mon_perso[2]=0
        Ennemi=[]
        efface_bloque()
        efface_listeitem()
        affiche_terrain()
        mouvement_perso()
        
    elif(mon_perso[2]<0):
        mapx-=1
        mon_perso[2]=640-32
        Ennemi=[]
        efface_bloque()
        efface_listeitem()
        affiche_terrain()
	affiche_obj()
        mouvement_perso()
        
    elif(mon_perso[3]<0):
        mapy+=1
        mon_perso[3]=640-32
        Ennemi=[]
        efface_bloque()
        efface_listeitem()
        affiche_terrain()       
	mouvement_perso()
        
    elif(mon_perso[3]+32>640):
        mapy-=1
        mon_perso[3]=0
        Ennemi=[]
        efface_bloque()
        efface_listeitem()
        affiche_terrain()       
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

    decale=False
    x=mon_perso[2]
    y=mon_perso[3]
    fichier = open("./Attaque/epee",'r')
    print "aff_attaque"
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

def aff_tireur():
	global mon_perso
	global sprite_att

	mon_fleche[2]=True
	mon_fleche[5]=mon_perso[6]
	touche_qqch=False
	decale=False
	x=mon_perso[2]
	y=mon_perso[3]
	mon_fleche[0] = mon_perso[2]
	mon_fleche[1] = mon_perso[3]
	fichier = open("./Attaque/arc/arc_secure",'r')
	print "aff_tirer"
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
		elif mon_perso[6]=="Haut":
            		num=32
            		for i in range (0,16):
                		ligne=lignes[i+num]
                		for j in range(0,16):
                    			placer_attaque(ligne[j],x,y)
                    			x+=2
                		x-=32
                		if(y>mon_perso[3]+31):
                    			y-=64
                		y+=2
		elif mon_perso[6]=="Droite":
		    	num=64
		    	for i in range (0,16):
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
		    	num=96
		    	for i in range (0,16):
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

def affiche_fleche():
	orientation = mon_fleche[5]
	fichier=open("./Attaque/arc/arc_secure")
	lignes = fichier.readlines()
	num = 17
    	if (orientation == "Bas") :
		if (mon_perso[3] <= 608) :
			mon_fleche[1] += 8	
        	mon_fleche[3] = "Bas"
	elif orientation == "Haut" :
		if mon_perso[3] >= 32 :
			mon_fleche[1] -= 8
			num += 32
        	mon_fleche[3] = "Haut" 
	elif orientation == "Droite" :
		if mon_perso[2] <= 608 :		
			mon_fleche[0] += 8
			num += 64
        	mon_fleche[3] = "Droite"
	elif orientation == "Gauche" :
		if mon_perso[2] >= 32 :
			mon_fleche[0] -= 8
			num += 96
        	mon_fleche[3] = "Gauche"
	bouger_fleche(mon_fleche[4],orientation,mon_fleche[0],mon_fleche[1],num)

	print mon_fleche[1]
	print mon_fleche[0]	
#def mouvement_fleche():
#	sprite_pos = []
#	orientation = mon_perso[6]
#	bouger_fleche(sprite_pos,orientation,mon_fleche[0],mon_fleche[1],num)
	
def mouvement_fleche():
	effaces=[]
	affiche_fleche()
	if mon_fleche[3]=="Haut" or mon_fleche[3]=="Bas":
		if mon_fleche[3]=="Haut":
			posx=mon_fleche[0]
			posy=mon_fleche[1]
        
		if mon_fleche[3]=="Bas":
			posx=mon_fleche[0]
			posy=mon_fleche[1]+16
            
		for i in range(0,len(Ennemi)):
			if Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
				effaces.append(i)
				mon_fleche[2] = False
                
			elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
				effaces.append(i)
				mon_fleche[2] = False
                
			elif Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
				effaces.append(i)
				mon_fleche[2] = False
                
			elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
				effaces.append(i)
				mon_fleche[2] = False

	if mon_fleche[3]=="Droite" or mon_fleche[3]=="Gauche":
		if mon_fleche[3]=="Gauche":
			posx=mon_fleche[0]-16
			posy=mon_fleche[1]
            
		if mon_fleche[3]=="Droite":
			posx=mon_fleche[0]+16
			posy=mon_fleche[1]

            
		for i in range(0,len(Ennemi)):
			if Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
				effaces.append(i)
				mon_fleche[2] = False
                
			elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]+31>=posy and Ennemi[i][3]+31<posy+31:
				effaces.append(i)
				mon_fleche[2] = False
                
			elif Ennemi[i][2]>=posx and Ennemi[i][2]<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
				effaces.append(i)
				mon_fleche[2] = False
                
			elif Ennemi[i][2]+31>=posx and Ennemi[i][2]+31<posx+31 and Ennemi[i][3]>=posy and Ennemi[i][3]<posy+31:
				effaces.append(i)
				mon_fleche[2] = False

	if mon_fleche[0] >= 640 or mon_fleche[0] <= 0 or mon_fleche[1] <= 0 or mon_fleche[1] >= 640:
		efface(mon_fleche[4])
		mon_fleche[2]= False
		print "ok"

	if(len(effaces)>0):     
		for i in range(len(effaces)):
			efface(Ennemi[effaces[i]][4])
			efface(mon_fleche[4])

def bouger_fleche(sprite_pos,orientation, x, y, num):
	efface(sprite_pos)
	
	val_x=x
	val_y=y
	fichier=open("./Attaque/arc/arc_secure")
	lignes = fichier.readlines()
	for i in range (0,16):
		ligne = lignes[i+num]
		for j in range (0,16):
			if ligne[j]=="1":
				pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#0a650a",outline="")
			elif ligne[j]=="2":
				pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="black",outline="")
			elif ligne[j]=="3":
				pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="blue",outline="")
			elif ligne[j]=="4":
				pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#808180",outline="")
			elif ligne[j]=="5":
				pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#614919",outline="")
			elif ligne[j]=="6":
				pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="red",outline="")
			elif ligne[j]=="7":
				pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#d4a566",outline="")
			elif ligne[j]=="8":
				pos= canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#96c14b",outline="") #vertClaire
			elif ligne[j]=="9":
				pos=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="white",outline="")

			if ligne[j]!="0":
				sprite_pos.append(pos)
			val_x +=2

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

    if(not attendre):
    #print mon_perso[0]
        evenement()
        changeMap()
        
        if mon_perso[9][1]:
            if mon_perso[9][0]==0:
                if mon_perso[9][2]=="b":
					aff_attaque()
                elif mon_perso[9][2]=="c" and mon_fleche[2]==False:
					aff_tireur()
                mon_perso[9][0]=1
            else:
                mon_perso[9][0]-=1

        if(not mon_perso[9][1]):
			mouvement_perso()


        if (mon_fleche[2] == True):
            mouvement_fleche()
            
       # for i in range(0,len(Ennemi)):
          #  mouvement_ennemi(Ennemi[i])
        
        if(len(Ennemi)>0):
            if mon_perso[9][1]:
                toucher(mon_perso)
            
        for i in range(0,len(listeitem)):
            if(listeitem[i][3]>0):
                compt(listeitem[i])
        
        canvas.after(30,frame)

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
        for i in range(len(effaces)):
            efface(Ennemi[effaces[i]][4])

            
                    
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

        
    if(touche=="a"):
        interagir()

    if(touche=="b"):
        attaque()
	
    if(touche=="c"): 
	tirer()

def attaque():
    global mon_perso
    if not mon_perso[9][1]:
	mon_perso[9][2]="b"
        mon_perso[9][1]=True
        mon_perso[9][0]=0
        mon_perso[7]=3

def tirer():
    global mon_perso
    if not mon_perso[9][1]: #on cd ?
	mon_perso[9][2]="c"
        mon_perso[9][1]=True #cd = true
	mon_perso[9][0]=0 #cd time
	mon_perso[7]=0


def placer_sol(x,y):
    canvas.create_rectangle(x,y,x+32,y+32,fill="#219a21",outline="") #vert

def accueil():
	global premier_passage
	canvas.delete("all")
	canvas.create_text(400, 300, text = "Appuyer sur Espace pour Continuer")
	premier_passage = True

def menu_principal(event):
	global choix_menu_principal
	global attendre_principal
	global attendre
	global premier_passage

	touche=event.keysym
	if(touche == "space"):
		if(premier_passage == True):
			attendre_principal = True
			canvas.delete("all")
			choix_menu_principal = 0
			premier_passage = False
			creation_menu_principal(300,200)
		
	if(touche=="Down"):
		if(attendre_principal == True):
			if(choix_menu_principal == 0):
				canvas.delete("all")
				choix_menu_principal = 1
				creation_menu_principal(300,300)	
				
			elif(choix_menu_principal == 1):
				canvas.delete("all")
				choix_menu_principal = 2
				creation_menu_principal(300,400)
				
			elif(choix_menu_principal == 2):
				canvas.delete("all")
				choix_menu_principal = 0
				creation_menu_principal(300,200)
				
		elif(attendre_principal == False):
			menu(event)
	if(touche=="Up"):
		if(attendre_principal == True):
			if(choix_menu_principal == 0):
				canvas.delete("all")
				choix_menu_principal = 2
				creation_menu_principal(300,400)
				
			elif(choix_menu_principal == 1):
				canvas.delete("all")
				choix_menu_principal = 0
				creation_menu_principal(300,200)
				
			elif(choix_menu_principal == 2):
				canvas.delete("all")
				choix_menu_principal = 1
				creation_menu_principal(300,300)
				
		elif(attendre_principal == False):
			menu(event)

	if(touche=="Return"):
		if(attendre_principal == True):
			if(choix_menu_principal == 0):
				attendre_principal = False
				affiche_terrain()
				affiche_obj()
				frame()				
		elif(attendre_principal == False):
			menu(event)		
def creation_menu_principal(x,y):
	
	canvas.create_text(200, 200, text = "Nouvelle Partie")
	canvas.create_text(x, y, text = "<")
	canvas.create_text(200, 300, text = "Charger Partie")
	canvas.create_text(200, 400, text = "Options")
   
def creation_menu(x,y):
	
	canvas.create_text(200, 200, text = "Reprendre")
	canvas.create_text(x, y, text = "<")
	canvas.create_text(200, 300, text = "Menu Principal")



def menu(event):
    global attendre
    global choix_menu
	
    touche=event.keysym
    if(touche=="Escape"):
	if(attendre != True):
		if(attendre_principal == False):
	        	attendre = True
			canvas.delete("all")
			choix_menu = 0
			creation_menu(300,200)

    if(touche=="Down"):
	if(attendre == True):
		if(choix_menu == 0):
			canvas.delete("all")
			creation_menu(300,300)
			choix_menu = 1
		elif(choix_menu == 1):
			canvas.delete("all")
			creation_menu(300,200)
			choix_menu = 0
	elif(attendre == False):
		vitesse(event)
    if(touche=="Up"):
	if(attendre == True):
		if(choix_menu == 0):
			canvas.delete("all")
			creation_menu(300,300)
			choix_menu = 1
		elif(choix_menu == 1):
			canvas.delete("all")
			creation_menu(300,200)
			choix_menu = 0
	elif(attendre == False):
		vitesse(event)

    if(touche=="Return"):
	if(attendre == True):
		if(choix_menu == 0):
			affiche_terrain()
        		attendre = False
			frame()
		elif(choix_menu == 1):
			attendre = False
			accueil()


				

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
    if liste[0]=="5" or liste[0]=="6" or liste[0]=="7" or liste[0]=="8":
        liste[3]-=1
        if liste[3]==0:
            placer("./spriteObjet/objet4",liste[1],liste[2],0)
            
def efface_listeitem():
    global listeitem
    while len(listeitem)>0:
        del listeitem[len(listeitem)-1]

def efface_item(liste):
    for i in range(0,len(liste[5])):
        canvas.delete(liste[5][0])
        del liste[5][0]

def interaction(liste):
    global inventaire
    global listechangement
    global mapx
    global mapy
    global bloque_x
    global bloque_y
    numero_eff=[]
    
    if liste[0]=="5" or liste[0]=="6" or liste[0]=="7" or liste[0]=="8":
        if liste[4]!=1:
            liste[3]=10
            liste[4]=1
            listechangement.append([liste[1],liste[2],mapx,mapy,liste[0]])
            placer("./spriteObjet/objet"+liste[0],liste[1],liste[2],0)
            if liste[0]=="5":
                inventaire[0]+=1
                print inventaire[0]
            elif liste[0]=="6":
                inventaire[0]+=5
                print inventaire[0]
            elif liste[0]=="7":
                inventaire[1]+=1

            
    if liste[0]=="C" and inventaire[1]>0 and liste[4]!=1:
        
        inventaire[1]-=1
        print inventaire[1]
        listechangement.append([liste[1],liste[2],mapx,mapy,liste[0]])
        
        for i in range(0,len(bloque_x)):
            if(bloque_x[i]==liste[1] and bloque_y[i]==liste[2]):
                numero_eff.append(i)
                liste[4]=1
                efface_item(liste)
                placer_sol(liste[1],liste[2])

                
        if len(numero_eff)!=0:
            for j in range(0, len(numero_eff)):
                del bloque_x[numero_eff[len(numero_eff)-1]]
                del bloque_y[numero_eff[len(numero_eff)-1]]
                del numero_eff[len(numero_eff)-1]
    
        
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

canvas = Canvas(fenetre, width=640, height=639, background="#219a21")
mapx=1
mapy=1
deplacement=0
mon_perso=[0,0,96,384,[],"./spritePerso/PersoB1","Bas",0,0,[0,False,"null"]] # vitesse x,y ,pos x,y ,perso,sprite,orientation,cptAttaque,cptOriente,CouldownAttaque
mon_fleche=[mon_perso[2],mon_perso[3],False,"Bas",[],orientation]#position x, y, flèche_sur_écran?, orientation du fleche
Ennemi=[]
bloque_y=[]
bloque_x=[]
cpt=0
bloquer=[]
for i in range(0,20*20):
    bloquer.append([])

sprite_att=[]
coffre1=False
attendre = False
attendre_principal = False
premier_passage = False
listeitem=[]
listecassable=[]
listechangement=[]
inventaire=[0,0]
#accueil()
affiche_terrain()
frame()


canvas.pack()
canvas.event_add('<<menu_esc>>', '<KeyPress-Escape>')
canvas.event_add('<<menu_ret>>', '<KeyPress-Return>')
canvas.event_add('<<menu_up>>', '<KeyPress-Up>')
canvas.event_add('<<menu_dwn>>', '<KeyPress-Down>')
canvas.event_add('<<menu_spac>>', '<KeyPress-space>')
canvas.focus_set()
canvas.bind("<Key>", vitesse)
canvas.bind("<KeyRelease>", stop)
canvas.bind("<<menu_esc>>",menu)
canvas.bind("<<menu_ret>>",menu_principal)
canvas.bind("<<menu_up>>",menu_principal)
canvas.bind("<<menu_dwn>>",menu_principal)
canvas.bind("<<menu_spac>>",menu_principal)

        
fenetre.mainloop()
    
