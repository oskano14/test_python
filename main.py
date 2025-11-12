def Chiffre_cesar(texte, decalage):
    message_chiffre = ""
    for char in texte:
        new_position = (ord(char) + decalage) % 257
        new_char = chr(new_position)
        message_chiffre += new_char

    return message_chiffre

test = "ne dors pas ."
decalage = 3
resultat = Chiffre_cesar(test, decalage)
print("Texte original :", test)
print("Texte chiffré  :", resultat)


def Dechiffre_cesar(texte, decalage):
    return Chiffre_cesar(texte, -decalage)

texte_dechiffre = Dechiffre_cesar(resultat, decalage)
print("Texte déchiffré:", texte_dechiffre)

brute_force_result = []
for decalage in range(257):
    brute_force_result.append(Dechiffre_cesar(resultat, decalage))

print("Résultats du brute-force :")
for decalage, texte in enumerate(brute_force_result):
    print(f"Décalage {decalage}: {texte}")


key = [1, 2, 3, 4, 5]

def chiffre_viginere(texte, key):
    message_chiffre = ""
    key_length = len(key)
    for index, char in enumerate(texte): 
        decalage = key[index % key_length]
        message_chiffre += Chiffre_cesar(char, decalage)
    return message_chiffre

texte_viginere = "Ceci est un texte pour le chiffre de Viginere."
texte_chiffre_viginere = chiffre_viginere(texte_viginere, key)
print("Texte Viginere original :", texte_viginere)
print("Texte Viginere chiffré  :", texte_chiffre_viginere)

   

def dechiffre_viginere(texte, key):
    message_dechiffre = ""
    key_length = len(key)
    for index, char in enumerate(texte):
        decalage = key[index % key_length]
        message_dechiffre += Dechiffre_cesar(char, decalage)
    return message_dechiffre

texte_dechiffre_viginere = dechiffre_viginere(texte_chiffre_viginere, key)
print("Texte Viginere déchiffré:", texte_dechiffre_viginere)


 