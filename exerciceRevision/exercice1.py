
def calculer_superficies(rayons: list):
    """
    Permet de calculer les superficies de la liste de rayons entrées par la liste 'rayons'
    :param rayons: Liste de rayons de cercle
    :return: La liste de superficies de rayons entrés et la superficie min et la superficie max.
    """
    PI = 3.14
    superficies = []
    try:
        for rayon in rayons:
            if rayon < 0:
                return None, None, None
            superficies.append(rayon*rayon*PI)

        min_superficie = min(superficies)
        max_superficie = max(superficies)
    except (TypeError, ValueError):
        return None, None, None

    return superficies, min_superficie, max_superficie

if __name__ == '__main__':
    list_rayons = [4, 5, 2, 6]
    lst_superficie, min_superficie, max_superficie = calculer_superficies(list_rayons)

    print(calculer_superficies(list_rayons))

