def bubble_sort_words(words):  # O(n²)
    n = len(words)  # O(1)
    for index in range(n):  # O(n)
        for inside_index in range(0, n-index-1):  # O(n)
            if words[inside_index] > words[inside_index+1]:  # O(1)
                words[inside_index], words[inside_index+1] = words[inside_index+1], words[inside_index]  # O(1)
    return words  # O(1)

words = ["banano", "manzana", "pera", "uva", "cereza"]  # O(1)
print("Lista original:", words)  # O(n)
sorted_words = bubble_sort_words(words)  # O(n²)
print("Lista ordenada:", sorted_words)  # O(n) 
