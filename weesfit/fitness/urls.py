from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    


    path('login/', auth_views.LoginView.as_view(template_name='fitness/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    # path('success/', views.success, name='onboarding_success'),
    path('', views.home, name='home'),  
    # path('onboarding/', views.onboarding, name='onboarding'),
    # path('onboarding2/', views.onboarding2, name='onboarding2'),
    # path('onboarding3/', views.onboarding3, name='onboarding3'),
    # path('onboarding4/', views.onboarding4, name='onboarding4'),
    # path('onboarding5/', views.onboarding5, name='onboarding5'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_user, name='register'),
    # path('login/', views.login_user, name='login'),
    path('track-features/', views.track_features, name='track_features'),
    path('bmi-calculator/', views.bmi_calculator, name='bmi_calculator'),
    path('personal-plans/', views.personal_plans, name='personal_plans'),
    path('community/', views.community, name='community'),
    path('weight-monitor/', views.weight_monitor, name='weight_monitor'),
    path('daily-routines/', views.daily_routines_view, name='daily_routines'),
    # path('success/', views.success_view, name='onboarding_success'),

    # path('', views.dashboard, name='dashboard'),
    path('bmi/', views.bmi_form, name='bmi_form'),
    path('bmi/result/', views.bmi_result, name='bmi_result'),
    path('plan/', views.bmi_plan, name='bmi_plan'), 
    path('track/', views.track_progress, name='track_progress'),
    path('personal-plans/', views.personal_plans, name='personal_plans'),
    path('plan-detail/<slug:goal_slug>/', views.plan_detail, name='plan_detail'),
]
