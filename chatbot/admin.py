from django.contrib import admin
from .models import User_Answers
from .models import ABC_Modules

class ABC_Modules_Admin(admin.ModelAdmin):
    list_display = ('code_abc_modules','created_date', 'module_type', 'module_level', 'module_used', 'vanessa_question','url_address')
    search_fields = ('vanessa_question',)
    list_display_links = ('module_type', 'module_level', 'vanessa_question','url_address')


class User_Answers_Admin(admin.ModelAdmin):
    list_display = ('module_guestion_field', 'created_date', 'keyword','keyword_weight')
    search_fields = ('keyword','keyword_weight')
    # list_display_links = ('created_date', 'keyword','keyword_weight')


admin.site.register(User_Answers, User_Answers_Admin)
admin.site.register(ABC_Modules, ABC_Modules_Admin)