from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta():
        model = Comment
        # fields = '__all__'

        # 필요한 일정 부분만 출력되도록 변경 (선택옵션)
        # fields -> 추가할 필드 목록
        # fields = ('content', )
        

        # 필요한 일정 부분만 출력되도록 변경 (제외옵션)
        # exclude -> 제외할 필드 목록
        exclude = ('article', )

        