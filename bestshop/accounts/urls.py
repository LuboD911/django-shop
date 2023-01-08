from django.urls import path

from bestshop.accounts.views import logout_user, profile_details, SignUpView, SignInView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('profile/', profile_details, name='profile details'),

)