from django.urls import path
from accounts.views import login_page, logout_page, user_profile


urlpatterns = [
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('profile/', user_profile, name="profile"),
]