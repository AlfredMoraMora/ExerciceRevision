# Un organisme à

def afficher_nom_donateurs(dictionnaire):
    """
    Permet de retourner et d'afficher la liste des noms des donateurs avec les noms des donatuers
    ayant fait des dons > 1000$ écrits de manière spectaculaire (avec des étoiles entres les caractères)
    :param dictionnaire: Dictionnaire qui contient les noms et la liste des dons des donateurs
    :return: la liste des donateurs
    """
    noms_donateurs = []
    genereux = False
    for nom, dons in dictionnaire.items():
        total_don = sum(dons) # Calculer le total des dons
        if total_don > 10000:
            genereux = True
        if total_don > 1000:

            nom_spectaculaire = ""
            for car in nom:
                nom_spectaculaire = nom_spectaculaire + car + "*"
            noms_donateurs.append(nom_spectaculaire)
            print(f"{nom_spectaculaire}")
        else:
            # Sinon, afficher le nom normalement
            noms_donateurs.append(nom)
            print(nom)
    return noms_donateurs, genereux


if __name__ == "__main__":

    # Dictionnaire des donateurs et leurs dons
    donateurs = {
        "Alice": [1500, 300, 250],
        "Bob": [500, 200],
        "Charlie": [1200, 500],
        "David": [400, 200]
    }

    # Appel de la fonction
    print(afficher_nom_donateurs(donateurs))