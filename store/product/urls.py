from django.urls import path
from .views import *

urlpatterns = [
    # path('',about,name="about"),
    # path('self/',self1,name="self"),
    # path('contact/',contact,name="contact"),
    # path('about/',about,name='about'),
    # path('basicdtl/',basicdtl,name='basicdtl'),
    path('',register_user,name='register'),
    path('home/',home,name='home'),
    path('service/',services,name='service'),
    path('boot/',bootstrap,name='bootstrap'),
    path('aboutnav/',aboutnav,name='aboutnav'),
    path('contactnav/',hos_contact,name='contactnav'),
    path('booking1/',hos_booking,name='booking1'),
    path('dept/',dept,name='dept'),
    path('doc/',doc,name='doc'),
    path('deptlist/', DeptListView.as_view(), name='deptlist'),
    path('depdetail/<int:pk>', DeptDetailed.as_view(), name='depdetail'),
    path('depupdate/<int:pk>', TaskUpdateView.as_view(), name='depypdate'),
    path('depdelete/<int:pk>', TaskViewDelete.as_view(), name='depdelete'),
    path('deptcreate/', TaslViewCreate.as_view(), name='deptcreate')




]