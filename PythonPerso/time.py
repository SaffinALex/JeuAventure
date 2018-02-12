#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
        
fenetre = Tk()

canvas = Canvas(fenetre, width=640, height=639, background="#F5F5DC")
mapx=1
mapy=1
Deplacement=0
MonPerso=[0,0,0,0]
MonEnnemi=[0,0,100,150]
Bloque_y=[]
Bloque_x=[]
Ennemi=[]
Joueur=canvas.create_rectangle(MonPerso[2],MonPerso[3],MonPerso[2]+32,MonPerso[3]+32,fill="blue",outline="")
canvas.pack()
canvas.focus_set()


        
fenetre.mainloop()
fichier = open("map1-1",'r')
lignes  = fichier.readlines()
for ligne in lignes:
    print ligne[0]
    print ligne[1]
