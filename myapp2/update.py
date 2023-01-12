from . import models



class request_to_update:
    def __init__(self):
        self.status_ins = {0:"帰宅",1:"在室",2:"不在",3:"講義中",4:"会議中"}
    
    def against_req(self,req):
        touch_room = models.room.objects.get(pk = int(req.GET["area"]))
        next_room = touch_room.room_status
        print(touch_room)
        teacher_pk = models.teacher.objects.get(pk=int(req.GET["status"]))
        last_status = teacher_pk.status_list_set.last()
        now_room = last_status.room_id.room_status#現状態のroom_statusから、紐づけられたroomのroom_statusを取得
        print("現状態のタッチ場所："+now_room)
        print("次状態のタッチ場所："+next_room)
        print("現状態のステータス："+str(last_status.status))


        """
        if now_room == next_room :
            #前の部屋情報がタッチした部屋情報と同じとき、在室→不在、不在→在室。交互
            #教室、会議室ならば、～中→学内。交互
        if now_room != next_room :
            #前の部屋情報がタッチした部屋情報と違うとき、その部屋情報を出力
            #教室ならば、講義中、会議室の時、会議中、研究室ならば、在室
        
        """

        
        if now_room == "研究室" and next_room == "講義室":
            models.status_list.objects.create(status_name=self.status_ins[3],status=3,room_id=touch_room,teacher_id=teacher_pk)
        elif now_room == "研究室" and next_room == "会議室":
            models.status_list.objects.create(status_name=self.status_ins[4],status=4,room_id=touch_room,teacher_id=teacher_pk)
        elif now_room == "研究室" and next_room == "研究室":
            if last_status.status == 1:#現状態が在室
                models.status_list.objects.create(status_name=self.status_ins[2],status=2,room_id=touch_room,teacher_id=teacher_pk)
            elif last_status.status == 2:#現状態が不在
                models.status_list.objects.create(status_name=self.status_ins[1],status=1,room_id=touch_room,teacher_id=teacher_pk)
        elif now_room == "なし" and next_room == "研究室":
            models.status_list.objects.create(status_name=self.status_ins[1],status=1,room_id=touch_room,teacher_id=teacher_pk)
            #先生が出勤していきなり会議室や講義棟に行く場合はif文で処理追加(なし➔研究室でcreate)
        elif now_room == "講義室" and next_room == "研究室":
            models.status_list.objects.create(status_name=self.status_ins[1],status=1,room_id=touch_room,teacher_id=teacher_pk)
        elif now_room == "講義室" and next_room == "会議室":
            models.status_list.objects.create(status_name=self.status_ins[4],status=4,room_id=touch_room,teacher_id=teacher_pk)
        elif now_room == "会議室" and next_room == "研究室":
            models.status_list.objects.create(status_name=self.status_ins[1],status=1,room_id=touch_room,teacher_id=teacher_pk)
        elif now_room == "会議室" and next_room == "講義室":
            models.status_list.objects.create(status_name=self.status_ins[3],status=3,room_id=touch_room,teacher_id=teacher_pk)


        #if last_status.status == 1 and last_status. #status1➔3に移動


        """
        if last_status != 1 and touch_room == 5206:
            #最新ステータスが在室ではないandタッチされた場所がlaboの時
            print("ステータスを在室以外から在室(1)に変更")
            models.status_list.objects.create(status_name=self.status_ins[1],status=1,room_id=touch_room,teacher_id=teacher_pk)
        elif last_status == 1 and touch_room == 5206:
            print("ステータス在室から不在に変更")
            models.status_list.objects.create(status_name=self.status_ins[2],status=2,room_id=touch_room,teacher_id=teacher_pk)
        elif touch_room != 5206:
            print("タッチされた場所が研究室以外ならstatus講義中(3)に変更")
            models.status_list.objects.create(status_name=self.status_ins[3],status=3,teacher_id=teacher_pk)
        """