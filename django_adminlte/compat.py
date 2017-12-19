import django


def is_authenticated(user):
    if django.VERSION >= (2, 0):
        return user.is_authenticated
    else:
        return user.is_authenticated()
