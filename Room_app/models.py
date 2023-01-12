from django.db import models

class Siratuti(models.Model):
    room_id = models.IntegerField(primary_key=True)
    datatime = models.DateTimeField(auto_now_add=True,null=True)
    zyoukyou1 = models.CharField(max_length=100)

    def __str__(self):
        return self.zyoukyou1

class Roomlist(models.Model):
    teacher_name = models.CharField(max_length=100)
    #pk=primarykeyは自動割り当てのはず
    def __str__(self):
        return self.teacher_name
    
