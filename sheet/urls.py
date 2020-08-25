from django.urls import path
from . import views

app_name = 'sheet'

urlpatterns = [
	path('sheet/', views.ledger_view,name='ledger_sheet'),
	path('sheet/<int:pk>/', views.grp_view, name = 'grp_view'),
	path('sheet/del/<int:pk>/', views.transaction_del, name = 'transaction_del'),
	path('sheet/del/decision/<int:pk>/', views.go, name = 'go')
    # path('sheet/<str:x>/', views.ledger_view,name='ledger_sheet')
]
