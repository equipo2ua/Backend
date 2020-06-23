from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate,EmailUpdateCard
from registration import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),  
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('contact_form/', views.contact_form, name="contact_form"),
    path('profile/email_card/', EmailUpdateCard.as_view(), name="profile_email_card"),
] 