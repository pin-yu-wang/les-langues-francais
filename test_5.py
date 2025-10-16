### Imports et définition des variables globales
import csv
import random

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

#### Fonctions secondaires


def read_data(FILENAME):
    mots = []
    with open(FILENAME, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            mots.append(ligne.strip())  # Supprime les sauts de ligne
    return mots

def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
    sous_ensemble = set()
    taille = len(mots)
    if taille == 0:
        return 'ensemble_vide'
    for mot in mots:
        if nmin<len(mot)<nmax:
            for i in lstart:
                if mot.startswith(i):
                    for k in lmid:
                        if k in mot[1:len(mot)]:
                            for j in lstop:
                                if mot.endswith(j):
                                    sous_ensemble.add(mot)
    return sous_ensemble
    
#for mot in mots:
#   for i in range(len(mot)):
#      if n == len(mot) and mot[:len_start] == start and mot[-len_stop:] == stop : #[-len_stop:] signifie qu'on commence à la len_stop-ième lettre en partant de la fin de la chaîne jusqu'à la fin de la chaine de caractere
#         sous_ensemble.add(mot)
#return sous_ensemble

def main():
    mots = read_data(FILENAME)
    return cherche2(mots,VOYELLES, 'ç' ,CONSONNES,8,12)

print(main())