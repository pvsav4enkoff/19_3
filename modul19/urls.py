from django.contrib import admin
from django.urls import path
from task1.views import task4_view_platform, task4_view_games, task4_view_cart
from task1.views import sign_up_by_html, sign_up_by_django
urlpatterns = [
    path('',sign_up_by_html),
    path('django_sign_up/',sign_up_by_django),
    path('platform/',task4_view_platform),
    path('platform/games/',task4_view_games),
    path('platform/cart/',task4_view_cart),
    path('admin/', admin.site.urls)
]