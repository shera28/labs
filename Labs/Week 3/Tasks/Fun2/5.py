def m(mm):
    Thriller = 0
    t = 0
    Action = 0
    ac = 0
    Adventure = 0
    ad = 0
    Drama = 0
    d = 0
    Romance = 0
    r = 0
    War = 0
    w = 0
    Crime = 0
    cr = 0
    Comedy = 0
    co = 0
    Suspense = 0
    s = 0

    for i in mm:
        if i['category'] == "Thriller":
            Thriller += i['imdb']
            t += 1
        elif i ['category'] == "Action":
            Action += i['imdb']
            ac += 1
        elif i ['category'] == "Adventure":
            Adventure+= i['imdb']
            ad += 1
        elif i ['category'] == "Drama":
            Drama+= i['imdb']
            d += 1
        elif i ['category'] == "Romance":
            Romance+= i['imdb']
            r += 1
        elif i ['category'] == "War":
            War+= i['imdb']
            w += 1
        elif i ['category'] == "Crime":
            Crime+= i['imdb']
            cr += 1
        elif i ['category'] == "Comedy":
            Comedy+= i['imdb']
            co += 1
        else:
            Suspense+= i['imdb']
            s += 1
    print('Thriller: ', Thriller / t)
    print('Action: ', Action / ac)
    print('Adventure: ', Adventure / ad)
    print('Drama: ', Drama / d)
    print('Romance: ', Romance/ r)
    print('War: ', War / w)
    print('Crime: ', Crime / cr)
    print('Comedy: ', Comedy / co)
    print('Suspense: ', Suspense / s)


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
