from django.shortcuts import render
from django.views.generic import View
from . import models
from . import update
from django.http import HttpResponse

class teacher_list_view(View):
    def get(self,req):
        data = {"categories_list":models.category.objects.all()}
        return render(req,"teacher_list.html",data)

class status_list_view(View):
    def get(self,req,pk):
        categoty_pk = models.category.objects.get(pk=pk)
        #pk=「getリクエストで送られてきたid」のcategoryモデルインスタンスを取得
        data = {"status_list_pk":categoty_pk.status_list_set.all()}
        #①(特定のpkを持った従テーブルのモデルインスタンス).②(主テーブルのモデル名)_set.all()で、
        #②の従モデル名_id属性に①のpkと同じ値を持つ主テーブルのモデルインスタンスが呼びだされる
        return render(req,"status_list_pk.html",data)

class status_update(View):
    def get(self,req):
        req1 = update.request_to_update()
        req1.against_req(req)
        return HttpResponse()
        