def get_actor_film_n1_issue(cursor):
    cursor.execute("SELECT actor_id, first_name, last_name FROM actor ORDER BY actor_id ASC")
    actors = cursor.fetchall()

    result = []

    for actor_id, actor_firstName, actor_lastName in actors:
        cursor.execute("""
            SELECT DISTINCT f_a.film_id, film.title FROM actor JOIN film_actor f_a ON f_a.actor_id = %s
            JOIN film ON f_a.film_id = film.film_id
        """,(actor_id,))
        films = cursor.fetchall()
        result.append(
            {
                "Actor's FirstName" : actor_firstName,
                "Actor's LastName" : actor_lastName,
                "Actor's Films" : [
                    {"Film ID" : film_id, "Film Title" : film_title}
                    for film_id, film_title in films
                ]
            }
        )
