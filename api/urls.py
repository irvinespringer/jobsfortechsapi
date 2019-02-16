from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    
    path('jobs/<int:job_id>', views.JobsView.as_view(), name='id-jobs'),
    path('jobs/', views.JobsView.as_view(), name='all-jobs'),
    
    path('candidates/<int:candidate_id>', views.CandidatesView.as_view(), name='id-candidates'),
    path('candidates/', views.CandidatesView.as_view(), name='all-candidates'),
    
    path('blogs/<int:blog_id>', views.BlogsView.as_view(), name='id-blogs'),
    path('blogs/', views.BlogsView.as_view(), name='all-blogs'),
]
