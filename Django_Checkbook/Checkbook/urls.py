from django.urls import path
from . import views

urlpatterns = [
    path('checkbook', views.checkbook, name='checkbook'),
    path('<int:pk>/balance/', views.balanceSheet, name='balanceSheet'),
    path('createaccount/', views.create_account, name='newAccount'),
    path('addtransaction/', views.transaction, name='addTransaction'),
]