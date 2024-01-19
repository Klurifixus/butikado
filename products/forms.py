from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Size
from django.forms import ModelForm, inlineformset_factory

class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = ['size', 'quantity']

# Define the SizeFormSet at the module level
SizeFormSet = inlineformset_factory(
    Product, Size, form=SizeForm, extra=1, can_delete=True
)       

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        if self.instance and self.instance.pk:
            self.size_formset = SizeFormSet(instance=self.instance)

            for size_form in self.size_formset:
                for field_name, field in size_form.fields.items():
                    if field_name in ["id", "DELETE", "product"]:
                        field.widget.attrs['class'] = 'd-none'
        else:
            self.size_formset = SizeFormSet()
            