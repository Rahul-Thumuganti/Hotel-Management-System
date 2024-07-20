from django.urls import path
from . import views


urlpatterns = [
#========================================================================================
    #BRANCH
    path('', views.home_view,name='home_view'),
    path('about_view/', views.about_view,name='about_view'),
    path('restarunts_view/', views.restarunts_view,name='restarunts_view'),
    path('rooms_view/', views.rooms_view,name='rooms_view'),
    path('blog_view/', views.blog_view,name='blog_view'),
    path('contact_view/', views.contact_view,name='contact_view'),
    path('my_account_view/', views.my_account_view,name='my_account_view'),
    path('user_login/', views.user_signin, name='user_login'),
    path('user_reg/', views.user_signup, name='user_reg'),
    path('user_signout/', views.user_signout, name='user_signout'),
    path('user_otp/<int:pk>', views.user_otp_verification, name='user_otp'),
    #============================================================================================================
    path('book_view/<int:pk>/', views.book_view,name='book_view'),
    path('addreservation/', views.addreservation,name='addreservation'),
    path('room_view1/<int:pk>/', views.room_view1,name='room_view1'),
    path('terms/', views.terms,name='terms'),
    path('mybooking/', views.mybooking,name='mybooking'),
    path('togglestatus/', views.togglestatus,name='togglestatus'),
    # path('addmanage/', views.addmanage,name='addmanage'),




    ]