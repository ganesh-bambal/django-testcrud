from django.urls import path

from . import views
app_name = 'testapp'

urlpatterns = [
    path('', views.BookList.as_view(), name='employee_list'),
    path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
    path('new', views.BookCreate.as_view(), name='book_new'),
    path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
    path('edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
    # path('register/',views.register,name='register'),
    # path('logout/',views.user_login,name='user_login'),

    # path('new', views.EmployeeCreate.as_view(), name='employee_new'),
    # path('delete/<int:pk>', views.EmployeeDelete.as_view(), name='employee_delete'),
    # path('edit/<int:pk>', views.EmployeeUpdate.as_view(), name='employee_edit'),
    # path('', views.EmployeeList.as_view(), name='employee_list'),
    # path('view/<int:pk>', views.EmployeeView.as_view(), name='employee_view'),
]