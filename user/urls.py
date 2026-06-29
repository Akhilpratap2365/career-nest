from django.urls import path
from.import views

urlpatterns=[
    path("",views.index),
    path("index/",views.index),
    path("aboutus/",views.about),
    path("team/",views.team),
    path("gallery/",views.gallery),
    path("category/",views.category),
    path("services/",views.services),
    path("job/",views.job),
    path("details/",views.details),
    path("contact/",views.contact),
    path("jobs/",views.jobs),
    path("company/",views.company),
    path("register/",views.register),
    path("ulogin/",views.ulogin),
    path("elogin/",views.elogin),
    path("profile/",views.profile),
    path("logout/",views.logout),
    path("alljobs/",views.alljobs),
    path("apply/",views.apply),
    path("application/",views.application)
    
]