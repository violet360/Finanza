from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views as core_views

# app_name = 'sheet'

urlpatterns = [
	path('signup/', core_views.signup, name='signup'),
	path('login/', LoginView.as_view(template_name='registration/login.html'), name = 'login'),
	path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
	# path('signup/', core_views.signup, name = 'signup')
	# path('login/', core_views.login, name = 'login'),
	# path('logout/', core_views.logout, name = 'logout'),

]
