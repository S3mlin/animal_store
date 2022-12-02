from django.urls import path


from . import views

app_name = 'animal-store'
urlpatterns = [
    path('', views.index, name='index'),
    path('entry/', views.entry, name='entry'),
    path('delete/<animal_id>', views.delete, name='delete'),
    path('edit/<animal_id>', views.edit, name='edit'),
    path('delete-tag/<tag_id>', views.delete_tag, name='delete-tag'),
    path('animal-list/', views.AnimalListAPIView.as_view(), name='animal-list'),
    path('selected-tag/<tag_id>', views.selected_tag, name='selected-tag'),
]
