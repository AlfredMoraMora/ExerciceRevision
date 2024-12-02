import pytest
from exercice1 import calculer_superficies

@pytest.mark.parametrize("lst_cercles, lst_superficies_attendu, min_sup_attendu, max_sup_attendu", [
   # Arrange
    ([1,2,3,4,5,6],[3.14, 12.56, 28.26, 50.24, 78.5, 113.04], 3.14, 113.04),
    (["sunny"], None, None, None),
    ([], None, None, None),
    ([-1], None, None, None)

])

def test_calculer_superficies(lst_cercles : list,
                              lst_superficies_attendu : list,
                              min_sup_attendu : float,
                              max_sup_attendu : float):

    # Act
    lst_superficies_obtenu, min_sup_obtenu, max_sup_obtenu = calculer_superficies(lst_cercles)

    # Assert
    """ 
    Il faut que les variables aient les mêmes types également. 
    """
    assert lst_superficies_obtenu == lst_superficies_attendu
    if isinstance(lst_superficies_obtenu, list):
        assert min_sup_obtenu == min_sup_attendu
        assert max_sup_obtenu == max_sup_attendu
        assert isinstance(lst_superficies_obtenu, list)
        assert isinstance(min_sup_obtenu, float) and  isinstance(max_sup_obtenu, float)
    else:
        assert isinstance(lst_superficies_obtenu, type(None)) and isinstance(min_sup_obtenu, type(None)) and isinstance(max_sup_obtenu, type(None))

