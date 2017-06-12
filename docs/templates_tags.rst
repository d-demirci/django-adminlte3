Templates & Blocks Reference
============================

.. contents::


Some utility template tags are provided which you may find useful.

``{% add_active %}``
--------------------

Returns the string ``" active "`` if the current url matches the one
provided. You may find this useful in your ``lib/_main_sidebar.html``
template.

Example::

    <li class="{% add_active 'myapp:detail' object.pk %}">
        <a href="{% url 'myapp:detail' object.pk %}">Details</a>
    </li>

This will normally match any URL which starts with the provided value. Therefore
the 'active' class will be applied for child pages too.

You can also specify the ``exact_only`` parameter which will override this behaviour.
This is often useful for the home page::

    <li class="{% add_active 'myapp:home' exact_match=True %}">
        <a href="{% url 'myapp:home' %}">Home</a>
    </li>

``{% avatar_url %}``
--------------------

Used in the based templates to find an avatar for the current user
(uses Gravatar_).

``{% logout_url %}``
--------------------

Used in the based templates to determine the default logout url by
looking for the ``LOGOUT_URL`` setting.



.. _Gravatar: https://gravatar.com/
