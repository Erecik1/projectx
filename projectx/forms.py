from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from post.models import Post

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=64, required=True)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author',
                  'title',
                  'text',
                  'document',
                  'published_date')


class PostSearchForm(forms.Form):
    title = forms.CharField(required=False,
                            label="Title",
                            max_length=30)

    author = forms.CharField(required=False,
                            label="Author",
                            max_length=30)

    text = forms.CharField(required=False,
                            label="Text",
                            max_length=30)

