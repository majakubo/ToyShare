from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from toyshare import views

urlpatterns = [
    path('myprofile/', views.MyProfile.as_view()),
    path('toys/', views.ToysList.as_view()),
    path('toys/<int:pk>', views.ToysDetail.as_view()),
    path('toys/<str:range>/<int:age>', views.ToySearchList.as_view()),
    path('rentings/', views.RentingList.as_view()),
    path('rentings/<int:pk>', views.RentingDetail.as_view()),
    path('wanted/', views.WantedList.as_view()),
    path('unwanted/', views.UnwantedList.as_view()),
    path('users/', views.UserList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)