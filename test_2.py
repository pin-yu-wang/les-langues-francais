#### Imports et définition des variables globales
import csv
import random

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")
def read_data(FILENAME):
    mots = []
    with open(FILENAME, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            mots.append(ligne.strip())  # Supprime les sauts de ligne
    return mots



def mots_de_n_lettres(mots, n):
    sous_ensemble = set()
    taille = len(mots)
    if taille == 0:
        return None
    for mot in mots:
        if n == len(mot):
            sous_ensemble.add(mot)
    return sous_ensemble

def main():
    mots = read_data(FILENAME)
    return mots_de_n_lettres(mots,7)


print(len(main()))