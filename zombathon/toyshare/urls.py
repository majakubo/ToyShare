from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from toyshare import views

urlpatterns = [
    path('myprofile/', views.MyProfile.as_view()),
    path('add_toy/', views.ToysCreate.as_view()),
    path('toys/', views.ToysList.as_view()),
    path('toys/<int:id>', views.ToysDetail.as_view()),
    path('search/<String:range/<int:age>', views.SearchList.as_view()),
    path('rentings/', views.RentingList.as_view()),
    path('rentings/<int:id>', views.RentingDetail.as_view()),
]
