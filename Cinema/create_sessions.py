from cinema_app.models import Session, Cinema, Hall, Movie
from datetime import timedelta, date, datetime
import random



def main():
    DAYS_WITH_SESSIONS = 100
    today = date.today()
    today_dtm = datetime(year=today.year, month=today.month, day=today.day)
    movies = Movie.objects.all()
    cinemas = Cinema.objects.all()

    for x in range(DAYS_WITH_SESSIONS):
        minutes = random.randint(0, 60)
        hour = random.randint(8, 22)
        price = random.randint(80, 300)
        delta = timedelta(days=x, hours=hour, minutes=minutes)
        session_date = today_dtm+delta
        while True:
            movie = random.choice(movies)
            if movie.realise_date < today:
                break
        cinema = random.choice(cinemas)
        hall = random.choice(Hall.objects.all().filter(cinema=cinema))
        Session.objects.create(movie=movie,cinema=cinema,hall=hall, date=session_date,price=price)
        print(1)
