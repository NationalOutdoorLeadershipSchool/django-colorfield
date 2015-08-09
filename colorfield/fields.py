import re

from django import forms
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.six import string_types

color_re = re.compile('^rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)'
                      '|rgba\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*(\d*(?:\.\d+)?)\)'
                      '|#([A-Fa-f0-9]{6}'
                      '|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')

quoted_options = set([
    'customBG',
    ])

quoted_bool_options = set([
    'opacity',
    'preventFocus',
    ])


def quote(key, value):
    """
    If option value is a string we need to wrap in quotes and
    if value is a python boolean convert to javascript boolean.
    Int values can be left as is.
    """

    if key in quoted_options and isinstance(value, string_types):
        return "'%s'" % value

    if key in quoted_bool_options and isinstance(value, bool):
        return {True: 'true', False: 'false'}[value]

    return value


class ColorWidget(forms.Widget):
    def __init__(self, options=None, attrs=None):
        super(ColorWidget, self).__init__(attrs)
        self.options = options

    class Media:
        js = [settings.STATIC_URL + 'colorfield/colorpicker/jqColorPicker.min.js']
        
    def render(self, name, value, attrs=None):
        options_list = []
        for k, v in iter(self.options.items()):
            options_list.append("%s: %s" % (k, quote(k, v)))

        js_options = ",\n".join(options_list)
        js_options = mark_safe('{%s}' % js_options)
        return render_to_string('colorfield/color.html', locals())


class ColorField(models.CharField):
    default_validators = [validate_color]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        if not kwargs.get('default'):
            kwargs['default'] = 'rgb(0, 0, 0)'
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^colorfield\.fields\.ColorField"])
except ImportError:
    pass
