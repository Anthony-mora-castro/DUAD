import csv

def add_games_csv(games, games_path='games.csv'):
    with open(games_path, 'w', newline='', encoding='utf-8') as file:
        headers = ['name', 'genre', 'developer', 'ESRB']
        writer_csv = csv.DictWriter(file, fieldnames=headers)
        writer_csv.writeheader()  
        for game in games:
            writer_csv.writerow(game)


def get_games_info(n):
    games = []
    for i in range(n):
        print(f'Ingrese la informaciÃ³n del videojuego: {i + 1}')
        name = input('Name: ')
        genre = input('Genre: ')
        developer = input('Developer: ')
        ESBR = input(' ESRB: ')

        game = {
            'name': name,
            'genre': genre,
            'developer': developer,
            'ESRB': ESBR  
        }
        games.append(game)
    return games 

def main():
    n = int(input('Ingrese la cantidad de juegos que desea ingresar: '))
    games = get_games_info(n)
    add_games_csv(games)
    print(f'Se han guardado {n} juegos en el archivo csv.')

if __name__ == "__main__":
    main()
