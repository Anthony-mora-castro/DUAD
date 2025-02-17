list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

dict = {}
for i in range(len(list_a)):
    dict[list_a[i]] = list_b[i]

print(dict)