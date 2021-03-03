from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from .models import *


class WorkersPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkersPosition
        fields = '__all__'


class WorkersSerializerFromList(serializers.ModelSerializer):
    position = WorkersPosition()

    class Meta:
        model = Workers
        fields = '__all__'


class WorkersSerializer(serializers.ModelSerializer):

    def validate_hr(self, hr):
        if hr > 0:
            if not Workers.objects.filter(id=hr).exists():
                raise serializers.ValidationError('Такого работника не существует')
            if not Workers.objects.filter(id=hr, position__name_position='hr'):
                raise serializers.ValidationError('Данный работник не hr')
        return hr

    def validate_mentor(self, mentor):
        if mentor > 0:
            if not Workers.objects.filter(id=mentor).exists():
                raise serializers.ValidationError('Такого работника не существует')

            if not Workers.objects.filter(id=mentor, position__name_position='наставник'):
                raise serializers.ValidationError('Данный работник не наставник')
        return mentor

    class Meta:
        model = Workers
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class ResultQuestionsSerializerList(serializers.ModelSerializer):
    type_questions = QuestionsSerializer()

    class Meta:
        model = ResultsQuestions
        fields = '__all__'


class ResultsQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultsQuestions
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = ['type_questions']


class PassingTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassingTests
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'], first_name = validated_data['first_name'],
                                        last_name = validated_data['last_name'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
