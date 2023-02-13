def m(mm):
    Thriller = []
    Action = []
    Adventure = []
    Drama = []
    Romance = []
    War = []
    Crime = []
    Comedy = []
    Suspense = []

    for i in mm:
        if i['category'] == "Thriller":
            Thriller.append(i['name'])
        elif i ['category'] == "Action":
            Action.append(i['name'])

        elif i ['category'] == "Adventure":
            Adventure.append(i['name'])

        elif i ['category'] == "Drama":
            Drama.append(i['name'])

        elif i ['category'] == "Romance":
            Romance.append(i['name'])

        elif i ['category'] == "War":
            War.append(i['name'])

        elif i ['category'] == "Crime":
            Crime.append(i['name'])

        elif i ['category'] == "Comedy":
            Comedy.append(i['name'])

        else:
            Suspense.append(i['name'])

    print('Thriller: ', Thriller)
    print('Action: ', Action)
    print('Adventure: ', Adventure)
    print('Drama: ', Drama)
    print('Romance: ', Romance)
    print('War: ', War)
    print('Crime: ', Crime)
    print('Comedy: ', Comedy)
    print('Suspense: ', Suspense)


movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

m(movies)
