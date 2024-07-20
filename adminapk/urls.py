from django.urls import path
from adminapk import views

urlpatterns = [
#========================================================================================
    #BRANCH
    path('branch_management_view/', views.branch_management_view,name='branch_management_view'),
    # BRANCH

    path('addbm/', views.addbm, name='addbm'),
    path('deletebm/<int:pk>', views.deletebm, name='deletebm'),
    path('editbm/', views.editbm, name='editbm'),
    path('updatebm/<int:id>/', views.updatebm, name='updatebm'),
    path('branch_management/togglestatusbm/<int:item_id>/', views.togglestatusbm, name='togglestatusbm'),
#======================================================================================
    # path('settings/', views.settings, name='settings'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    # path('hotel_profile_view/', views.hotel_profile_view, name='hotel_profile_view'),
    path('addhp/', views.addhp, name='addhp'),
    path('deletehp/<int:pk>', views.deletehp, name='deletehp'),
    path('edithp/', views.edithp, name='edithp'),
    path('updatehp/<int:id>/', views.updatehp, name='updatehp'),

#========================================================================================
    # Adding rooms
    path('adding_rooms/', views.adding_rooms, name='adding_rooms'),
    path('addad/', views.addad, name='addad'),
    path('deletead/<int:pk>', views.deletead, name='deletead'),
    path('editad/', views.editad, name='editad'),
    path('updatead/<int:id>/', views.updatead, name='updatead'),
    path('Adding_Rooms/togglestatusar/<int:item_id>/', views.togglestatusar, name='togglestatusar'),
#========================================================================================
    #reservations
    path('reservations/', views.reservations,name='reservations'),
    path('addreservation/', views.addreservation, name='addreservation'),
    path('deletereservarions/<int:pk>', views.deletereservarions, name='deletereservarions'),

    path('editreservarions/', views.editreservarions, name='editreservarions'),
    path('updatereservarions/<int:id>/', views.updatereservarions, name='updatereservarions'),
    path('reservation/togglestatus/<int:item_id>/', views.togglestatus, name='togglestatus'),
#========================================================================================
    #Admin_staff
    path('admin_staff_view/', views.admin_staff_view,name='admin_staff_view'),
    path('addas/', views.addas, name='addas'),
    path('deleteas/<int:pk>', views.deleteas, name='deleteas'),
    path('editas/', views.editas, name='editas'),
    path('updateas/<int:id>/', views.updateas, name='updateas'),
path('Admin_staff/togglestatus12/<int:item_id>/', views.togglestatus12, name='togglestatus12'),
#========================================================================================
    #food_service
    path('food_service/', views.food_service,name='food_service'),

    path('deletefood/<int:pk>', views.deletefood, name='deletefood'),
    path('editfood/', views.editfood, name='editfood'),
    path('updatefood/<int:id>/', views.updatefood, name='updatefood'),
    path('Food_Services/togglestatusff/<int:item_id>/', views.togglestatusff, name='togglestatusff'),
#========================================================================================
    path('security/', views.security, name='security'),
    # ===================================================================================================================
    # ===================================================================================================================
    path('cctv_view/', views.cctv_view, name='cctv_view'),
    path('addcctv/', views.addcctv, name='addcctv'),
    path('deletecctv/<int:pk>', views.deletecctv, name='deletecctv'),
    path('editcctv/', views.editcctv, name='editcctv'),
    path('updatecctv/<int:id>/', views.updatecctv, name='updatecctv'),
    path('cctv/togglestatuscctv/<int:item_id>/', views.togglestatuscctv, name='togglestatuscctv'),
    # ===================================================================================================================
    # ===================================================================================================================
    path('fire_view/', views.fire_view, name='fire_view'),
    path('addfire/', views.addfire, name='addfire'),
    path('deletefire/<int:pk>', views.deletefire, name='deletefire'),
    path('editfire/', views.editfire, name='editfire'),
    path('updatefire/<int:id>/', views.updatefire, name='updatefire'),
    path('fire/togglestatusfire/<int:item_id>/', views.togglestatusfire, name='togglestatusfire'),
    # ===================================================================================================================
    # ===================================================================================================================
    # path('medical_view/', views.medical_view, name='medical_view'),
    # path('addmd/', views.addmd, name='addmd'),
    # path('deletemd/<int:pk>', views.deletemd, name='deletemd'),
    # path('editmd/', views.editmd, name='editmd'),
    # path('updatemd/<int:id>/', views.updatemd, name='updatemd'),
    # path('medical/togglestatusmed/<int:item_id>/', views.togglestatusmed, name='togglestatusmed'),

    # ===================================================================================================================
    path('settings_view/', views.settings_view, name='settings_view'),

    # ===================================================================================================================
    path('amenities_views/', views.amenities_views, name='amenities_views'),
    path('addamenities/', views.addamenities, name='addamenities'),
    path('deleteeme/<int:pk>', views.deleteeme, name='deleteeme'),
    path('editeme/', views.editeme, name='editeme'),
    path('updateeme/<int:id>/', views.updateeme, name='updateeme'),
    path('amenities/togglestatusame/<int:item_id>/', views.togglestatusame, name='togglestatusame'),
    # ===================================================================================================

    # ===================================================================================================
    path('currency_view/', views.currency_view, name='currency_view'),
    path('addcurrency/', views.addcurrency, name='addcurrency'),
    path('deletecur/<int:pk>', views.deletecur, name='deletecur'),
    path('editemp/', views.editemp, name='editemp'),
    path('updatecur/<int:id>/', views.updatecur, name='updatecur'),
    path('currency/togglestatuscurrency/<int:item_id>/', views.togglestatuscurrency, name='togglestatuscurrency'),
    # ===================================================================================================

    # ===================================================================================================
    path('elmpoyee_view/', views.elmpoyee_view, name='elmpoyee_view'),
    path('addemp/', views.addemp, name='addemp'),
    path('deleteemp/<int:pk>', views.deleteemp, name='deleteemp'),
    path('editcur/', views.editcur, name='editcur'),
    path('updateemp/<int:id>/', views.updateemp, name='updateemp'),
    path('Designation/togglestatusemp/<int:item_id>/', views.togglestatusemp, name='togglestatusemp'),
    #=========================================================================================================
     #=========================================================================================================

    path('Department_view/', views.Department_view, name='Department_view'),
    path('adddep/', views.adddep, name='adddep'),
    path('deletedep/<int:pk>', views.deletedep, name='deletedep'),
    path('editdep/', views.editdep, name='editdep'),
    path('updatedep/<int:id>/', views.updatedep, name='updatedep'),
    path('Department/togglestatusdep/<int:item_id>/', views.togglestatusdep, name='togglestatusdep'),

    # ===================================================================================================

    # ===================================================================================================
    path('hotel_view/', views.hotel_view, name='hotel_view'),
    path('addhot/', views.addhot, name='addhot'),
    path('deletehot/<int:pk>', views.deletehot, name='deletehot'),
    path('edithot/', views.edithot, name='edithot'),
    path('updatehot/<int:id>/', views.updatehot, name='updatehot'),
    path('hotel/togglestatusth/<int:item_id>/', views.togglestatusth, name='togglestatusth'),
    # ===================================================================================================

    # ===================================================================================================
    path('language_view/', views.language_view, name='language_view'),
    path('addlanguage/', views.addlanguage, name='addlanguage'),
    path('deletelan/<int:pk>', views.deletelan, name='deletelan'),
    path('editlan/', views.editlan, name='editlan'),
    path('updatelan/<int:id>/', views.updatelan, name='updatelan'),
    path('language/togglestatuslan/<int:item_id>/', views.togglestatuslan, name='togglestatuslan'),
    # ===================================================================================================

    # ============================================================================================================
    # ROOM
    path('room_view/', views.room_view, name='room_view'),
    path('addroom/', views.addroom, name='addroom'),
    path('deleteroom/<int:pk>', views.deleteroom, name='deleteroom'),
    path('editroom/', views.editroom, name='editroom'),
    path('updateroom/<int:id>/', views.updateroom, name='updateroom'),
    path('room/togglestatusT/<int:item_id>/', views.togglestatusT, name='togglestatusT'),

    # ===================================================================================================================
    path('service_view/', views.service_view, name='service_view'),
    path('addservice/', views.addservice, name='addservice'),
    path('deleteservice/<int:pk>', views.deleteservice, name='deleteservice'),
    path('editservice/', views.editservice, name='editservice'),
    path('updateservice/<int:id>/', views.updateservice, name='updateservice'),
    path('service/togglestatusser/<int:item_id>/', views.togglestatusser, name='togglestatusser'),
#=======================================================================================================================
    path('', views.login, name='login'),

    path('logout', views.log_out, name='logout'),


#=======================================================================================================================
    path('manageuser/', views.manageuser_view, name='manageuser'),
    path('addmanageuser/', views.addmanageuser, name='addmanageuser'),
    path('deleteuser/<int:pk>', views.deleteuser, name='deleteuser'),
    path('edit_MU/<int:pk>', views.edit_MU, name='edit_MU'),
    path('updateuser/<int:id>/', views.updateuser, name='updateuser'),
    path('Manageusers/togglestatus1/<int:item_id>/', views.togglestatus1, name='togglestatus1'),
#=======================================================================================================================
    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),

    ]
