from . import models



class request_to_update:
    def __init__(self):
        pass
        
    def against_req(self,req):
        touch_room = models.room.objects.get(pk = int(req.GET["area"]))#5210の場合は、id=5210の白土研究室を持ってくる
        next_room = touch_room.room_status_id#id=5210の場合は、研究室を持ってくる
        owrner = touch_room.owner_id.id
        teacher_pk = models.teacher.objects.get(pk=int(req.GET["status"]))#タッチしたカードの情報
        last_status = teacher_pk.status_list_set.last()
        now_room = last_status.room_id.room_status_id#現状態のroom_statusから、紐づけられたroomのroom_statusを取得
        print("現状態の場所,タッチした人間："+str(now_room)+","+str(teacher_pk.id))
        print("次状態のタッチ場所,所有者："+str(next_room)+","+str(owrner))
        print("現状態のステータス："+str(last_status.status_id))
        

        status_ins = models.status.objects
        if now_room.id == next_room.id:#同じ場所タッチ
            if now_room.id == 1000 and next_room.id == 1000:#研究室➔研究室
                if teacher_pk.id == owrner:#タッチしたカード情報とタッチした場所の部屋のオーナーが同じ時,
                    if last_status.status_id.id == 5:#現状態が他教授の研究室の時➔在室に変化(テストで発覚した抜け穴を補助する形で記述したプログラム)
                        models.status_list.objects.create(status_id=status_ins.get(id=last_status.status_id.id-4),room_id=touch_room,teacher_id=teacher_pk)
                    else:#現状態が5でない場合は、在室↔不在
                        models.status_list.objects.create(status_id=status_ins.get(id=-last_status.status_id.id),room_id=touch_room,teacher_id=teacher_pk)
                elif teacher_pk.id != owrner:#つまり、先生が別の先生の研究室でタッチした時,の研究室(誰かの研究室という意味)=5をidを変更
                    models.status_list.objects.create(status_id=status_ins.get(id=5),room_id=touch_room,teacher_id=teacher_pk)
            elif next_room.id == 2000:
                    models.status_list.objects.create(status_id=status_ins.get(id=2),room_id=touch_room,teacher_id=teacher_pk)
                #講義中からは反転させない。➔別の号館へタップした際に上手く動作しない
            elif next_room.id == 3000:
                    models.status_list.objects.create(status_id=status_ins.get(id=3),room_id=touch_room,teacher_id=teacher_pk)
        elif now_room.id != next_room.id:#別の場所をタッチ
            print("1")
            if next_room.id == 1000:#別の場所➔研究室
                if teacher_pk.id == owrner:#タッチしたカード情報とタッチした場所の部屋のオーナーが同じ時
                    models.status_list.objects.create(status_id=status_ins.get(id=1),room_id=touch_room,teacher_id=teacher_pk)
                elif teacher_pk.id != owrner:#つまり、先生が別の先生の研究室でタッチした時,の研究室(誰かの研究室という意味)=5をidを変更
                    models.status_list.objects.create(status_id=status_ins.get(id=5),room_id=touch_room,teacher_id=teacher_pk)
            elif next_room.id == 2000:#別の場所➔講義棟
                    models.status_list.objects.create(status_id=status_ins.get(id=2),room_id=touch_room,teacher_id=teacher_pk)
            elif next_room.id == 3000:#別の場所➔会議室
                    models.status_list.objects.create(status_id=status_ins.get(id=3),room_id=touch_room,teacher_id=teacher_pk)
                



"""
        if now_room == next_room:
             #研究室➔研究室(owrner_idがtouch_idと一致したとき)
            if now_room.id == 1000 and next_room.id == 1000:
                #不在↔在室(statusのidの反転(1➔-1、これならマイナスをつければできる))
                models.status_list.objects.create(status_id=status_ins(id=0).id,room_id=touch_room,teacher_id=teacher_pk) ok
                #研究室➔研究室(owrner_idとtouch_idが不一致)
                #次のstatusを「owrner_idの研究室内」にする
            else:
                #next_roomが講義棟、会議室、ゼミ室の場合は、ステータスをそれに対応したstatus_idにする。
                #↑は分岐を３つにする、もしくは１つにまとめられる？
        elif now_room != next_room:
            #タッチした場所と現状態の場所が違う場合は、そのタッチした場所をroom_idにして、status_id=status_insのid(statussの講義中のid=room_statusの講義棟のidである2000にしてみると分岐がなくても済むかも)ごとに分岐を分ける
"""
            
                
