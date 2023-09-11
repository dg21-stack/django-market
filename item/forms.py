from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            }),
            'image': forms.FileInput(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            })

        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            }),
            'image': forms.FileInput(attrs={
                'class': 'mt-6 w-full px-6 rounded-xl border'
            })

        }
