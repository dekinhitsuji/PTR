from django.shortcuts import render, redirect
from . import forms
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from . forms import Contact_Form, CheckeForm
from django.urls import reverse_lazy
from django.views import View



class FormView(TemplateView):

    #初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                       "form":forms.Contact_Form(),
                       }

    #GET時の処理を記載
    def get(self,request):
        return render(request, "polls/formpage.html",context=self.params)

    #POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Contact_Form(request.POST)

            #フォーム入力が有効な場合
            if self.params["form"].is_valid():
                #入力項目をデータベースに保存
                self.params["form"].save(commit=True)
                self.params["Message"] = "入力情報が送信されました。"
                return redirect(reverse_lazy('polls:doui'))

        return render(request, "polls/formpage.html",context=self.params)


class ChoiceView(View):
    def get(self, request):
        form = forms.CheckeForm()
        context = {
            'form': form
        }

        return render(request, 'polls/doui.html', context)

def PrivacyView(request):
    return render(request, 'polls/welcome.html')
