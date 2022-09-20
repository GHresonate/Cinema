from django import template
from ..models import Background


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
