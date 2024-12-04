def entrer_locataires():
    locataires = {}
    while True:
        nom = input("Entrez le nom du locataire (ou 'q' pour terminer) : ")
        if nom.lower == 'q':
            break
        numero = input("Entrez le numero d'appartement : ")
        locataires[nom] = numero
    return locataires