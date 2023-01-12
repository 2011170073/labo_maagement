from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from . import models


def periodic_execution():
    print("20時定期実行")
    teacher_list = models.room.objects.all()#room_status_id＝研究室のみのroomsテーブルを持ってくる
    room_status_0 = models.room.objects.get(pk=0)
    room_status_pk = models.room_status.objects.get(pk=1000)#id=研究室を持つroom_statusテーブルを取得
    room_pk = room_status_pk.room_set.all()#研究室idを持つroomの情報のみを全て取得
    status_pk = models.status.objects.get(pk=0)
    for i in room_pk:
        teacher_pk = models.teacher.objects.get(pk=i.owner_id.id)
        models.status_list.objects.create(status_id=status_pk,room_id=room_status_0,teacher_id=teacher_pk)#room_idにroomモデル

def start():
  scheduler = BackgroundScheduler()
  scheduler.add_job(periodic_execution, 'cron', hour=20, minute=43)# 毎日20時に実行
  scheduler.start()