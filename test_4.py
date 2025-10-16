#### Imports et définition des variables globales
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

def cherche1(mots, start, stop, n):
    mots = read_data(FILENAME)
    sous_ensemble = set()
    taille = len(mots)
    len_start = len(start)
    len_stop = len(stop)
    if taille == 0:
        return 'ensemble_vide'
    for mot in mots:
        if n == len(mot) and mot[:len_start] == start and mot[-len_stop:] == stop : #[-len_stop:] signifie qu'on commence à la len_stop-ième lettre en partant de la fin de la chaîne jusqu'à la fin de la chaine de caractere
            sous_ensemble.add(mot)
    return sous_ensemble

def main():
    mots = read_data(FILENAME)
    return cherche1(mots,'sur', 'on', 17)

print(main())