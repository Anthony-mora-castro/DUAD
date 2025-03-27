from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        # Ajuste si aún no ha pasado el cumpleaños este año
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age  # ← Ahora devuelve solo el número (int)

def Check_if_is_adult(func):
    def wrapper(user: User, *args, **kwargs):
        if user.age < 18:
            raise ValueError(f'The user is under 18 years (age: {user.age})')  # Cambiado a ValueError
        return func(user, *args, **kwargs) 
    return wrapper

@Check_if_is_adult
def Get_Drivers_license(user: User):
    return f'You can get your drivers license because you have more than 18 years (age: {user.age})'

adult = User(date(2006, 5, 15))
print(Get_Drivers_license(adult))
