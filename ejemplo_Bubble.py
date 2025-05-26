def bubble_sort_words(words):
    n = len(words)
    for index in range(n):

        for inside_index in range(0, n-index-1):

            if words[inside_index] > words[inside_index+1]:

                words[inside_index], words[inside_index+1] = words[inside_index+1], words[inside_index]
                
    return words

# Ejemplo de uso
words = ["banano", "manzana", "pera", "uva", "cereza"]
print("Lista original:", words)
sorted_words = bubble_sort_words(words)
print("Lista ordenada:", sorted_words)