from django.forms import ModelForm
from .models import Contact, Apply


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'msg']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'field__input'
            field.widget.attrs['placeholder'] = field_name.capitalize()
