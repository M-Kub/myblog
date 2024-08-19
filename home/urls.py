from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.home, name='index'),
    path('', views.post_list, name='post_list'),
    path('post/(<int:pk>)/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/(<int:pk>)/edit/', views.post_edit, name='post_edit'),
    path('about/', views.about, name='about'),
    path('impressum/', views.impressum, name='impressum')


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
