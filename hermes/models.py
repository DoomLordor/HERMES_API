from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WorkersPosition(models.Model):
    """Список должностей"""
    name_position = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'workers_position_manual'
        unique_together = (('id',), ('name_position',))
        verbose_name = 'Должность сотрудника'


class Workers(models.Model):
    """Рабникы компании, их должность и их наставники"""
    position = models.ForeignKey(WorkersPosition, on_delete=models.PROTECT)
    mentor = models.IntegerField('id наставника')
    hr = models.IntegerField('id HR менеджера')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'workers'
        unique_together = (('id',), ('user',))
        verbose_name = 'Сотрудник'


class Questions(models.Model):
    """Список анкет"""
    type_questions = models.TextField('Тип анкеты')
    questions = models.TextField('Вопросы анкеты')

    class Meta:
        managed = True
        db_table = 'questions'
        unique_together = ('id',)
        verbose_name = 'Анкета'


class ResultsQuestions(models.Model):
    """Результаты анкетирования"""
    type_questions = models.ForeignKey(Questions, on_delete=models.PROTECT)
    data = models.TextField('Данные анкеты')
    date = models.DateField('Дата заполнения анкеты')
    worker = models.ForeignKey(Workers, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'results_questions'
        unique_together = ('id',)
        verbose_name = 'Результат анкеты'


class Messages(models.Model):
    """Таблица дял пересылки сообщений"""
    message = models.TextField('Сообщение для отправки')
    sender = models.ForeignKey(Workers, on_delete=models.PROTECT, related_name='senderWorkers')
    recipient = models.ForeignKey(Workers, on_delete=models.PROTECT, related_name='recipientWorkers')
    kod_chat = models.CharField(max_length=100)
    time_message = models.DateTimeField('Время отправки сообщение')

    class Meta:
        managed = True
        db_table = 'messages'
        unique_together = ('id',)
        verbose_name = 'Сообщение'


class Notifications(models.Model):
    """Таблица для уведомления пользователей"""
    message = models.TextField('Сообщение для уведомления')
    recipient = models.ForeignKey(Workers, on_delete=models.PROTECT)
    time_notification = models.DateTimeField('Время уведомления')

    class Meta:
        managed = True
        db_table = 'notification'
        unique_together = ('id',)
        verbose_name = 'Уведомление'


class TypesTests(models.Model):
    type_test = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'types_tests'
        unique_together = (('id',), ('type_test',))
        verbose_name = 'Типы тестов'


class Tests(models.Model):
    """Тесты с вопросами и ответами"""
    type_test = models.ForeignKey(TypesTests, on_delete=models.PROTECT)
    questions_test = models.TextField('Вопросы теста')
    answers_test = models.TextField('Ответы теста')
    true_answers_test = models.TextField('Правельный ответ')

    class Meta:
        managed = True
        db_table = 'tests'
        unique_together = ('id',)
        verbose_name = 'Тест'


class PassingTests(models.Model):
    """Результаты прохождения тестов сотрудниками"""
    worker = models.ForeignKey(Workers, on_delete=models.PROTECT)
    type_test = models.ForeignKey(TypesTests, on_delete=models.PROTECT)
    date = models.DateTimeField('Дата прохождения теста')
    number_of_attempts = models.IntegerField('Количество попыток прохождения теста')
    status = models.BooleanField('Статус прохождения теста')

    class Meta:
        managed = True
        db_table = 'passing_tests'
        unique_together = ('id',)
        verbose_name = 'Результат теста'


class Documents(models.Model):
    """Документы для ознакомления"""
    type_document = models.CharField(max_length=100)
    path_to_file = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'documents'
        unique_together = ('id',)
        verbose_name = 'Документ'
