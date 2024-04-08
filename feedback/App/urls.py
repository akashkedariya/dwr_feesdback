from django.urls import path
from .views import *
from App import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.login, name = 'login'),
    path('add_project/',views.add_project, name = 'add_project'),
    path('feedback/',views.feedback,name = 'feedback'),
    path('user_logout/',views.user_logout, name = 'user_logout'),
    path('feedback_history/',views.feedback_history,name = 'feedback_history'),
    
    path('dwr_feedback/',views.dwr_feedback, name = 'dwr_feedback'),
    path('dwr_feedback_history/',views.dwr_feedback_history,name = 'dwr_feedback_history'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
