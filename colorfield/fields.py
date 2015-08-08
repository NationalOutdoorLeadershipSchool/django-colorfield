#!/usr/bin/env python

import re

from django import forms
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

color_re = re.compile('^rgba?\((?:\d{1,3}[,\)]){3}(?:\d+\.\d+\))$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')


class ColorWidget(forms.Widget):
    class Media:
        js = [settings.STATIC_URL + 'colorfield/colorpicker/jqColorPicker.min.js']
        
    def render(self, name, value, attrs=None):
        return render_to_string('colorfield/color.html', locals())


class ColorField(models.CharField):
    default_validators = [validate_color]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^colorfield\.fields\.ColorField"])
except ImportError:
    pass

# vim: et sw=4 sts=4
