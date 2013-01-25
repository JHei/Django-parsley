from django import forms


def parsleyfy(klass):
    class ParsleyClass(klass):
        def __init__(self, *args, **kwargs):
            super(ParsleyClass, self).__init__(*args, **kwargs)
            for key, val in self.fields.items():
                if val.required:
                    val.widget.attrs.update({"data-required": "true"})
                if isinstance(val, forms.URLField):
                    val.widget.attrs.update({"data-type": "url"})
                if isinstance(val, forms.EmailField):
                    val.widget.attrs.update({"data-type": "email"})
                if isinstance(val, forms.IntegerField):
                    val.widget.attrs.update({"data-type": "digits"})
                if isinstance(val, forms.DecimalField):
                    val.widget.attrs.update({"data-type": "number"})
                if isinstance(val, forms.RegexField):
                    val.widget.attrs.update({"data-regexp": val.regex.pattern})
                if hasattr(val, "max_length") and val.max_length:
                    val.widget.attrs.update({"data-maxlength": val.max_length})
                if hasattr(val, "min_length") and val.min_length:
                    val.widget.attrs.update({"data-minlength": val.min_length})

    return ParsleyClass
