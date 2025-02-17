def name_of_songs(names_path, text):
        with open(names_path, 'w', encoding='utf-8') as file:
                file.write(text)

text_to_write = """
        Despacito de Luis Fonsi ft Daddy Yankee.
        Shape of you de Ed Sheeran. 
        See you again de Wiz Khalifa. 
        Uptown Funk de Mark Ronson ft Bruno Mars. 
        Sugar de Marron 5. 
        Dame tu cosita de El Chombo. 
        Sorry de Justin Bieber. 
        Roar de Katy Perry.
        """

name_of_songs("names.txt", text_to_write)

def names_in_order(names_sort_path, output_path):
                with open(names_sort_path, 'r', encoding='utf-8') as file:
                        songs = file.read().splitlines()
        
                songs = [song.lower() for song in songs]  
                songs.sort()  

                with open(output_path, 'w', encoding='utf-8') as file:
                        for song in songs:
                                file.write(song + '\n')  

names_in_order("names.txt", "names_in_order.txt")