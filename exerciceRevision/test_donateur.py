import pytest
from donateur import afficher_nom_donateurs

@pytest.mark.parametrize('donateur, expected, genereux', [
    # Arrange
    ({"Alice": [1500, 300, 250], "Bob": [500, 200],
        "Charlie": [1200, 500], "David": [400, 200]},
     ['A*l*i*c*e*', 'Bob', 'C*h*a*r*l*i*e*', 'David'], False),
    ({}, [], False)
])
def test_afficher_nom_donateurs(donateur, expected, genereux):
    # Act
    noms_donateurs_obtenus, est_genereux = afficher_nom_donateurs(donateur)

    # Assert
    assert noms_donateurs_obtenus == expected
    assert isinstance(noms_donateurs_obtenus, list)
    assert isinstance(est_genereux, bool)
    assert (len(noms_donateurs_obtenus)) == len(donateur)
    assert genereux == False
    # for donors in noms_donateurs_obtenus:
    #     assert isinstance(donors, dict)
