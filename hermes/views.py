from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import *
import hermes.serializers as sr
import hermes.services as services
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from datetime import datetime

# Create your views here.
COMPARISON = {'GET': 'view', 'POST': 'add', 'PUT': 'change', 'PATCH': 'CHANGE', 'DELETE': 'delete', 'OPTIONS': 'view',
              'HEAD': 'view'}


class WorkersRest(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = sr.WorkersSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = services.WorkersFilter
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action != 'list':
            return self.serializer_class
        return sr.WorkersSerializerFromList

    def create(self, request, *args, **kwargs):
        all_tests = TypesTests.objects.all()
        res = super().create(request)
        date = datetime.now()
        for test in all_tests:
            serializer = sr.PassingTestsSerializer(data={'worker': res.data['id'], 'type_test': test.pk,
                                                         'date': date, 'number_of_attempts': 0, 'status': False})
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return res


class WorkersPositionRest(viewsets.ModelViewSet):
    queryset = WorkersPosition.objects.all()
    serializer_class = sr.WorkersPositionSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = services.WorkersPositionFilter


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = sr.UserSerializer


class UserByToken(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response({'id': str(request.user.id)}, status=status.HTTP_200_OK)


class MessagesRest(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = sr.MessagesSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter, services.FilterMessagesByUser)
    filterset_class = services.MessagesFilter
    permission_classes = (IsAuthenticated,)


class TestsRest(viewsets.ModelViewSet):
    queryset = Tests.objects.all()
    serializer_class = sr.TestsSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = services.TestsFilter
    permission_classes = (IsAuthenticated,)


class TypesTestsRest(viewsets.ModelViewSet):
    queryset = TypesTests.objects.all()
    serializer_class = sr.TestsSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    permission_classes = (IsAuthenticated,)


class QuestionsRest(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = sr.QuestionsSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    permission_classes = (IsAuthenticated,)


class ResultsQuestionsRest(viewsets.ModelViewSet):
    queryset = ResultsQuestions.objects.all()
    serializer_class = sr.ResultsQuestionsSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = services.ResultsQuestionsFilter
    permission_classes = (IsAuthenticated,)


class NotificationsRest(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = sr.NotificationSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = services.NotificationsFilter
    permission_classes = (IsAuthenticated,)


class DocumentsRest(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = sr.DocumentSerializer
    pagination_class = services.PaginationData
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    permission_classes = (IsAuthenticated,)

class PassingTestsRest(viewsets.ModelViewSet):
    queryset = PassingTests.objects.all()
    serializer_class = sr.PassingTestsSerializer
    pagination_class = services.PaginationData
    filterset_class = services.PassingTestsFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    permission_classes = (IsAuthenticated,)
