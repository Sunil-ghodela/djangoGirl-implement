from django.conf.urls import url, include
from django.urls import path
from blog import views
from dashing.utils import router

urlpatterns = [
    url(r'dashboard/', include(router.urls)),
    url(r'post_list/', views.post_list, name = 'post_list'),
]
