from modeltranslation.translator import translator, TranslationOptions
from .models import NewsAndDiscount


class NewsAndDiscTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(NewsAndDiscount, NewsAndDiscTranslationOptions)
