from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField


# class NameForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=255)
#     message =forms.CharField(widget=forms.Textarea) 

class CommentForm(forms.ModelForm):
    # captcha = CaptchaField()

    class Meta:
        model = Comment
        # fields =['name','subject', 'email', 'message']
        fields = ['post','name', 'email', 'subject', 'message']  


