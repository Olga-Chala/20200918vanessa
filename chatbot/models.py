from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

class User_Answers(models.Model):    
    code_keys = models.UUIDField(primary_key=True, unique=True, editable=False, null=False, default=uuid.uuid4)
    title_block = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    module_code = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    
    def publish_keys(self):
        self.save()

    def __str__(self):
        return self.title_block

class ABC_Modules(models.Model):
    code_abc_modules = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # code_keys = models.ForeignKey(User_Answers, on_delete=models.CASCADE,default=0)
    module_type = models.CharField(max_length=2)
    web_interface = models.TextField(default='google.com')
    vanessa_answ = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    next_module_code = models.CharField(max_length=200, default='')

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.vanessa_answ
