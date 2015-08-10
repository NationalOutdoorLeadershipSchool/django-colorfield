from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.six import string_types

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
        js_options = ''
        if self.options:
            options_list = []
            for k, v in iter(self.options.items()):
                options_list.append("%s: %s" % (k, quote(k, v)))

            js_options = ",\n".join(options_list)
            js_options = mark_safe('{%s}' % js_options)
        return render_to_string('colorfield/color.html', locals())
