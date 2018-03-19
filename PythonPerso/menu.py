#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from random import *
import os

def placer(nom,x,y,canvas):

    global ma_map
    val_x=x
    val_y=y
    fichier = open(nom,'r')
    lignes  = fichier.readlines()

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

            if ligne[i]!="0":    
                ma_map[x/32+y/32*20].append(fig)
                                        
            val_x+=2
        val_y+=2
        val_x=x
    print ma_map[x/32+y/32*20]
    print"-------------"
    fichier.close()

def bougerCurseur1():
    global curseur1
    global selection
    curseur1[2]+=curseur1[0]
    curseur1[3]+=curseur1[1]
    if len(curseur1[4])>0:
        canvas2.delete(curseur1[4][0])
        del curseur1[4][0]
    curseur1[4].append(canvas2.create_rectangle(curseur1[2],curseur1[3],curseur1[2]+32,curseur1[3]+32,fill=''))

    
def bougerCurseur2():
    global curseur2
    global selection
    curseur2[2]+=curseur2[0]
    curseur2[3]+=curseur2[1]
    if len(curseur2[4])>0 :
        canvas.delete(curseur2[4][0])
        del curseur2[4][0]
    curseur2[4].append(canvas.create_rectangle(curseur2[2],curseur2[3],curseur2[2]+32,curseur2[3]+32,fill=''))

    selection=(curseur2[2]/32)+(curseur2[3]/32*20)


def frame():

    bougerCurseur1()
    bougerCurseur2()

def vitesse(event):
    global commence
    global Bloc
    global nom
    global mode
    global nommap
    touche=event.keysym
    if(commence==True):
    
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
            placer_map()
            
        if touche=="Delete":
            effacer()

            
        if touche=="space":
            posx=0
            posy=0
            mode+=1
            if mode>3:
                mode=0
                canvas.delete("all")
                for i in range(0,len(Bloc)):
                    nom="./spriteSurface/bloc"
                    placer(nom+Bloc[i],posx,posy,canvas)
                    if(posx>=608):
                        posx=0
                        posy+=32
                    else:
                        posx+=32
            if mode==1:
                canvas.delete("all")
                for i in range(0,len(Bloc)):
                    nom="./spriteDecor/bloc"
                    placer(nom+Bloc[i],posx,posy,canvas)
                    if(posx>=608):
                        posx=0
                        posy+=32
                    else:
                        posx+=32
                
            elif mode==3:
                canvas.delete("all")
                for i in range(0,len(Bloc)):
                    nom="./spriteObjet/objet"
                    placer(nom+Bloc[i],posx,posy,canvas)
                    if(posx>=608):
                        posx=0
                        posy+=32
                    else:
                        posx+=32
                        
            elif mode==2:
                canvas.delete("all")
                for i in range(0,len(Bloc)):
                    nom="./spriteEnnemi/Ennemi"
                    placer(nom+Bloc[i],posx,posy,canvas)
                    if(posx>=608):
                        posx=0
                        posy+=32
                    else:
                        posx+=32

def placer_map():
    
    global commence
    global Bloc
    global nom
    global mode
    global nommap
    global ma_map

    cpt=0
    nom2=nom+Bloc[selection]
    fichier=open("./map/"+nommap+".cp","r")
    lignes=fichier.readlines()
    fichier2=open("./map/"+nommap+".cp","w")
            
    for ligne in lignes:
        for i in range(0,20):
            if cpt==curseur1[3]/32+(mode*20):
                if i==curseur1[2]/32:
                    if i==0:
                        deb=""
                        fin=ligne[i+1:]

                    else:
                        deb=ligne[:i]
                        fin=ligne[i+1:]

                    ligne=deb+nom2[len(nom2)-1]+fin
                            
        fichier2.write(ligne)
        cpt+=1
                
    fichier2.close()
    fichier.close()
    fichier=open("./map/"+nommap+".cp","r")
    lignes=fichier.readlines()
    
    ma_map[curseur1[2]/32+curseur1[3]/32*20]=[]
    num=lignes[curseur1[3]/32][curseur1[2]/32]
    placer("./spriteSurface/bloc"+num,curseur1[2],curseur1[3],canvas2)
    num=lignes[curseur1[3]/32+20][curseur1[2]/32]
    if num!="0":
        placer("./spriteDecor/bloc"+num,curseur1[2],curseur1[3],canvas2)
    num=lignes[curseur1[3]/32+40][curseur1[2]/32]
    placer("./spriteEnnemi/Ennemi"+num,curseur1[2],curseur1[3],canvas2)
    num=lignes[curseur1[3]/32+60][curseur1[2]/32]
    placer("./spriteObjet/objet"+num,curseur1[2],curseur1[3],canvas2)

