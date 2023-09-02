from django import forms
from .models import post

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        # 어떤 필드를 입력 받을지 써주기
        fields = ['name', 'phoneNumber', 'inviterName', 'complete']