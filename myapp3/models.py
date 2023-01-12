from django.db import models

class teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.teacher_name)

class status(models.Model):
    id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.status_name)

class room_status(models.Model):
    id = models.IntegerField(primary_key=True)
    room_status_name=models.CharField(max_length=100)

    def __str__(self):
        return str(self.room_status_name)

class room(models.Model):
    id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=100)
    room_status_id = models.ForeignKey(room_status,on_delete=models.PROTECT)
    owner_id = models.ForeignKey(teacher,on_delete=models.PROTECT,blank=True)

    
    def __str__(self):
        return str(self.room_name)

#スネークケース記法で変数を宣言(小文字と単語ごとに_を挟む)


class status_list(models.Model):
    status_id = models.ForeignKey(status,on_delete=models.PROTECT)
    room_id = models.ForeignKey(room,on_delete=models.PROTECT)
    teacher_id = models.ForeignKey(teacher,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.status_id)
    #foreignkeyクラスで、引数１に指定したモデルのテーブルcategoriesと紐づけする
    
