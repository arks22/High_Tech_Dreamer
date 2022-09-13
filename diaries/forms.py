from django import forms
from diaries.models import Diary
from datetime import date, datetime

# --------------------------------------------------
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        
        # 送信フィールド
        fields = ('teacher',
                  'date',
                  'student',
                  'subject',
                  'content',
                  'range',
                  'homework',
                  'remark')
        
        # ラベル表示の編集
        labels = {'subject': '科目コース',
                  'student': '生徒',}
        
        # タグの属性

        widgets = {'range': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                   'subject': forms.Select(attrs={'class': 'form-control'}),
                   'homework': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                   'date': forms.NumberInput(attrs={'type': 'date', 'class': 'form-control','max':date.today()}),
                   'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                   'teacher': forms.Select(attrs={'class': 'form-control'}),
                   'student': forms.Select(attrs={'class': 'form-control'}),
                   'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),}

