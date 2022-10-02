from django import template
from ..models import Background, Pages
from ..models import MainPage
register = template.Library()

@register.simple_tag
def phone_numbers():
    about_cinema = MainPage.objects.all()[0]
    return f'<div class="col">{about_cinema.phone_number}</div><div class="col">{about_cinema.phone_number2}</div>'

@register.simple_tag
def background():
    back = Background.objects.all()[0]
    result = ''
    if back.is_photo:
        result = f'background-image: url({back.main_photo.url})'
    else:
        result = f'background-color: {back.color};'
    return result


@register.simple_tag
def pages_list(code):
    result = ''
    pages = Pages.objects.all()
    for page in pages:
        result += f'<li><a class="dropdown-item" style="color: gray" href="/{code}/pages/page/{page.seo.url}">{page.name}</a></li>'
    return result
