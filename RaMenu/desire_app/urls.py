from django.urls import path
from . import views

app_name = 'desire_app'

urlpatterns = [
    path('newcategory/', views.newcategory, name='newcategory'),
    path('category_exists/', views.category_exists, name='category_exists'),
    path('newdesire/', views.newdesire, name='newdesire'),
    path('newdesirelist/<int:category_id>', views.newdesirelist, name='newdesirelist'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>', views.category_list),
]