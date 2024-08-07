# mynewapp/urls.py
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('categories/<slug:val>', views.categories_view.as_view(), name='categories'),
    path('brands/<slug:val>', views.brands_view.as_view(), name='brands'),
    path('brands',views.brands,name='brand'),
    path('myorders/',views.myorders_view,name='myorders'),
    path('buynow/',views.buynow_view,name='buynow'),
    path('logout/',views.logout_page,name="logout_page"),
    path('allproducts/',views.allproducts_view,name="allproducts"),
    path('apnasweet/',views.apnasweet_view,name="apnasweet"),
    path('categories',views.categories,name='category'),
    # path("accounts/", include("django.contrib.auth.urls"))

]
