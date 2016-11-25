Notes on Static Files
=====================

This static files are provided primerily as a fallback for your convienience.
Feel free to rely on them.

However, the folder structure is designed in such a way that you can
override these assets through the use of ``django-npm``.

A rough guide is:

1. Install ``django-npm``

2. Set ``STATICFILES_FINDERS`` and ensure the npm finder appears above the app finder

3. Create a ``package.json`` file specifying the required versions of the packages

4. Run ``npm install``

Django should now load the static files from your newly installed ``npm`` packages.


