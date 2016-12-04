AdminLTE Templates, Template Tags, and Admin Theme for Django
=============================================================

[![pypi_badge](https://badge.fury.io/py/django-adminlte2.png)](pypi.python.org/pypi/django-adminlte2)

Django AdminLTE2 provides the functionality of the AdminLTE2 theme
to developers in the form of standard base templates. Optional styling for
Django's built-in admin interface is also provided.

Installation
------------

Installation using pip:

    pip install django-adminlte2

Add to installed apps:

    INSTALLED_APPS = [
         # General use templates & template tags (should appear first)
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

This project a based heavily on work by the following:

* dnaextrim for [django_adminlte_x]
* beastbikes for [django-adminlte]

django-adminlte2 is packaged using [seed].

  [seed]: https://github.com/adamcharnock/seed/
  [django_adminlte_x]: https://github.com/dnaextrim/django_adminlte_x
  [django-adminlte]: https://github.com/beastbikes/django-adminlte/
  [base template]: https://github.com/adamcharnock/django-adminlte2/blob/master/django_adminlte/templates/adminlte/base.html
