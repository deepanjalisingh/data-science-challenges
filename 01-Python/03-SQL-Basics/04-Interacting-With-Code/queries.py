# pylint: disable=missing-docstring, C0103

def directors_count(db):
    # return the number of directors contained in the database
    query = "SELECT COUNT(name) FROM directors"
    db.execute(query)
    results = db.fetchall() # results in a list (rows) of tuples (columns)
    return results[0][0]


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = "SELECT name FROM directors ORDER BY name"
    db.execute(query)
    results = db.fetchall()
    list_of_directors=[]
    for result in results:
        list_of_directors.append(result[0])
    return list_of_directors


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = """
        SELECT title FROM movies m WHERE title LIKE '% LOVE %'
        OR title LIKE 'LOVE %'
        OR title LIKE 'LOVE,%'
        OR title LIKE "LOVE'%"
        OR title LIKE "LOVE.%"
        OR title LIKE '% LOVE'
        OR title LIKE '% LOVE.%'
        OR title LIKE '% LOVE,%'
        OR title LIKE "% LOVE'%"
        OR title LIKE "%, LOVE%"
        or title in ('LOVE', 'Love')
        ORDER BY title
    """
    db.execute(query)
    results = db.fetchall()
    love_movie_list=[]
    for result in results:
        love_movie_list.append(result[0])
    return love_movie_list

def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = "SELECT COUNT(name) FROM directors WHERE name LIKE ?"
    #t = (name,)
    db.execute(query, (f"%{name}%",))
    results = db.fetchall()
    return results[0][0]

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = "SELECT title FROM movies WHERE minutes > ? ORDER BY title"
    #t=(min_length,)
    db.execute(query,(min_length,))
    results = db.fetchall()
    movie_list=[]
    for result in results:
        movie_list.append(result[0])
    return movie_list
