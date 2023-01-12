from django.core.management.base import BaseCommand
from ... import models

class Command(BaseCommand):
    def handle(self,*args,**options):
        teacher_list = models.room.objects.all()#room_status_id＝研究室のみのroomsテーブルを持ってくる
        room_status_pk = models.room_status.objects.get(pk=1000)#id=研究室を持つroom_statusテーブルを取得
        room_pk = room_status_pk.room_set.all()#研究室idを持つroomの情報のみを全て取得
        status_pk = models.status.objects.get(pk=0)
        for i in room_pk:
            teacher_pk = models.teacher.objects.get(pk=i.owner_id.id)
            models.status_list.objects.create(status_id=status_pk,room_id=i,teacher_id=teacher_pk)#room_idにroomモデル

        