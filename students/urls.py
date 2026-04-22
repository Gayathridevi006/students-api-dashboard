from django.urls import path
from .views import StudentListCreateView, StudentDetailView, home_view, login_view

urlpatterns = [
    path('students/',      StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(),  name='student-detail'),
    path('', home_view, name='home'),
    # path('login/', login_view, name='login'),

]