import csv
import datetime
import re
from datetime import date

document=open(r"Données Projet.xlsx - Feuil2.csv")
myreader=csv.reader(document)


dat="16-août-99"
def date_na(d):
    d=(re.split('[ ;-_.;/]', d))
    #if d[0].isnumeric()






   # print(date_na




d2="12;mars;2013"






#for i in tab:
 #  verification des numero valid/////////////////////////////////////////////////////////////////////
def Numero_valid(Numero):
    if not Numero.isupper() or len(Numero)!=7 or  Numero.isnumeric()  or  Numero.isalpha()  or not Numero.isalnum():
        return False
    else:
        return True


# pour verifier les nomes valides////////////////////////////////////////////////////////////////////
def nom_valid(fname):
    if fname!="":
        if fname[0].isalpha() and len(fname)>=2 and fname.isalpha():
            return True
        else:
            return False

#verification prenom valide//////////////////////////////////////////////////////////////////////////
def prenom_valid(sname):
    if sname[0].isalpha and len(sname) >= 3 and sname.isalpha():
        return True
    else:
        return False
#verification des class valid////////////////////////////////////////////////////
def classe_valide(classe):
    cl=[3,4,5,6]
    cls=[ 'A' ,'B']
    if classe != "":

        if classe[0] in cl and classe[-1] in cls:
            return True
        else:
              return classe[0]+"em"+classe[-1]


#/////////////////////////////////////////////////////////////////////////////////////////////////////////
#calule moyenn_genral
#Nte="Math[8;13;13:16] #Francais[08;17:12] #Anglais[13;13:12] #PC[09;18:07] #SVT[15;10:10] #HG[14;19:17]"
def Note_valid(Note):
    Note=Note.split("#")
    liste=""
    som = 0

    l=0
    if Note!="":
        for k in range(len(Note)):
            l=0
            sub0=Note[k]

            sub_m1=sub0.split("[")


            for s in sub_m1[1]:
                if s==":":
                    l=l+1
            if l!=1:
                return False
            else:

                sub_m1 = str(sub_m1[1]).replace("]","")

                sub_m1 = sub_m1.split(":")


                noteco=sub_m1[1]

                notedev=sub_m1[0]


                if noteco=="" or int(noteco) < 0 or int(noteco) > 20:
                    return False
                else:
                   notedev=notedev.split(";")

                   some_note = 0
                   for l in range(len(notedev)):

                        if notedev[l]=="" or int(notedev[l]) > 20 or int(notedev[l]) <0  :
                         return False
                        else:
                            some_note=some_note+int(notedev[l])
                            #moy_en des notes
                            myn = some_note / len(notedev)
                            #moy_enn_matier_et_compo
                            moyenmat = round((myn + 2 * float(noteco)) / 3, )
                            print(moyenmat)


print(Note_valid(ste))
#///////////////::::::::::::::: Note valid
print("liste valid")
for element in docum:
    numero = element[1]
    nom=element[2]
    prenom=element[3]
    birth=element[4]
    classe=element[5]
    Note=element[6]
    tab1=[]


    #print(clas)

    if  nom_valid(nom)  and Numero_valid(numero) and prenom_valid(prenom) and classe_valide(classe) and Note_valid(Note):
        tab1.append([numero,nom,prenom,classe,Note])

        print(tab1)
print("liste invalid")
for element in docum:
    numero = element[1]
    nom=element[2]
    prenom=element[3]
    birth=element[4]
    classe=element[5]
    Note=element[6]
    tab2=[]
    if not Numero_valid(numero) or not nom_valid(nom) or not prenom_valid(prenom) :
        tab2.append([numero,nom,prenom,classe])

        print(tab2)