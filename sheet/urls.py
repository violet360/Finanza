from django.urls import path
from . import views

app_name = 'sheet'

urlpatterns = [
    path('sheet/', views.ledger_view,name='ledger_sheet')
]
