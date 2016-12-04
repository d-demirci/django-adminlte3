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

The [base template] is designed to be highly customisable. Template blocks are provided to
allow you to hook in customisations as you wish

### Admin Theme Usage

Install as per the above installation instructions. The django admin UI should then change as expected.

Documentation
-------------

Can be found at: http://django-adminlte2.readthedocs.io

Credits
-------

* dnaextrim for [django_adminlte_x]
* beastbikes for [django-adminlte]

django-adminlte2 is packaged using [seed].

  [seed]: https://github.com/adamcharnock/seed/
  [django_adminlte_x]: https://github.com/dnaextrim/django_adminlte_x
  [django-adminlte]: https://github.com/beastbikes/django-adminlte/
  [base template]: https://github.com/adamcharnock/django-adminlte2/blob/master/django_adminlte/templates/adminlte/base.html
