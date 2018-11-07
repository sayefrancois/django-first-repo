from django.conf.urls import url
from LogApp import views

app_name = 'LogApp'


urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