def effacer():
    global ma_map
    global commence
    global Bloc
    global nom
    global mode
    global nommap

    if(commence==True):
        print ma_map[(curseur1[2]/32)+curseur1[3]/32*20]
        print"-------------"

        for i in range(0,len(ma_map[(curseur1[2]/32)+curseur1[3]/32*20])):
            canvas2.delete(ma_map[curseur1[2]/32+curseur1[3]/32*20][i])
            
        ma_map[(curseur1[2]/32)+curseur1[3]/32*20]=[]
                
        cpt=0
        nom2=nom+Bloc[selection]
        fichier=open("./map/"+nommap+".cp","r")
        lignes=fichier.readlines()
        fichier2=open("./map/"+nommap+".cp","w")

        for ligne in lignes:
            for i in range(0,20):
                if cpt==curseur1[3]/32:
                    if i==curseur1[2]/32:
                        if i==0:
                            deb=""
                            fin=ligne[i+1:]

                        else:
                            deb=ligne[:i]
                            fin=ligne[i+1:]

                        ligne=deb+"0"+fin
            fichier2.write(ligne)
            cpt+=1
            if cpt>=20:
                cpt=0
        fichier2.close()
        fichier.close()
   

def stop(event):
    global commence
    if(commence==True):
        touche=event.keysym
        if(touche=="Up" or touche=="Down"):
            curseur1[1]=0

        if(touche=="Right" or touche=="Left"):
            curseur1[0]=0
        
        if(touche=="z" or touche=="s"):
            curseur2[1]=0

        if(touche=="d" or touche=="q"):
            curseur2[0]=0

    



def initialisecanvas():
    global canvas
    global canvas2
    global posx
    global posy
    global ma_map

    ma_map=[]
    for i in range(0,20*20):
        ma_map.append([])
        
    posx=0
    posy=0
    canvas2 =Canvas(fenetre, width=640, height=640, background="#219a21")
    canvas =Canvas(fenetre, width=640, height=300)
    canvas.pack()
    canvas.focus_set()
    canvas2.pack()
    canvas2.focus_set()
    for i in range(0,len(Bloc)):
        nom="./spriteDecor/bloc"+Bloc[i]
        placer(nom,posx,posy,canvas)
    
        if(posx>=608):
            posx=0
            posy+=32
        else:
            posx+=32
                
    
def test():
    global commence
    global efface
    if efface:
        initialisecanvas()
        efface=False
    if commence:            
        frame()

    fenetre.after(100,test)
    
def affiche_terrain(nom):
    global ma_map
    fichier=open(nom,"r")
    lignes=fichier.readlines()
    j=0
    h=0
    cpt=0
    

    for ligne in lignes:
        if cpt>=20:
            cpt=0
            h+=1
            j=0
            print ligne
        for i in range (0,20):
            ma_map[i+j/32*20]=[]
            if(ligne[i]!="0"):
                if h==0:
                    nom="./spriteSurface/bloc"

                elif h==1:
                    nom="./spriteDecor/bloc"
                elif h==3:
                    nom="./spriteObjet/objet"
                elif h==2:
                    nom="./spriteEnnemi/Ennemi"
                        
                nom+=ligne[i]
                placer(nom,(i*32),j,canvas2)
        j+=32
        cpt+=1
    fichier.close()
    
