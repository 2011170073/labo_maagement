from django.shortcuts import render
from django.views.generic import View
from . import models
from . import update
from django.http import HttpResponse
from django.shortcuts import redirect

class teacher_list_view(View):
    def get(self,req):
        data = {"teacher_list":models.teacher.objects.exclude(id=0)}
        return render(req,"teacher_list.html",data)

class status_list_view(View):
    def get(self,req,pk):
        teacher_pk = models.teacher.objects.get(pk=pk)
        #pk=「getリクエストで送られてきたid」のcategoryモデルインスタンスを取得
        data = {"status_list_pk":teacher_pk.status_list_set.all()}#1から多を参照
        #①(特定のpkを持った従テーブルのモデルインスタンス).②(主テーブルのモデル名)_set.all()で、
        #②の従モデル名_id属性に①のpkと同じ値を持つ主テーブルのモデルインスタンスが呼びだされる
        return render(req,"status_list_pk.html",data)

class status_last_view(View):
    def get(self,req,pk):
        teacher_pk = models.teacher.objects.get(pk=pk)
        data = {"status_last_pk":teacher_pk.status_list_set.last()}
        return render(req,"status_last_pk.html",data)

class status_update(View):
    def get(self,req):
        print(req)
        req1 = update.request_to_update()
        req1.against_req(req)
        teacher_pk = int(req.GET["status"])
        print(teacher_pk)
        #redirect("")#現在のページをリロード
        return HttpResponse()
        #最後にrenderをしないとページが描画されない？
        #status_list_pkにjavascriptでページリロード用メソッドを記述
        