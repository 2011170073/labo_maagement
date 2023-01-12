from django.shortcuts import render,redirect
from . import models
from django.views.generic import View
from django.http import HttpResponse


class roomlist_view(View):
    def get(self,req):
        #各先生のpk(id)カラムを取得してaタグのurl属性に付与。
        data = {"roomlist_list":models.Roomlist.objects.all()}
        return render(req,"roomlist.html",data)


class RoomupdateView(View):
    def get(self,req):#getリクエストに対する処理、引数reqはリクエストの中身が入る
        try:
            req1 = int(req.GET["key1"])
            if req1 == 12345:
                data = {"sira_list":models.Siratuti.objects.all()}
                for item in data["sira_list"]:
                    i1 = item.room_id
                    i2 =  0           
                    if i1 > i2:
                        i2 = i1
                print(i2)
                #models.Siratuti.objects.create(room_id=i2+1,zyoukyou1="在室")
                print(data["sira_list"][i2-1])#一番idが大きいモデルのテーブルのzyoukyou1カラム
                if data["sira_list"][i2-1] == "在籍":
                    response = HttpResponse(status=201)#201は在籍
                elif data["sira_list"][i2-1] == "不在":
                    response = HttpResponse(status=202)#202は不在という意味にする
                else:
                    print("在籍・不在以外の文字列")
                #statusの400はBadrequest、401はunauthorizedという意味
            else:
                print("登録されてない")
        except:
            print("エラーが出るが値は取得できる！")
        
        return response

#class RoompollingView(View):


class RoomSiratutiView(View):
    def post(self,req):
        data = {"sira_list":models.Siratuti.objects.all()}
        


    def get(self,req):#getリクエストに対する処理、引数reqはリクエストの中身が入る
        data = {"sira_list":models.Siratuti.objects.all()}
        """
        for item in data["sira_list"]:
            i1 = item.room_id
            i2 =  0           
            if i1 > i2:
                i2 = i1#i2には一番大きいid値が入る
        #ラズパイから来たgetリクエストはxsgiという種類の為、.GETでキー指定
        
        try:
            req1 = int(req.GET["key1"])
            if req1 == 12345:#取得した教員証のidが白土先生の場合、新規siratutiモデルをインサート
                models.Siratuti.objects.create(room_id=i2+1,zyoukyou1="在室")
            else req1 == 2:#取得した教員証のidが〇〇先生の場合、新規〇〇モデルをインサート
        except:
            print("エラーが出るが値は取得できる！")
        """
        
        return render(req,"room.html",data)






