from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import (
    CustomLoginView, logout_page, user_profile, RegisterView,
    ActiveAccountView
)


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login_page"),
    path('logout/', LogoutView.as_view(), name="logout_page"),
    path('registration/', RegisterView.as_view(), name="registration"),
    path('profile/', user_profile, name="profile"),
    path('activate/<str:uidb64>/<str:token>/', ActiveAccountView.as_view(), name="activate"),
]