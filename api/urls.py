from django.urls import path, include
from .views import CustomPersonList, CustomPersonDetail, TeamList, TeamDetail

urlpatterns = [
    path('person/', CustomPersonList.as_view()),
    path('person/<int:pk>/', CustomPersonDetail.as_view()),
    path('team/', TeamList.as_view()),
    path('team/<int:pk>/', TeamDetail.as_view())
]