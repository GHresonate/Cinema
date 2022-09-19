from modeltranslation.translator import translator, TranslationOptions
from .models import NewsAndDiscount, Pages


class NewsAndDiscTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class PagesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(NewsAndDiscount, NewsAndDiscTranslationOptions)
translator.register(Pages, PagesTranslationOptions)

