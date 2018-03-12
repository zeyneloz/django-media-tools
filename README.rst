==================
django-media-tools
==================

django-media-tools is an app that provides useful widgets for managing media files in django admin. It doesn't use any javascript library.

Works with Django 1.10 and newer versions.

Screenshot of preview widget:

.. image:: https://screenshotscdn.firefoxusercontent.com/images/c7cce7f5-cfe6-4de0-9d1b-1dc9529c87f4.png


Installation
============

#. Install using pip::

    pip install django-media-tools

#. Add ``media_tools`` to the ``INSTALLED_APPS``::

    INSTALLED_APPS = [
       ...
       'media_tools',
    ]

#. Run ``collectstatic`` command. It will copy the static files used by media_tools to your static root.::

     python manage.py collectstatic

