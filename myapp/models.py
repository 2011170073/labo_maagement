from django.db import models

"""
class category(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher_name
"""

class teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name

class room(models.Model):
    id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.room_name

#スネークケース記法で変数を宣言(小文字と単語ごとに_を挟む)


class status_list(models.Model):
    status_name = models.CharField(max_length=100)
    status = models.IntegerField()
    room_id = models.ForeignKey(room,on_delete=models.PROTECT)
    teacher_id = models.ForeignKey(teacher,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    #foreignkeyクラスで、引数１に指定したモデルのテーブルcategoriesと紐づけする
    def __str__(self):
        return str(self.status)


