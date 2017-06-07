Quickstart
==========

Install the pip package::

    pip install django-adminlte2

Add the apps to ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS = [
        # Any apps which will override adminlte's templates (i.e. your apps)
        ...

        # The general purpose templates
        'django_adminlte',

        # Optional: Skin for the admin interface
        'django_adminlte_theme',

        # Any apps which need to have their templates overridden by adminlte
        'django.contrib.admin',
        ...
    ]

.. important::

    Take note of the ordering of ``INSTALLED_APPS``. If you find templates are not
    being found & used as expected it is probably due to a problem here.

    Django looks for a template in the order in which apps are listed in
    ``INSTALLED_APPS``, hence the ordering above.

If you only wish to skin the admin interface, you can stop here. Your admin
interface should now be displaying with the AdminLTE theme.

You can also make use of the AdminLTE theme for your app. This may be particularly
useful for internal (non-public) apps which need a quick and effective layout.

Using the templates in your app
-------------------------------

The base AdminLTE template provides much of what you need, but you'll need to customise
it in some ways to meet your needs. In particular, no navigation is provided (we'll cover
this shortly).

To add & modify the functionality of the base template you should create your own base
template. This template should extend ``adminlte/base.html``. Several blocks are available
for you to extend.

.. code:: jinja

    {% extends 'adminlte/base.html' %}

    {% block title %}My App{% endblock %}
    {% block content %}
        Just some example content
    {% endblock %}

Take a look at the base template to see the available blocks.

Adding navigation
-----------------

The base template includes a number of other templates in order to create the whole.

For example, the sidebar navigation resides in ``adminlte/lib/_main_sidebar.html``. To customise
this template you should create a template of the same path & name in your app's templates folder.

.. important::

    Your app(s) must be listed before ``django_adminlte2`` in ``INSTALLED_APPS``. Otherwise
    Django will find the default default provided by ``django-adminlte2`` before your customised one.

In **your own app** create the template ``adminlte/lib/_main_sidebar.html``:

.. code:: jinja

    {% extends 'adminlte/lib/_main_sidebar.html' %}

    {% block nav_links %}
        <li>
            <a href="/some/url">
                <i class="fa fa-dashboard"></i> <span>Home</span>
            </a>
        </li>
        <li>
            <a href="/some/url">
                <i class="fa fa-user"></i> <span>Users</span>
            </a>
        </li>
    {% endblock nav_links %}

You should now find the navigation has updated.
