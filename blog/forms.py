from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = False 
        self.fields['comment'].label = False 
    # username = forms.CharField()
    class Meta:
        model = Comment
        fields = ('username', 'comment')
        widgets = {
          'username': forms.TextInput(),
      
        }

