
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

from app_plugins.models import PluginPoint, Plugin, LABEL_RE

def validate_label(value):
    if not LABEL_RE.search(value):
        raise forms.ValidationError(gettext(
            u"This value must contain only letters, "
            u"numbers, underscores, and '.' dots."
        ))
    else:
        return value

class AdminPluginPointForm(forms.ModelForm):
    class Meta:
        model = PluginPoint
        exclude = ()
    
    def clean_label(self):
        value = self.cleaned_data["label"]
        return validate_label(value)

class AdminPluginForm(forms.ModelForm):
    class Meta:
        model = Plugin
        exclude = ()
    
    def clean_label(self):
        value = self.cleaned_data["label"]
        return validate_label(value)