def validernom2():
    global copie
    global commence
    global efface
    global nommap
    global curseur1
    global curseur2
    global pasouvert


    nommap= copie[0].get()
    
    if(os.path.isfile("./map/"+nommap)):
        if commence:
            canvas.destroy()
            canvas2.destroy()
        
        curseur1[2]=0
        curseur1[3]=0
        curseur2[2]=0
        curseur2[3]=0
        
        initialisecanvas()
    
        fichier=open("./map/"+nommap+".cp","w")
        fichier2=open("./map/"+nommap,"r")
        lignes=fichier2.readlines()
        for ligne in lignes:
            fichier.write(ligne)
        
        fichier.close()
        fichier2.close()
        
        copie[1].destroy()
        copie[0].destroy()
        del copie[1]
        del copie[0]
        commence=True
        affiche_terrain("./map/"+nommap)
        pasouvert=True
        
    else:
        print "Fichier inexistant"

    
def nouveau():
    global copie
    global pasouvert

    if not(pasouvert):
        copie[1].destroy()
        copie[0].destroy()
        del copie[1]
        del copie[0]
        
    pasouvert=False
    entree = Entry(fenetre, width=30)
    copie.append(entree)
    entree.pack()
    bouton=Button(fenetre, text="Valider", command=validernom)
    copie.append(bouton)
    bouton.pack()

def validernom():
    global copie
    global commence
    global efface
    global nommap
    global curseur1
    global curseur2
    global pasouvert

    nommap= copie[0].get()
    print "./map/"+nommap
    
    if(os.path.isfile("./map/"+nommap)):
        print "Existe deja"

    else:
        curseur1[2]=0
        curseur1[3]=0
        curseur2[2]=0
        curseur2[3]=0
        
        if commence:
            canvas.destroy()
            canvas2.destroy()
        
        initialisecanvas()
        fichier=open("./map/"+nommap+".cp","w")
        ligne="00000000000000000000"
        for i in range(0,79):
            fichier.write(ligne+"\n")
        fichier.write(ligne)
        fichier.close()
    
        copie[1].destroy()
        copie[0].destroy()
        del copie[1]
        del copie[0]
        commence=True
        pasouvert=True

    
    
def editer():
    global copie
    global mode
    global pasouvert

    if not(pasouvert):
        copie[1].destroy()
        copie[0].destroy()
        del copie[1]
        del copie[0]
        
    pasouvert=False
    mode=1
    entree = Entry(fenetre, width=30)
    copie.append(entree)
    entree.pack()
    bouton=Button(fenetre, text="Valider", command=validernom2)
    copie.append(bouton)
    bouton.pack()

def souris(event):
    global curseur1
    global curseur2
    
    if(commence==True):
        if event.widget==canvas2:
            curseur1[2]=(event.x/32)*32
            curseur1[3]=(event.y/32)*32
            placer_map()

        elif event.widget==canvas:
            curseur2[2]=(event.x/32)*32
            curseur2[3]=(event.y/32)*32
            selection=(curseur2[2]/32)+(curseur2[3]/32*20)
            
def sauvegarder():
    global nommap
    fichier=open("./map/"+nommap+".cp","r")
    fichier2=open("./map/"+nommap,"w")
    lignes=fichier.readlines()
    for ligne in lignes:
        fichier2.write(ligne)
    fichier2.close()
    fichier.close()
    
fenetre = Tk()  
menubar = Menu(fenetre)
copie=[]
commence=False
Finit=True
efface=False
mode=1
nom="./spriteDecor/bloc"
ma_map=[]
for i in range(0,20*20):
    ma_map.append([])

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouveau", command=nouveau)
menu1.add_command(label="Editer", command=editer)
menu1.add_command(label="Sauvegarder", command=sauvegarder)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)
fenetre.config(menu=menubar)

mapobj=[]
map=[]
mapennemi=[]
mapsurf=[]
nommap=""

canvas2 =""
canvas ="" 
curseur1=[0,0,0,0,[]]
curseur2=[0,0,0,0,[]]
posx=0
posy=0
selection=0
Bloc="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi"
pasouvert=True


test()

fenetre.bind("<Key>", vitesse)
fenetre.bind("<KeyRelease>", stop)
fenetre.bind("<Button-1>", souris)
        
fenetre.mainloop()

