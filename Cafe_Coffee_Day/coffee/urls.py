from django.urls import path
from coffee import views

urlpatterns=[
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('handlelogin',views.handlelogin,name="handlelogin")

]