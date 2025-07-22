import pytest
from semana_15.Ejercicio_2_semana_15 import bubble_sort

def test_bubble_sort_with_incorrect_parameters():
    with pytest.raises(TypeError):
        bubble_sort("no es una lista")
    with pytest.raises(TypeError):
        bubble_sort(123)