from hashlib import md5

from django import template
from django.conf import settings
from django.urls import reverse

register = template.Library()


@register.simple_tag()
def logout_url():
    return getattr(settings, 'LOGOUT_URL', '/logout/')


@register.simple_tag(takes_context=True)
def avatar_url(context, size=None):
    # TODO: Make behaviour configurable
    user = context['request'].user
    return 'https://www.gravatar.com/avatar/{hash}?s={size}&d=mm'.format(
        hash=md5(user.email.encode('utf-8')).hexdigest() if user.is_authenticated() else '',
        size=size or '',
    )


@register.simple_tag(takes_context=True)
def add_active(context, url_name, *args, **kwargs):
    exact_match = kwargs.pop('exact_match', False)

    path = reverse(url_name, args=args, kwargs=kwargs)
    if not exact_match and context.request.path.startswith(path):
        return ' active '
    elif exact_match and context.request.path == path:
        return ' active '
    else:
        return ''
