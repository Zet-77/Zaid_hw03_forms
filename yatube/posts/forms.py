from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image',)
        help_texts = {
                'text': 'Новый текст поста',
                'group': 'Выберите группу, к которой будет относится пост'
            }
        labels = {
            'text': 'Текст поста',
            'group': 'Группа'
        }

