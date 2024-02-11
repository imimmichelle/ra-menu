from django.urls import path
from . import views

app_name = 'draft'

urlpatterns = [
    #path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('preferences/', views.preferences, name='preferences'),
    path('usersform/', views.usersform, name='usersform'),
    path('newdesire/', views.newdesire, name='newdesire'),
    path('survey/', views.survey, name='survey'),
    path('compatibility/', views.compatibility, name='compatibility'),
    path('users/<int:user1_id>-<int:user2_id>', views.users_smb),
    path('newanswer', views.newanswer, name='newanswer'),
    #path('', views.results, name = 'results')
]