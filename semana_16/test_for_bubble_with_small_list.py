import pytest
from semana_15.Ejercicio_2_semana_15 import bubble_sort

def test_bubble_sort_with_small_list():
    """Prueba de ordenamiento de una lista popular"""
    list_of_ages = [1, 5, 4, 8, 6]
    expected = [1, 4, 5, 6, 8]  # Este es el resultado correcto ordenado
    bubble_sort(list_of_ages)
    assert list_of_ages == expected, f'Expected {expected}, got {list_of_ages}'
    
