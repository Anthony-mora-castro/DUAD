def Return_Args_and_Kwargs(func):
    def wrapper(*args, **kwargs):
        print(f'Args: {args}, Kwargs: {kwargs}')
        result = func(*args, **kwargs) 
        
        return result

    return wrapper

@Return_Args_and_Kwargs
def My_Function(parameter1, parameter2, **kwargs):
    sum = parameter1 + parameter2
    return sum

result1 = My_Function(5,5, My_kwarg= 'hola')
print(result1)
