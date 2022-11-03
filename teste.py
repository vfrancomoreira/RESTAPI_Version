hoteis = [
    {
        'hotel_id': 1,
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.0,
        'cidade': 'Santa Catarina'
    },
    {
        'hotel_id': 2,
        'nome': 'Delta Hotel',
        'estrelas': 5.0,
        'diaria': 320.0,
        'cidade': 'Santa Catarina'
    },
    {
        'hotel_id': 3,
        'nome': 'Bravo Hotel',
        'estrelas': 4.6,
        'diaria': 320.0,
        'cidade': 'Santa Catarina'
    },
    
]

# Acesso ao hotel especifico
# print(hoteis[1])

# Acesso ao valor do dicionario
# print(hoteis[1]['nome'])        
# Delta Hotel

def get(hotel_id):
    for hotel in hoteis:
        if hotel['hotel_id'] == hotel_id:
            return hotel
    return {'message': 'Hotel not found.'}, 404