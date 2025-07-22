from semana_15.Ejercicio_2_semana_15 import bubble_sort

def test_bubble_sort_with_empty_list():
    data = []
    expected = []
    bubble_sort(data)
    assert data == expected, f'Expected {expected}, got {data}'