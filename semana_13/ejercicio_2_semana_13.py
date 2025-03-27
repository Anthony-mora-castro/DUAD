def Only_numbers(func):
    def wrapper(*args, **kwargs):
       print(f'Args: {args}, Kwargs: {kwargs}')
       for arg in args:
           if not isinstance(arg, (int, float)):
               raise TypeError (f'The parameter {arg} is not a number')
           
       for key, value in kwargs.items():
           if not isinstance(value, (int, float)):
               raise TypeError(f'The kwarg {value} is not a number')
       return func(*args, **kwargs)
    return wrapper

@Only_numbers
def Normal_function(a,b, **kwarg):
    sum = a + b
    return sum

result = Normal_function(1, 2, My_kwarg = 3.14, my_second_kwarg = 0)
print("the result is: ", result)  # Imprime "La suma es: 3"


