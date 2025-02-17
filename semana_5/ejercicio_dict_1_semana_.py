my_hotel = [
    { 
    "name" : "RIU",
    "stars": "4 estrellas",
    "rooms" : [
        {
        "type": "estandar",
        "number": "De la 1 a la 200",
        "price" : "$150 por noche para 4 personas",
        "floor" : "Del piso 1 al 3"
        },
        
        {
        "type": "VIP",
        "number": "de la 201 a la 299 ",
        "price" : "$399 por noche para 4 personas",
        "floor" : "del piso 4 al 5"
        },

        {
        "type": "suit",
        "number": "300 y 301",
        "price" : "$1000 por noche para 4 personas",
        "floor" : "piso 6 y 7 "   
        }
    ]
}
]
print(my_hotel[0]["rooms"][2])