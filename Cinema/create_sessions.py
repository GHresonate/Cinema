from cinema_app.models import Session, Cinema, Hall, Movie
from datetime import timedelta, date, time
import random



def main():
    DAYS_WITH_SESSIONS = 100
    today = date.today()
    movies = Movie.objects.all()
    cinemas = Cinema.objects.all()

    for x in range(DAYS_WITH_SESSIONS):
        minutes = random.randint(0, 59)
        hour = random.randint(8, 22)
        t = time(hour=hour, minute=minutes)
        price = random.randint(80, 300)
        delta = timedelta(days=x)
        session_date = today+delta
        while True:
            movie = random.choice(movies)
            if movie.realise_date < today:
                break
        cinema = random.choice(cinemas)
        hall = random.choice(Hall.objects.all().filter(cinema=cinema))
        Session.objects.create(movie=movie,cinema=cinema,hall=hall, date=session_date,price=price, time=t)
        print(1)
