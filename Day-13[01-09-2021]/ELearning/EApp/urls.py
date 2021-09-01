from django.urls import path
from EApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('aboutu/',views.about,name="abt"),
	path('cntc/',views.contact,name="cnt"),
	path('allcourses/',views.courses,name="crs"),
	path('upcr/<int:y>/',views.courseupdate,name="crup"),
	path('dlcr/<int:p>/',views.coursedelete,name="crdl"),
	path('suball/',views.suballcourse,name="sbal"),
	path('sbupd/<int:v>/',views.subcourseup,name="sbup"),
	path('subdlt/<int:h>/',views.subcoursedel,name="sbdl"),
]