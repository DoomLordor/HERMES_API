from django.urls import path

from . import views
LIST_VIEW_METHODS = {'get': 'list', 'post': 'create'}
OBJECT_VIEW_METHODS = {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}

urlpatterns = [
    path('RegisterUser/', views.UserCreate.as_view()),
    path('UserByToken/', views.UserByToken.as_view()),

    path('Workers/', views.WorkersRest.as_view(LIST_VIEW_METHODS)),
    path('Workers/<int:pk>/', views.WorkersRest.as_view(OBJECT_VIEW_METHODS)),

    path('WorkersPosition/', views.WorkersPositionRest.as_view(LIST_VIEW_METHODS)),
    path('WorkersPosition/<int:pk>/', views.WorkersPositionRest.as_view(OBJECT_VIEW_METHODS)),

    path('Messages/', views.MessagesRest.as_view(LIST_VIEW_METHODS)),
    path('Messages/<int:pk>/', views.MessagesRest.as_view(OBJECT_VIEW_METHODS)),

    path('Tests/', views.TestsRest.as_view(LIST_VIEW_METHODS)),
    path('Tests/<int:pk>/', views.TestsRest.as_view(OBJECT_VIEW_METHODS)),

    path('TypesTests/', views.TypesTestsRest.as_view(LIST_VIEW_METHODS)),
    path('TypesTests/<int:pk>/', views.TypesTestsRest.as_view(OBJECT_VIEW_METHODS)),

    path('Questions/', views.QuestionsRest.as_view(LIST_VIEW_METHODS)),
    path('Questions/<int:pk>/', views.QuestionsRest.as_view(OBJECT_VIEW_METHODS)),

    path('ResultsQuestions/', views.ResultsQuestionsRest.as_view(LIST_VIEW_METHODS)),
    path('ResultsQuestions/<int:pk>/', views.ResultsQuestionsRest.as_view(OBJECT_VIEW_METHODS)),

    path('Notifications/', views.NotificationsRest.as_view(LIST_VIEW_METHODS)),
    path('Notifications/<int:pk>/', views.NotificationsRest.as_view(OBJECT_VIEW_METHODS)),

    path('Documents/', views.DocumentsRest.as_view(LIST_VIEW_METHODS)),
    path('Documents/<int:pk>/', views.DocumentsRest.as_view(OBJECT_VIEW_METHODS)),
]
