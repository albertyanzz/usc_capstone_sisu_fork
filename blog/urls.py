from django.urls import include, re_path
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from .views import IndexView

urlpatterns = [
    re_path('', views.index, name='index' ),
    # url(r'^$', views.about_sisu, name='about'),
    
    re_path('about-us/', views.about_us, name='about-us'),

    re_path('about_us/team', views.about_team, name='about_team'),
    re_path('about_us/empower_now', views.about_program, name='about_program'),
    re_path('post/', views.post_list, name='post_list'),
    re_path('post/new/', views.post_new, name='post_new'),
    re_path('drafts/', views.post_draft_list, name='post_draft_list'),
    
    re_path('post/(<pk>\d+)/publish/', views.post_publish, name='post_publish'),
    re_path('post/(<pk>\d+)/remove/', views.post_remove, name='post_remove'),
    re_path('post/(<pk>\d+)/edit/', views.post_edit, name='post_edit'),
    re_path('comment/(<pk>\d+)/approve/', views.comment_approve, name='comment_approve'),
    re_path('comment/(<pk>\d+)/remove/', views.comment_remove, name='comment_remove'),
    re_path('post/category/(<category_name>\w+)', views.post_list_by_category, name='post_list_by_category'),
    re_path('cases', views.post_cases, name='post_cases'),
    #path('contact_us', views.contact_us, name='contact_us'),
    re_path('sisu_case/category/(<category_name>\w+)', views.story, name='story'),
    re_path('sisu_case/(<pk>\d+)/', views.story_entry, name='story_entry'),
    re_path('user_details/user_id/(<pk>\d+)/', views.user_details, name='user_details'),
    
    # path('likepost/', views.on_off_star, name='on_off_star'),
    # path('add_comment/', views.add_comment_to_post, name='add_comment_to_post'),
    re_path('add_reply_to_comment', views.add_reply_to_comment, name='add_reply_to_comment'),
    re_path('search', views.search, name='search'),
    #url(r'^settings/user_id(?P<pk>\d+)/$', IndexView.as_view(), name='user_details'),

    re_path('sisu_case/category/', views.get_all_category, name='get_all_category'),
    re_path('enp_login/', views.login_portal, name='login_portal'),
    re_path('employee_progress/', views.employee_progress, name='employee_progress'),
    re_path('supervisor_progress/', views.supervisor_progress, name='supervisorprogress'),
    re_path('nonsupervisor_progress/', views.nonsupervisor_progress, name='nonsupervisorprogress'),
    re_path('modules/', views.modules, name='modules'),
    re_path('downloads/', views.downloads, name='downloads'),
    re_path('modules_s/', views.modules_s, name='modules_s'),
    re_path('downloads_s/', views.downloads_s, name='downloads_s'),
    re_path('employee_reg', views.employee_reg, name='employee_reg'),
    re_path('send_reg/', views.send_reg, name='send_reg'),
    re_path('reg_from_invite', views.reg_from_invite, name='reg_from_invite'),

    re_path('terms_conditions/', views.terms_conditions, name='t_c'),
    re_path('privacy_policy/', views.privacy_policy, name='p_p'),

    re_path('header/', views.header, name='header'),


    # PUBLIC SITE - START
    re_path('faq', views.faq, name='faq'),
    re_path('contact', views.contact, name='contact'),
    # PUBLIC SITE - END
    
    # Training Portal Authentication / Login / Logout - START
    re_path('auth-login/', views.portal_login, name='portal_login'),
    re_path('auth-login-trial/', views.portal_login_trial, name='portal_login_trial'),
    re_path('auth-logout/', views.portal_logout, name='portal_logout'),
    re_path('auth-register/', views.portal_signup, name='portal_signup'),
    re_path('redeem/', views.key_redeem, name='key_redeem'),
    # Training Portal Authentication / Login / Logout - START


    # Training Portal - START
    re_path('portal/home/', views.portal_home, name='home_portal'),
    re_path('portal/register/', views.portal_register, name='register'),
    re_path('portal/edit-registration/', views.portal_edit_registration, name='edit-registration'),
    re_path('portal/edit-registration/edit-user', views.portal_edit_user, name='edit-user'),
    re_path('portal/edit-registration/remove-user', views.portal_remove_user, name='remove-user'),
    re_path('portal/downloads/', views.portal_training_dl, name='downloads'),
    re_path('portal/downloads_trial/', views.portal_training_dl_trial, name='downloads_trial'),
    re_path('portal/progress/', views.portal_employee_progress, name='progress'),
    re_path('portal/settings/', views.portal_settings, name='settings'),
    re_path('portal/post-program-survey/<str:pk>', views.post_program_survey, name='post_program_survey'),
    re_path('portal/save-survey/<str:pk>', views.save_survey, name='save_survey'),
    re_path('portal/ethical-report/<str:pk>', views.portal_ethical_report, name='ethical_report'),
    re_path('portal/certificate/', views.portal_certificate, name='certificate'),
    re_path('portal/change_pwd/', views.portal_change_password, name='portal_pwd'),
    # Training Portal - END

    # PASSWORD RECOVERY URLS ARE IN users/urls.py

]
