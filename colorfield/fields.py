import re

from colorfield.widgets import ColorWidget

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

color_re = re.compile('^rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)'
                      '|rgba\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3}),\s*(\d*(?:\.\d+)?)\)'
                      '|#([A-Fa-f0-9]{6}'
                      '|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')


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
