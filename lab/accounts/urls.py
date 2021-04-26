from django.urls import path
from accounts.views.login import register_view, login_view
from accounts.views.logout import logout_view


app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', register_view, name='create_acc')
]