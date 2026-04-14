def get_actor_film_n1_resolved_issue(cursor):
    cursor.execute("""
    SELECT DISTINCT actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title
    FROM actor JOIN film_actor on film_actor.actor_id = actor.actor_id
    JOIN film ON film_actor.film_id = film.film_id 
    ORDER BY actor.actor_id ASC
    """)
    films = cursor.fetchall()