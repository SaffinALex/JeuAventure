#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from random import *
import os

def placer(nom,x,y,canvas):
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
                 fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#b81e1e",outline="") #rouge 
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
            elif ligne[i]=="F":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#c66f04",outline="") #orange
            elif ligne[i]=="G":
                fig=canvas.create_rectangle(val_x,val_y,val_x+2,val_y+2,fill="#5a2a10",outline="") #orange/POurpre
            if ligne[i]!="0":    
                ma_map[x/32+y/32*20].append(fig)
                                        
            val_x+=2
        val_y+=2
        val_x=x
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
    global pasouvert
    global fenetre2
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

        if touche=="c":
            if not(pasouvert):
                fenetre2.destroy()
                del copie[0]
            pasouvert=True
            fichier=open("./map/"+nommap+".cp","r")
            lignes=fichier.readlines()

            num1=lignes[curseur1[3]/32+60]
            num1=num1[:curseur1[2]/32*2+2]
            num1=num1[curseur1[2]/32*2:]
            num=num1
            chemin="./tp/"+nommap+"."+num+"."+str(curseur1[2])+"."+str(curseur1[3])
            if num!="00":
                if not os.path.isfile(chemin):
                    fichier2=open(chemin,"w")
                    fichier2.close()
            fichier.close()
    
            
        if touche=="t":
            if not(pasouvert):
                fenetre2.destroy()
                del copie[0]
            pasouvert=False
            i=0
            mesfichier = os.listdir('./tp')
            mesfichier.sort()
            fenetre2=Toplevel(fenetre)
            scrollbar = Scrollbar(fenetre2)
            scrollbar.pack(side=RIGHT, fill=Y)
            liste = Listbox(fenetre2,yscrollcommand=scrollbar.set)
            for fiche in mesfichier:
                liste.insert(i,fiche)
                i+=1
            scrollbar.config(command=liste.yview)
            liste.pack()
            copie.append(liste)
            bouton=Button(fenetre2, text="Valider", command=validerTP)
            bouton.pack()

        if touche=="m":
            if not(pasouvert):
                fenetre2.destroy()
                del copie[0]
            pasouvert=True
            fichier=open("./map/"+nommap+".cp","r")
            lignes=fichier.readlines()

            num1=lignes[curseur1[3]/32+60]
            num1=num1[:curseur1[2]/32*2+2]
            num1=num1[curseur1[2]/32*2:]
            num=num1
            chemin="./messages/"+nommap+"."+num+"."+str(curseur1[2])+"."+str(curseur1[3])
            if num!="00":
                if not os.path.isfile(chemin):
                    fichier2=open(chemin,"w")
                    fichier2.close()
            fichier.close()

        # if touche=="p":
        #     if not(pasouvert):
        #         fenetre2.destroy()
        #         del copie[0]
        #     pasouvert=False
        #     i=0
        #     list = os.listdir('./messages')
        #     fenetre2=Toplevel(fenetre)
        #     liste = Listbox(fenetre2)
        #     for fiche in list:
        #         liste.insert(i,fiche)
        #         i+=1
        #     liste.pack()
        #     copie.append(liste)
        #     bouton=Button(fenetre2, text="Valider", command=validerMessage(bouton))
        #     bouton.pack()

            
        if touche=="space":
            posx=0
            posy=0
            mode+=1
            if mode>3:
                mode=0
                canvas.delete("all")
                for i in range(0,100):
                    if i<10:
                        if not(os.path.isfile("./spriteSurface/bloc"+"0"+str(i))):
                            break
                        else:
                            nom="./spriteSurface/bloc"+"0"+str(i)
                    else:
                        if not(os.path.isfile("./spriteSurface/bloc"+str(i))):
                            break
                        else:
                            nom="./spriteSurface/bloc"+str(i)
                               
                    placer(nom,posx,posy,canvas)
                    if(posx>=608):
                        posx=0
                        posy+=32
                    else:
                        posx+=32
            if mode==1:
                canvas.delete("all")
                for i in range(0,100):
                    if i<10:
                        if not(os.path.isfile("./spriteDecor/bloc"+"0"+str(i))):
                            break
                        else:
                            nom="./spriteDecor/bloc"+"0"+str(i)
                    else:
                        if not(os.path.isfile("./spriteDecor/bloc"+str(i))):
                            break
                        else:
                            nom="./spriteDecor/bloc"+str(i)
                    placer(nom,posx,posy,canvas)
                    if(posx>=608):
                        posx=0
                        posy+=32
                    else:
                        posx+=32
                
            elif mode==3:
                canvas.delete("all")
                for i in range(0,100):
                    if i<10:
                        if not(os.path.isfile("./spriteObjet/objet"+"0"+str(i))):
                            break
                        else:
                            nom="./spriteObjet/objet"+"0"+str(i)
                    else:
                        if not(os.path.isfile("./spriteObjet/objet"+str(i))):
                            break
                        else:
                            nom="./spriteObjet/objet"+str(i)
 
                    placer(nom,posx,posy,canvas)
                    if(posx>=608):
                        posx=0
                        posy+=32
                    else:
                        posx+=32
                        
            elif mode==2:
                canvas.delete("all")
                for i in range(0,100):
                    if i<10:
                        if not(os.path.isfile("./spriteEnnemi/Ennemi"+"0"+str(i))):
                            break
                        else:
                            nom="./spriteEnnemi/Ennemi"+"0"+str(i)
                    else:
                        if not(os.path.isfile("./spriteEnnemi/Ennemi"+str(i))):
                            break
                        else:
                            nom="./spriteEnnemi/Ennemi"+str(i)
                    placer(nom,posx,posy,canvas)
                    if(posx>=608):
                        posx=0
                        posy+=32
                    else:
                        posx+=32

