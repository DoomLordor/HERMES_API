from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import BaseFilterBackend

from django.db.models import Q

from django_filters import rest_framework as filters

from .models import *


class PaginationData(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class WorkersPositionFilter(filters.FilterSet):
    name_position = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        models = WorkersPosition
        fields = ('name_position',)


class WorkersFilter(filters.FilterSet):
    position = filters.NumberFilter()
    mentor = filters.NumberFilter()
    hr = filters.NumberFilter()
    user = filters.NumberFilter()
    class Meta:
        models = Workers
        fields = '__all__'


class ResultsQuestionsFilter(filters.FilterSet):
    type_questions = filters.CharFilter(lookup_expr='icontains')
    worker = filters.NumberFilter()

    class Meta:
        models = Workers
        fields = ('type_questions', 'worker')


class MessagesFilter(filters.FilterSet):
    recipient = filters.NumberFilter()
    sender = filters.NumberFilter()

    class Meta:
        models = Messages
        fields = ('recipient', 'sender')


class NotificationsFilter(filters.FilterSet):
    recipient = filters.NumberFilter()

    class Meta:
        models = Notifications
        fields = ('recipient',)


class TestsFilter(filters.FilterSet):
    type_tests = filters.NumberFilter()

    class Meta:
        models = Tests
        fields = ('type_tests',)


class PassingTestsFilter(filters.FilterSet):
    worker = filters.NumberFilter()

    class Meta:
        models = PassingTests
        fields = ('worker',)


class FilterMessagesByUser(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if not request.user.is_superuser:
            worker = Workers.objects.get(user=request.user)
            queryset = queryset.filter(Q(recipient=worker) | Q(sender=worker))
        return queryset
