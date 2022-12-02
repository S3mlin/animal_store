from django.urls import path


from . import views

app_name = 'api'
urlpatterns = [
    path('entry/', views.entry, name='entry'),
    path('delete/', views.delete, name='delete'),
    path('edit/', views.edit, name='edit'),
]