from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Pregunta')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='Opción')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text