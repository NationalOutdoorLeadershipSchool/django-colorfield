Django Colorfield
---------------------

This module fills the need of having a 'colorfield' that's usable in both
django models and forms.

Makes use of http://www.dematte.at/tinyColorPicker/

Requirements
============
* `Django  <https://www.djangoproject.com/>`_ 1.7.0+
* `jQuery <http://jquery.com/>`_ 1.11.0+

Installation
============

#. Install django-colorfield using pip. For example::

    pip install django-colorfield

#. Add  ``datetimewidget`` to your INSTALLED_APPS.

Collect static files with ``./manage.py collectstatic``.

Basic Configuration
===================
#. Create your model and add a ColorField  ::

    from django.db import models
    from colorfield.fields import ColorField

    class Show(models.Model):
        title = models.CharField(u'Title', max_length=250)
        color = ColorField()
