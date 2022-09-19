from modeltranslation.translator import translator, TranslationOptions
from .models import Cinema, Movie, Hall


class CinemaTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class HallTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(Cinema, CinemaTranslationOptions)
translator.register(Movie, MovieTranslationOptions)
translator.register(Hall, HallTranslationOptions)

