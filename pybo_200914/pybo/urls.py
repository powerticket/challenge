from django.urls import path
from . import views


app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('answer/create/<int:pk>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

]
