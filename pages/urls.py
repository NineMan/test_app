from django.urls import path

from .views import PageDetailView
from .views import PageListView

app_name = 'app'
urlpatterns = [
    path('pages/', PageListView.as_view(), name='pages'),
    path('pages/<int:pk>', PageDetailView.as_view(), name='page-detail'),

]

