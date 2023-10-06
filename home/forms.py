from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
          'text': forms.Textarea(attrs={'rows':45, 'cols':85}),
        }
        fields = ('title', 'text', 'document', 'image')
