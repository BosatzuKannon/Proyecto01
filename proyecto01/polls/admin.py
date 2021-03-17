from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionConfig(admin.ModelAdmin):
    
    fieldsets = (
        ('Datos Básicos', {
            "fields": (
                'question_text',
            ),
        }),
        
    )
    inlines = (ChoiceInLine,)
    list_display = ('id', 'question_text', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    
    

# Register your models here.
admin.site.register(Question, QuestionConfig)
#admin.site.register(Choice)