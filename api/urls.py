from django.urls import include , path
from home import views

urlpatterns = [
    path('',views.ApiView, name = 'ApiView'),
    path('add/',views.Add, name = 'add student'),
    path('AllStudents/',views.AllStudents, name = 'all students'),
    path('update/<int:pk>/', views.Update, name = 'update'),
]