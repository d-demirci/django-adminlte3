Reusable AdminLTE Templates, Template Tags, and Admin Theme
===========================================================

[![pypi_badge](https://badge.fury.io/py/django-adminlte2.png)](pypi.python.org/pypi/django-adminlte2)

Installation
------------

Installation using pip:

    pip install django-adminlte2

Add to installed apps:

    INSTALLED_APPS = [
         # General use templates & template tags
        'django_adminlte',
         # Optional: Django admin theme (must be before django.contrib.admin)
        'django_adminlte_theme',

        ...
    ]

Usage
-----

General purpose templates & tags coming soon

### Admin Theme Usage

Install as per the above installation instructions. The django admin UI should then change as expected.

Credits
-------

* dnaextrim for [django_adminlte_x]
* beastbikes for [django-adminlte]

django-adminlte2 is packaged using [seed].

  [seed]: https://github.com/adamcharnock/seed/
  [django_adminlte_x]: https://github.com/dnaextrim/django_adminlte_x
  [django-adminlte]: https://github.com/beastbikes/django-adminlte/