def validerTP():
    global pasouvert
    global fenetre2
    pasouvert=True
    liste=copie[0]
    nom=liste.get(liste.curselection())
    fichier=open("./tp/"+nom,"w")
    fichier.write(nommap+"\n"+str(curseur1[2])+"\n"+str(curseur1[3]))
    fichier.close()
    del copie[0]
    fenetre2.destroy()

# def validerMessage(bouton):
#     global pasouvert
#     global fenetre2
#     liste=copie[0]
#     fenetre2.destroy()
#     entree = Entry(fenetre2, width=30)
#     entree.pack()
#     bouton=Button(fenetre2, text="Valider", command=validerMessage2(entree,liste))
#     bouton.pack()
    
# def validerMessage2(entree,liste):
#     i=0
#     pasouvert=True
#     ligne=""
#     nom=liste.get(liste.curselection())
#     fichier=open("./tp/"+nom,"w")
#     texte=copie[0].get()
#     for lettre in texte:
#         if i>60:
#             fichier.write(ligne+"\n")
#             i=0
#             ligne=""
#         ligne+=lettre
#         i+=1       
#     fichier.close()
#     del copie[0]
#     fenetre2.destroy()
                  
def placer_map():
    
    global commence
    global Bloc
    global nom
    global mode
    global nommap
    global ma_map

    cpt=0
    i=0
    if mode==0:
        nom="./spriteSurface/bloc"
    elif mode==1:
        nom="./spriteDecor/bloc"
    elif mode==2:
        nom="./spriteEnnemi/Ennemi"
    elif mode==3:
        nom="./spriteObjet/objet"

        
    if selection<10:
        nom2=nom+"0"+str(selection)
    else:
        nom2=nom+str(selection)
    print nom2
    if os.path.isfile(nom2):
        
        fichier=open("./map/"+nommap+".cp","r")
        lignes=fichier.readlines()
        fichier2=open("./map/"+nommap+".cp","w")
        
        for ligne in lignes:
            i=0
            while i<40:
                if cpt==curseur1[3]/32+(mode*20):
                    if i/2==curseur1[2]/32:
                        if i/2==0:
                            deb=""
                            fin=ligne[2:]
                        else:
                            deb=ligne[:i]
                            fin=ligne[i+2:]

                        ligne=deb+nom2[len(nom2)-2:]+fin
                i+=2        
            fichier2.write(ligne)
            cpt+=1
                
        fichier2.close()
        fichier.close()
        fichier=open("./map/"+nommap+".cp","r")
        lignes=fichier.readlines()
    
        ma_map[curseur1[2]/32+curseur1[3]/32*20]=[]
        ligney=curseur1[3]/32
        lignex=curseur1[2]/32
    
        num=lignes[ligney][lignex*2]+lignes[ligney][lignex*2+1]
        if num!="00":
            placer("./spriteSurface/bloc"+num,curseur1[2],curseur1[3],canvas2)
        else:
            canvas2.create_rectangle(curseur1[2],curseur1[3],curseur1[2]+32,curseur1[3]+32,outline="",fill="#0dac07")
        
        num=lignes[ligney+20][lignex*2]+lignes[ligney+20][lignex*2+1]
        placer("./spriteDecor/bloc"+num,curseur1[2],curseur1[3],canvas2)
        num=lignes[ligney+40][lignex*2]+lignes[ligney+40][lignex*2+1]
        placer("./spriteEnnemi/Ennemi"+num,curseur1[2],curseur1[3],canvas2)
        num=lignes[ligney+60][lignex*2]+lignes[ligney+60][lignex*2+1]
        placer("./spriteObjet/objet"+num,curseur1[2],curseur1[3],canvas2)

