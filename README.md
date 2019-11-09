AdminLTE Templates, Template Tags, and Admin Theme for Django
=============================================================

[![pypi_badge](https://badge.fury.io/py/django-adminlte3.png)](pypi.python.org/pypi/django-adminlte3)

Django AdminLTE3 provides the functionality of the AdminLTE3 theme
to developers in the form of standard base templates. Optional styling for
Django's built-in admin interface is also provided.

Installation
------------

Installation using pip:

    pip install django-adminlte3

Add to installed apps:

    INSTALLED_APPS = [
         # General use templates & template tags (should appear first)
        'adminlte3',
         # Optional: Django admin theme (must be before django.contrib.admin)
        'adminlte3_theme',

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

Can be found at: http://django-adminlte3.readthedocs.io

Credits
-------

This project a based heavily on work by the following:

* dnaextrim for [django_adminlte_x]
* beastbikes for [django-adminlte]
* adamcharnock for [django-adminlte2]

django-adminlte3 is packaged using twine.

  [django_adminlte_x]: https://github.com/dnaextrim/django_adminlte_x
  [django-adminlte]: https://github.com/beastbikes/django-adminlte/
  [base template2]: https://github.com/adamcharnock/django-adminlte2/blob/master/django_adminlte/templates/adminlte/base.html
  [base template]: https://github.com/d-demirci/django-adminlte3/blob/master/adminlte3/templates/adminlte/base.html

screenshots
![admin screenshot](https://user-images.githubusercontent.com/24219129/68517929-b39f4480-029a-11ea-9c34-4961fb3f5bf6.png)

![model screenshot](https://user-images.githubusercontent.com/24219129/68517976-e6e1d380-029a-11ea-8cde-b8373fce301b.png)