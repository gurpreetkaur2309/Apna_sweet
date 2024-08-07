"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Apna import views
from Apna.views import index
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Apna/', include('Apna.urls')),
    path('',views.index,name="index"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('categories/<slug:val>', views.categories_view.as_view(), name='categories'),
    #  path('delete/<slug:val>', views.categories_view.as_view(), name='delete'),
    path('brands/<slug:val>', views.brands_view.as_view(), name='brands'),
    path('brands',views.brands,name='brand'),
    path('myorders/',views.myorders_view,name='myorders'),
    path('buynow/',views.buynow_view,name='buynow'),
    path('logout/',views.logout_page,name="logout_page"),
    path('categories',views.categories,name='category'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.show_cart,name='show_cart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
   
    path('clear_cart/',views.clear_cart,name='clear_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('receipt/',views.receipt,name='receipt'),

    path('receipts/',views.g,name='g'),
    # path("private_place/",views.private_place),
    # path("accounts/", include("django.contrib.auth.urls"))
    path('searchbar/',views.searchbar_view,name='searchbar'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
