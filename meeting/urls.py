from django.urls import path
from .views import details, rooms, form, remove
urlpatterns = [
    path('<int:id>', details, name='details'),
    path('rooms', rooms, name='rooms'),
    path('new', form, name='form'),
    path('remove', remove, name='remove')
]