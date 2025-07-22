import pytest
from semana_15.Ejercicio_2_semana_15 import bubble_sort

def test_bubble_list_with_large_list():

    import random
    list_of_ages = [random.randint(1, 1000) for _ in range(150)]
    expected = sorted(list_of_ages)  # Este es el resultado correcto ordenado
    bubble_sort(list_of_ages)
    assert list_of_ages == expected, f'Expected {expected}, got {list_of_ages}'
    
