from django.urls import path
from .views import DataList, DataDetail

urlpatterns = [
    path('<int:pk>/', DataDetail.as_view()),
    path('', DataList.as_view()),
]