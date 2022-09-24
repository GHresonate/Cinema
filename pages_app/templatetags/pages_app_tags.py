from django import template
from ..models import Background, Pages


register = template.Library()


@register.simple_tag
def background():
    back = Background.objects.get(id=1)
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
