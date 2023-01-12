from . import models



class request_to_update:
    def __init__(self):
        self.status_ins = {0:"帰宅",1:"在室",2:"不在",3:"講義中"}
    
    def against_req(self,req):
        touch_area = str(req.GET["area"])
        categoty_pk = models.category.objects.get(pk=int(req.GET["status"]))
        last_status = categoty_pk.status_list_set.last()
        last_status = last_status.status
        print(last_status)
        if last_status != 1 and touch_area == "labo":
            #最新ステータスが在室ではないandタッチされた場所がlaboの時
            print("ステータスを在室以外から在室(1)に変更")
            models.status_list.objects.create(status_name=self.status_ins[1],status=1,category_id=categoty_pk,area=touch_area)
        elif last_status == 1 and touch_area == "labo":
            print("ステータス在室から不在に変更")
            models.status_list.objects.create(status_name=self.status_ins[2],status=2,category_id=categoty_pk,area=touch_area)
        elif touch_area != "labo":
            print("タッチされた場所が研究室以外ならstatus講義中(3)に変更")
            models.status_list.objects.create(status_name=self.status_ins[3],status=3,category_id=categoty_pk,area=touch_area)