def effacer():
    global ma_map
    global commence
    global Bloc
    global nom
    global mode
    global nommap
    i=0

    if(commence==True):

        canvas2.create_rectangle(curseur1[2],curseur1[3],curseur1[2]+32,curseur1[3]+32,outline="",fill="#0dac07")
            
        ma_map[(curseur1[2]/32)+curseur1[3]/32*20]=[]
                
        cpt=0
        fichier=open("./map/"+nommap+".cp","r")
        lignes=fichier.readlines()
        fichier2=open("./map/"+nommap+".cp","w")

        for ligne in lignes:
            i=0
            while i<40:
                if cpt==curseur1[3]/32:
                    if i/2==curseur1[2]/32:
                        if i/2==0:
                            deb=""
                            fin=ligne[i+2:]
                        else:
                            deb=ligne[:i]
                            fin=ligne[i+2:]
                        ligne=deb+"00"+fin
                i+=2
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
    canvas =Canvas(fenetre, width=640, height=200)
    canvas.pack()
    canvas.focus_set()
    canvas2.pack()
    canvas2.focus_set()
    for i in range(0,100):
        if i<10:
            if not(os.path.isfile("./spriteDecor/bloc"+"0"+str(i))):
                break
            else:
                nom="./spriteDecor/bloc"+"0"+str(i)
        else:
            if not(os.path.isfile("./spriteDecor/bloc"+str(i))):
                break
            else:
                   nom="./spriteDecor/bloc"+str(i)
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
    i=0
    

    for ligne in lignes:
        i=0
        if cpt>=20:
            cpt=0
            h+=1
            j=0
        while i<40:
            num=ligne[i]+ligne[i+1]
            ma_map[i/32+j/32*20]=[]
            if(num!="00"):
                if h==0:
                    nom="./spriteSurface/bloc"
                elif h==1:
                    nom="./spriteDecor/bloc"
                elif h==3:
                    nom="./spriteObjet/objet"
                elif h==2:
                    nom="./spriteEnnemi/Ennemi"
                        
                nom+=num
                placer(nom,(i/2*32),j,canvas2)
            i+=2
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
    global fenetre2
    
    liste=copie[0]
    nommap=liste.get(liste.curselection())     
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
        del copie[0]
        commence=True
        affiche_terrain("./map/"+nommap)
        pasouvert=True
        fenetre2.destroy()
    else:
        print "Fichier inexistant"

    
def nouveau():
    global copie
    global pasouvert
    global fenetre2

    if not(pasouvert):
        del copie[0]
        fenetre2.destroy()
        
    pasouvert=False
    fenetre2=Toplevel(fenetre)
    entree = Entry(fenetre2, width=30)
    copie.append(entree)
    entree.pack()
    bouton=Button(fenetre2, text="Valider", command=validernom)
    bouton.pack()

def validernom():
    global copie
    global commence
    global efface
    global nommap
    global curseur1
    global curseur2
    global pasouvert
    global fenetre2

    nommap= copie[0].get()

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
        ligne="0000000000000000000000000000000000000000"
        for i in range(0,79):
            fichier.write(ligne+"\n")
        fichier.write(ligne)
        fichier.close()
        del copie[0]
        commence=True
        pasouvert=True
        fenetre2.destroy()

def editer():
    global copie
    global mode
    global pasouvert
    global fenetre2
    i=0
    if not(pasouvert):
        del copie[0]
        fenetre2.destroy()
        
    pasouvert=False
    mode=1
    maliste = os.listdir('./map')
    maliste.sort()
    fenetre2=Toplevel(fenetre)
    scrollbar = Scrollbar(fenetre2)
    scrollbar.pack(side=RIGHT, fill=Y)
    liste = Listbox(fenetre2,yscrollcommand=scrollbar.set)
    for fiche in maliste:
        if fiche[len(fiche)-2:]!="cp":
            liste.insert(i,fiche)
            i+=1
    scrollbar.config(command=liste.yview)
    liste.pack()
    copie.append(liste)
    bouton=Button(fenetre2, text="Valider", command=validernom2)
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

pasouvert=True


test()

fenetre.bind("<Key>", vitesse)
fenetre.bind("<KeyRelease>", stop)
fenetre.bind("<Button-1>", souris)
fenetre.bind("<B1-Motion>", souris)
fenetre.mainloop()

