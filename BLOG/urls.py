
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view()),
    path('blog/',BlogView.as_view()),
    path('register/',register_view),
    path('maqola/<int:son>',MaqolaView.as_view()),
    path('logout/',logautview)
]
