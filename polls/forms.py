from django import forms
#モデルクラスを呼出
from .models import People
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.admin import widgets
import os


widget_textinput = forms.TextInput(
    attrs={
        "class":"form-control",
    }
)

#フォームクラス作成
class Contact_Form(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = People

        #②表示するモデルクラスのフィールドを定義
        fields = ('Name','Furigana','Tell','Mail','Birthday','Adress')


        #③表示ラベルを定義
        labels = {
            'Name':"名前  ",
            'Furigana':"フリガナ",
            'Tell':"電話番号",
            'Mail':"メール ",
            'Birthday':"生年月日",
            'Adress':"住所  ",
        }
        
        widgets = {
            'Name': forms.TextInput(attrs={'size':50}),
            'Furigana': forms.TextInput(attrs={'size':50}),
            'Tell': forms.TextInput(attrs={'size':50}),
            'Mail': forms.TextInput(attrs={'size':50}),
            'Birthday': forms.TextInput(attrs={'size':50}),
            'Adress': forms.TextInput(attrs={'size':50}),
        }

    label_suffix = ''

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)



class CheckeForm(forms.Form):
    selected_time = forms.fields.ChoiceField(
        choices = (
            ('','同意します'),
        ),
        label = '上記の内容に同意できる場合下記ボックスにチェックを入れてください',
        required = True,
        widget = forms.widgets.RadioSelect
    )
