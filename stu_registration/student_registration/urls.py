from django.urls import path
from . import views

urlpatterns = [
    # urls for class based view
    path('', views.StudentFormView.as_view(), name='student_insert'),
    path('list/', views.StudentListView.as_view(), name='student_list'),
    path('<int:id>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:id>', views.StudentDeleteView.as_view(), name='student_delete'),
    # urls for function based view
    # path('', views.student_form, name='student_insert'),
    # path('list/', views.student_list, name='student_list'),
    # path('<int:id>/', views.student_update, name='student_update'),
    # path('delete/<int:id>/', views.student_delete, name='student_delete'),
]
