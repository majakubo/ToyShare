from django.urls import path

urlpatterns = [
    path('myprofile/', views.MyProfile.as_view()),
    path('toys/', views.ToysList.as_view()),
    path('toys/<int:id>', views.ToysDetail.as_view()),
    path('toys/<String:range/<int:age>', views.ToySearchList.as_view()),
    path('rentings/', views.RentingList.as_view()),
    path('rentings/<int:id>', views.RentingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)