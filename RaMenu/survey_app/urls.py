from django.urls import path
from . import views

app_name = 'survey_app'

urlpatterns = [
        path('newsurvey/', views.newsurvey, name='newsurvey'),
        path('entercode/', views.entercode, name='entercode'),
        path('code_not_exists/', views.code_not_exists, name='code_not_exists'),
        path('survey/<str:code>', views.survey, name='survey'),
        path('results/<str:code>', views.results, name='results'),
        path('resultlist', views.resultlist, name='resultlist'),
]