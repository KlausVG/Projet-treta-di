# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:28:39 2021

@author: julia
"""



import pandas

import os


FichDi = [ f for f in os.listdir('C:/Users/julia/Documents/GitHub/Projet-treta-di/DonneesPython/Donnees_dimers') if os.path.isdir(os.path.join('C:/Users/julia/Documents/GitHub/Projet-treta-di/DonneesPython/Donnees_dimers',f)) ]

FichTri = [ f for f in os.listdir('C:/Users/julia/Documents/GitHub/Projet-treta-di/DonneesPython/Donnees_trimers') if os.path.isdir(os.path.join('C:/Users/julia/Documents/GitHub/Projet-treta-di/DonneesPython/Donnees_trimers',f)) ]


print (FichDi + FichTri)

pathdi = "C:/Users/julia/Documents/GitHub/Projet-treta-di/DonneesPython/Donnees_dimers"
pathtri= "C:/Users/julia/Documents/GitHub/Projet-treta-di/DonneesPython/Donnees_trimers"

con = pandas.core.frame.DataFrame()

for i in FichDi :
    df = pandas.read_csv( pathdi +"/" + i + "/" + "freqAASurfaceInterface_"+ i +  '.csv')
    
    df['nom']= i 
    con = pandas.concat([con, df], axis=0)
    
    
con.to_csv("C:/Users/julia/Documents/GitHub/Projet-treta-di/freqAASurfaceInterfaceDi") 

con1 = pandas.core.frame.DataFrame()

for i in FichTri :
    df = pandas.read_csv( pathdi +"/" + i + "/" + "freqAASurfaceInterface_"+ i +  '.csv')
    
    df['nom']= i 
    con1 = pandas.concat([con1, df], axis=0)
    
    
con1.to_csv("C:/Users/julia/Documents/GitHub/Projet-treta-di/freqAASurfaceInterfaceTri") 
# =============================================================
# =============================================================
# =============================================================

con = pandas.core.frame.DataFrame()

for i in FichDi :
    df = pandas.read_csv( pathdi +"/" + i + "/" + "freqTypesAASurfaceInterface_"+ i +  '.csv')
    
    df['nom']= i 
    con = pandas.concat([con, df], axis=0)
    
    
con.to_csv("C:/Users/julia/Documents/GitHub/Projet-treta-di/freqTypesAASurfaceInterface_Di") 

con1 = pandas.core.frame.DataFrame()

for i in FichTri :
    df = pandas.read_csv( pathdi +"/" + i + "/" + "freqTypesAASurfaceInterface_"+ i +  '.csv')
    
    df['nom']= i 
    con1 = pandas.concat([con1, df], axis=0)
    
    
con1.to_csv("C:/Users/julia/Documents/GitHub/Projet-treta-di/freqTypesAASurfaceInterface_Tri") 

# =============================================================
# =============================================================
# =============================================================

con = pandas.core.frame.DataFrame()

for i in FichDi :
    df = pandas.read_csv( pathdi +"/" + i + "/" + "tailleSurfaceInterface_"+ i +  '.csv')
    
    df['nom']= i 
    con = pandas.concat([con, df], axis=0)
    
    
con.to_csv("C:/Users/julia/Documents/GitHub/Projet-treta-di/tailleSurfaceInterface_Di") 

con1 = pandas.core.frame.DataFrame()

for i in FichTri :
    df = pandas.read_csv( pathdi +"/" + i + "/" + "tailleSurfaceInterface_"+ i +  '.csv')
    
    df['nom']= i 
    con1 = pandas.concat([con1, df], axis=0)
    
    
con1.to_csv("C:/Users/julia/Documents/GitHub/Projet-treta-di/tailleSurfaceInterface_Tri") 










