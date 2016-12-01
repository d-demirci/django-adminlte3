Templates & Blocks Reference
============================

.. contents::


Below you will find reference for each available template, and the blocks that
can be overridden.

Note than when overriding some blocks it may make sense to make use of
``{{ block.super }}`` (`inheritance docs`_).

Base templates
--------------

adminlte/base.html
~~~~~~~~~~~~~~~~~~

The primary base template which provides a sidebar, top navigation with user information, and footer.

Commonly used blocks
""""""""""""""""""""

* `title`_
* `page_name`_
* `page_description`_
* `content`_
* `stylesheets`_
* `javascript`_

Block reference
"""""""""""""""

``title_outer``
'''''''''''''''

    Wrapper around the the outside of the ``<title>`` tag. Default::

        {% block title_outer %}
            <title>{% block title %}{{ site.name }}{% endblock %}</title>
        {% endblock %}


``title``
'''''''''

    Contents of the pages ``<title>`` tag. Default::

        <title>{% block title %}{{ site.name }}{% endblock %}</title>

    This will set a sensible default if the ``site`` variable references the current site object
    (from Django's `sites framework`_)

``meta``
''''''''

    All ``<meta>`` tags which appear in the pages ``<head>``. Default::

        {% block meta %}
            <meta charset="utf-8">
            <meta http-equiv="X-UA-COMPATIBLE" content="IE=edge">
            <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
        {% endblock %}

    Consider making use of ``{{ block.super }}`` when overriding this block.

``stylesheets``
'''''''''''''''

    All ``<style>`` tags which appear in the pages ``<head>``. By default this includes all content
    from ``adminlte/lib/_styles.html``.

    Consider making use of ``{{ block.super }}`` when overriding this block.

``extra_head``
''''''''''''''

    Additional HTML to be placed before the ``</head>`` tag. Empty by default.

``body_class``
''''''''''''''

    Additional CSS classes which can be placed into the ``<body>`` tag's ``class`` attribute.

``nav_header``
''''''''''''''

    Wrapper around the entirety of the main header. Default::

        {% block nav_header %}
            {% include 'adminlte/lib/_main_header.html' %}
        {% endblock %}

    If you wish to customise the entirety of the main header you may override this block, otherwise
    you can redefine ``adminlte/lib/_main_header.html`` to get finer control over your changes.

``nav_sidebar``
'''''''''''''''

    Wrapper around the entirety of the sidebar. Default::

        {% block nav_header %}
            {% include 'adminlte/lib/_main_sidebar.html' %}
        {% endblock %}

    If you wish to customise the entirety of the sidebar you may override this block, otherwise
    you can redefine ``adminlte/lib/_main_header.html`` to get finer control over your changes.

``content_wrapper``
'''''''''''''''''''

    Wrapper around all of the content area (including the content header, messages, and actual page content).

    **You probably want to override the ``content`` block instead.** Default::

``content_header``
''''''''''''''''''

    The header that appears over the page content, but within the content area of the design.

    Default::

        {% block content_header %}
            <section class="content-header">
                <h1>
                    {% block page_name %}{% endblock %}
                    {% block no_description %}
                    <small>{% block page_description %}{% endblock %}</small>
                    {% endblock %}
                </h1>
                {% block breadcrumbs %}
                    {# Breadcrumb implementation left to developers #}
                {% endblock %}
            </section>
        {% endblock %}

``page_name``
'''''''''''''

    The name of the page as will be displayed in the content header.

``page_description``
''''''''''''''''''''

    The description of the page tht will appear alongside the page name in the header.

``no_description``
''''''''''''''''''

    If no description is to be displayed, you can implement this as an empty block to remove
    the wrapper HTML. For example::

        {% block no_description %}{% endblock %}

``breadcrumbs``
'''''''''''''''

    Use the block the implement your breadcrumbs if desired.

    .. todo::

        Provide tools to make the generation of breadcrumbs easier

``content_outer``
'''''''''''''''''

    Wraps the outside of the content area and any messages.

    **You probably want to override the ``content`` block instead.**

``messages``
''''''''''''

    Wrapper around the entirety of the message area. Default::

        {% block messages %}
            {% include 'adminlte/lib/_messages.html' %}
        {% endblock %}

    See the `Django messages framework`_.

``content_block_wrap``
''''''''''''''''''''''

    Wraps the ``content`` block. May be useful in some cases.

``content``
'''''''''''

    Block for the main content which will be displayed in the page. Empty by default.

``nav_footer``
''''''''''''''

    Wrapper around the entirety of the main footer. Default::

        {% block nav_footer %}
            {% include 'adminlte/lib/_main_footer.html' %}
        {% endblock %}

    If you wish to customise the entirety of the main footer you may override this block, otherwise
    you can redefine ``adminlte/lib/_main_footer.html`` to get finer control over your changes.

``javascript``
''''''''''''''

    All ``<script>`` tags which appear before the ``</body>`` tag. By default this includes all content
    from ``adminlte/lib/_scripts.html``.

    Consider making use of ``{{ block.super }}`` when overriding this block.

``extra_foot``
''''''''''''''

    Additional HTML to be placed before the ``</body>`` tag. Empty by default.






.. _sites framework: https://docs.djangoproject.com/en/1.10/ref/contrib/sites/
.. _inheritance docs: https://docs.djangoproject.com/en/1.10/ref/templates/language/#template-inheritance
.. _Django messages framework: https://docs.djangoproject.com/en/1.10/ref/contrib/messages/
