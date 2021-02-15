from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/<int:id>/', views.SubcategoryNews.as_view(), name='sub_category'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('getSubcategory/', views.get_sub_category)
]
