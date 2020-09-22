from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

class ABC_Modules(models.Model):
    verbose_name = "Модуль вопросов и ответов Ванессы"
    verbose_name_plural = "Модули вопросов и ответов Ванессы"  
    code_abc_modules = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField('Дата создания модуля', default=timezone.now)
    module_type = models.CharField('Тип модуля', max_length=1)
    module_level = models.IntegerField('Уровень модуля', default=0)
    module_used = models.BooleanField('Модуль используется Ванессой', default=True)
    previous_module = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    # ,  related_name='Предшествующий модуль'
    # previous_module = models.IntegerField('Предшествующий модуль', null=True)
    vanessa_question = models.CharField('Вопрос Ванессы', max_length=200, default='')
    Vanessa_answer_word = models.BooleanField('Использовать слова пользователя в ответе', default=False)
    vanessa_answer = models.CharField('Ответ Ванессы', max_length=200, blank=True)
    web_interface = models.CharField('Интерфейс', max_length=200, default='Интерфейс', blank=True)
    url_address = models.URLField('url', max_length=200, blank=True, null=True)

    def ABC_Modules_save(self):
        self.created_date = timezone.now()
        self.save()
        

class User_Answers(models.Model):  
    verbose_name = "Ключевое слово в ответе пользователя"
    verbose_name_plural = "Ключевые слова в ответе пользователя"
    code_keys = models.UUIDField(primary_key=True, unique=True, editable=False, default=0)
    created_date = models.DateTimeField('Дата', default=timezone.now)
    module_code = models.ForeignKey('ABC_Modules', on_delete=models.PROTECT, default=1)
    keyword = models.CharField(' Ключевое слово', max_length=30)
    keyword_weight = models.FloatField('Вес(важность) слова', blank=True, null=True)

    def User_Answers_save(self):
        self.created_date = timezone.now()
        self.save()

    def module_guestion_field(self):
        verbose_name = "Модуль вопросов и ответов Ванессы"
        return ABC_Modules.vanessa_question
        
    def module_type_field(self):
        return ABC_Modules.module_type

    def module_level_field(self):
        return ABC_Modules.module_level

