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

def ensemble_mots(FILENAME):
    ensemble = set()
    mots = read_data(FILENAME)
    if mots is None:
        return None
    for i in range(len(mots)):
        ensemble.add(mots[i])
    return ensemble # set de mots

def main():
    mots = read_data(FILENAME)
    test = ("chronophage", "procrastinateur", "dangerosité", "gratifiant" )
    tous_present = True
    for mot in test:
        if mot not in mots:
            tous_present = False
            break
    return tous_present

if __name__ == "__main__":
    resultat = main()
    print("Tous les mots sont présents dans le fichier :", resultat)
