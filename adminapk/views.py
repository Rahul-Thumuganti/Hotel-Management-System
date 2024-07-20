# Create your views here.
from django.shortcuts import render, redirect
from .models import branch_management, room, amenities, currency, language, service, Designation, Department, hotel, \
    cctv, fire, reservation, Admin_staff, Adding_Rooms, Hotel_Profile, Food_Services, Manageusers
from django.shortcuts import get_object_or_404
from datetime import date

from django.contrib.auth import logout
from django.contrib import auth

# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.utils import timezone


# ========================================================================================================================


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


# Hotel Profile
@login_required(login_url='login')
def admin_profile(request):
    profile = Hotel_Profile.objects.all()

    context = {
        'profile': profile,
    }

    return render(request, 'admin_profile.html', context)


@login_required(login_url='login')
def addhp(request):
    hp_b = Hotel_Profile.objects.all()

    if request.method == 'POST':
        Hotel_name = request.POST.get('Hotel_name')
        username = request.POST.get('username')
        Hotel_registration_number = request.POST.get('Hotel_registration_number')
        contact_by_mobile = request.POST.get('contact_by_mobile')
        contact_by_mail = request.POST.get('contact_by_mail')
        About_us = request.POST.get('About_us')
        description = request.POST.get('description')
        hotel_image = request.POST.get('hotel_image')

        c = Hotel_Profile(
            Hotel_name=Hotel_name,
            username=username,
            Hotel_registration_number=Hotel_registration_number,
            contact_by_mobile=contact_by_mobile,
            contact_by_mail=contact_by_mail,
            About_us=About_us,
            description=description,
            hotel_image=hotel_image,

        )
        c.save()
        return redirect('hotel_profile_view')

    return render(request, 'hotel_profile.html', {'hp_b': hp_b})


@login_required(login_url='login')
def deletehp(request, pk):
    b = Hotel_Profile.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('hotel_profile_view')


@login_required(login_url='login')
def edithp(request, pk):
    hp_e = Hotel_Profile.objects.get(id=pk)
    context = {
        'hp_e': hp_e
    }
    return render(request, 'hotel_profile.html', context)


@login_required(login_url='login')
def updatehp(request, id):
    if request.method == 'POST':
        Hotel_name = request.POST.get('Hotel_name')
        username = request.POST.get('username')
        Hotel_registration_number = request.POST.get('Hotel_registration_number')

        contact_by_mobile = request.POST.get('contact_by_mobile')
        contact_by_mail = request.POST.get('contact_by_mail')
        About_us = request.POST.get('About_us')
        description = request.POST.get('description')

        hotel_image = request.POST.get('hotel_image')

        s = Hotel_Profile(
            Hotel_name=Hotel_name,
            username=username,
            Hotel_registration_number=Hotel_registration_number,
            contact_by_mobile=contact_by_mobile,
            contact_by_mail=contact_by_mail,
            About_us=About_us,
            description=description,
            hotel_image=hotel_image,

        )
        s.save()
        return redirect('hotel_profile_view')

    return render(request, 'hotel_profile.html')


# ==============================================================================================================================
# branch management
@login_required(login_url='login')
def branch_management_view(request):
    bb_a = branch_management.objects.all()

    context = {
        'bb_a': bb_a,
    }
    return render(request, 'branch_management.html', context)


@login_required(login_url='login')
def addbm(request):
    cc_b = branch_management.objects.all()

    if request.method == 'POST':
        branch_image = request.POST.get('branch_image')
        room_numbers = request.POST.get('room_numbers')
        contact_by_mobile = request.POST.get('contact_by_mobile')
        contact_by_mail = request.POST.get('contact_by_mail')
        country = request.POST.get('country')
        state = request.POST.get('state')
        Branchlocation = request.POST.get('Branchlocation')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')

        c = branch_management(

            branch_image=branch_image,
            room_numbers=room_numbers,
            contact_by_mobile=contact_by_mobile,
            contact_by_mail=contact_by_mail,
            country=country,
            state=state,
            Branchlocation=Branchlocation,
            city=city,
            pincode=pincode,
            address=address,
            status=status,
            created_at=created_at

        )
        c.save()
        return redirect('branch_management_view')

    return render(request, 'branch_management.html', {'cc_b': cc_b})


@login_required(login_url='login')
def deletebm(request, pk):
    b = branch_management.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('branch_management_view')


@login_required(login_url='login')
def editbm(request, pk):
    cc_e = branch_management.objects.get(id=pk)
    context = {
        'cc_e': cc_e
    }
    return render(request, 'branch_management.html', context)


@login_required(login_url='login')
def updatebm(request, id):
    if request.method == 'POST':
        branch_image = request.POST.get('branch_image')
        room_numbers = request.POST.get('room_numbers')
        contact_by_mobile = request.POST.get('contact_by_mobile')
        contact_by_mail = request.POST.get('contact_by_mail')
        country = request.POST.get('country')
        state = request.POST.get('state')
        Branchlocation = request.POST.get('Branchlocation')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')

        s = branch_management(
            id=id,

            branch_image=branch_image,
            room_numbers=room_numbers,
            contact_by_mobile=contact_by_mobile,
            contact_by_mail=contact_by_mail,
            country=country,
            state=state,
            Branchlocation=Branchlocation,
            city=city,
            pincode=pincode,
            address=address,

        )
        s.save()
        return redirect('branch_management_view')


def togglestatusbm(request, item_id):
    item = branch_management.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('branch_management_view')


# ==============================================================================================================================
#Adding Rooms
@login_required(login_url='login')
def adding_rooms(request):
    room_type = room.objects.all()
    city = branch_management.objects.all()
    ad_a = Adding_Rooms.objects.all()

    context = {
        'room_type': room_type,
        'ad_a': ad_a,
        'city': city
    }
    return render(request, 'adding_rooms.html', context)

@login_required(login_url='login')
def addad(request):
    ad_b = Adding_Rooms.objects.all()
    room_type = room.objects.all()


    if request.method == 'POST':
        city_id=request.POST.get('city')
        city = branch_management.objects.get(id=city_id)
        Room_image = request.POST.get('Room_image')
        Room_number = request.POST.get('Room_number')
        Room_area = request.POST.get('Room_area')
        room_type_id = request.POST.get('room_type')
        room_type = room.objects.get(id=room_type_id)
        No_of_beds = request.POST.get('No_of_beds')
        Price = request.POST.get('Price')
        Room_description = request.POST.get('Room_description')
        status=request.POST.get('status')



        c = Adding_Rooms(

            city=city,
            Room_image=Room_image,
            Room_number=Room_number,
            Room_area=Room_area,
            room_type=room_type,
            No_of_beds=No_of_beds,
            Price=Price,
            Room_description=Room_description,
            status=status,

        )
        c.save()
        return redirect('adding_rooms')


    return render(request, 'adding_rooms.html', {'ad_b': ad_b, 'room_type': room_type})

@login_required(login_url='login')
def deletead(request, pk):
    b = Adding_Rooms.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('adding_rooms')

@login_required(login_url='login')
def editad(request, pk):
    ad_e = Adding_Rooms.objects.get(id=pk)
    room_type = room.objects.all()
    city = branch_management.objects.all()
    context = {
        'ad_e': ad_e,
        "room_type": room_type,
        'city': city,
    }
    return render(request, 'adding_rooms.html', context)

@login_required(login_url='login')
def updatead(request, id):
    if request.method == 'POST':

        city_id = request.POST.get('city')
        city = branch_management.objects.get(id=city_id)
        Room_image = request.POST.get('Room_image')
        Room_number = request.POST.get('Room_number')
        Room_area = request.POST.get('Room_area')
        room_type_id = request.POST.get('room_type')
        room_type = room.objects.get(id=room_type_id)
        No_of_beds = request.POST.get('No_of_beds')

        Price = request.POST.get('Price')
        Room_description = request.POST.get('Room_description')

        s = Adding_Rooms(
            id=id,

            city=city,
            Room_image=Room_image,
            Room_number=Room_number,
            Room_area=Room_area,
            room_type=room_type,
            No_of_beds=No_of_beds,

            Price=Price,
            Room_description=Room_description,
        )
        s.save()
        return redirect('adding_rooms')
    return redirect(request, 'adding_rooms.html')

def togglestatusar(request, item_id):
    item = reservation.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('adding_rooms')
# ==============================================================================================================================
# Reservations
@login_required(login_url='login')
def reservations(request):
    rr_a = reservation.objects.all()
    city = branch_management.objects.all()

    context = {
        'rr_a': rr_a,
        'city': city,
    }
    return render(request, 'reservations.html', context)


@login_required(login_url='login')
def addreservation(request):
    ar_b = reservation.objects.all()
    room_type=room.objects.all()

    if request.method == 'POST':
        profile_name = request.POST.get('profile_name')
        contact = request.POST.get('contact')

        email_id = request.POST.get('email_id')
        city_id = request.POST.get('city')
        city = branch_management.objects.get(id=city_id)

        room_type_id = request.POST.get('room_type')
        room_type = room.objects.get(id=room_type_id)
        status = request.POST.get('status')
        number_of_guest = request.POST.get('number_of_guest')

        number_of_child = request.POST.get('number_of_child')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        created_at = request.POST.get('created_at')

        r = reservation(

            profile_name=profile_name,
            contact=contact,
            email_id=email_id,
            city=city,
            room_type=room_type,
            status=status,
            number_of_guest=number_of_guest,
            number_of_child=number_of_child,
            check_in=check_in,
            check_out=check_out,
            created_at=created_at,

        )
        r.save()
        return redirect('reservations')

    return render(request, 'reservation.html', {'ar_b': ar_b,'room_type':room_type})


@login_required(login_url='login')
def deletereservarions(request, pk):
    b = reservation.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('reservations')


def editreservarions(request, pk):
    ar_e = reservation.objects.get(id=pk)
    context = {
        'today': date.today(),
        'ar_e': ar_e
    }
    return render(request, 'reservation.html', context)


def updatereservarions(request, id):
    if request.method == 'POST':
        profile_name = request.POST.get('profile_name')
        contact = request.POST.get('contact')
        email_id = request.POST.get('email_id')
        branch = request.POST.get('branch')
        room_type = request.POST.get('room_type')
        status = request.POST.get('status')
        number_of_guest = request.POST.get('number_of_guest')
        number_of_child = request.POST.get('number_of_child')
        r = reservation(
            id=id,
            profile_name=profile_name,
            contact=contact,
            email_id=email_id,
            branch=branch,
            room_type=room_type,
            status=status,
            number_of_guest=number_of_guest,
            number_of_child=number_of_child,

        )
        r.save()
        return redirect('reservations')
    return redirect(request, 'reservation.html')


def togglestatus(request, item_id):
    item = reservation.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('mybooking')


# ==============================================================================================================================
# Admin staff
@login_required(login_url='login')
def admin_staff_view(request):
    as_a = Admin_staff.objects.all()
    department = Department.objects.all()
    designation = Designation.objects.all()
    city = branch_management.objects.all()
    today = date.today()

    context = {
        'as_a': as_a,
        'today': today,
        'department': department,
        'designation': designation,
        'city': city,
    }
    return render(request, 'admin_staff.html', context)


def addas(request):
    as_b = Admin_staff.objects.all()

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        date_of_joining = request.POST.get('date_of_joining')
        employee_age = request.POST.get('employee_age')
        gender = request.POST.get('gender')
        emp_address = request.POST.get('emp_address')
        nationality = request.POST.get('nationality')
        mobile_number = request.POST.get('mobile_number')
        alternative_mobile_number = request.POST.get('alternative_mobile_number')
        email = request.POST.get('email')
        pincode = request.POST.get('pincode')
        # Assuming 'designation' is a foreign key to Designation model
        designation_id = request.POST.get('designation')
        designation = Designation.objects.get(pk=designation_id)

        # Assuming 'department' is a foreign key to Department model
        department_id = request.POST.get('department')
        department = Department.objects.get(pk=department_id)
        city_id = request.POST.get('city')
        city = branch_management.objects.get(id=city_id)
        shift_timings = request.POST.get('shift_timings')
        type_of_emp = request.POST.get('type_of_emp')
        passport_image = request.POST.get('passport_image')
        id_prooof = request.POST.get('id_prooof')
        certificates = request.POST.get('certificates')
        signature = request.POST.get('signature')
        created_at = request.POST.get('created_at')

        r = Admin_staff(

            full_name=full_name,
            date_of_joining=date_of_joining,
            employee_age=employee_age,
            gender=gender,
            emp_address=emp_address,
            nationality=nationality,
            mobile_number=mobile_number,
            alternative_mobile_number=alternative_mobile_number,
            email=email,
            pincode=pincode,
            designation=designation,  # Assigning the Designation instance
            department=department,
            city=city,
            shift_timings=shift_timings,
            type_of_emp=type_of_emp,
            passport_image=passport_image,
            id_prooof=id_prooof,
            certificates=certificates,
            signature=signature,
            created_at=created_at,

        )
        r.save()
        return redirect('admin_staff_view')

    return render(request, 'admin_staff.html', {'as_b': as_b})


def deleteas(request, pk):
    b = Admin_staff.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('admin_staff_view')


def editas(request, pk):
    as_e = Admin_staff.objects.get(id=pk)
    city = branch_management.objects.all()
    context = {
        'today': date.today(),
        'as_e': as_e,
        'city': city,
    }
    return render(request, 'admin_staff.html', context)


def updateas(request, id):
    if request.method == 'POST':
        passport_image = request.POST.get('passport_image')

        id_prooof = request.POST.get('id_prooof')
        certificates = request.POST.get('certificates')

        signature = request.POST.get('signature')
        full_name = request.POST.get('full_name')
        date_of_joining = request.POST.get('date_of_joining')

        employee_age = request.POST.get('employee_age')
        gender = request.POST.get('gender')

        emp_address = request.POST.get('emp_address')
        nationality = request.POST.get('nationality')
        mobile_number = request.POST.get('mobile_number')

        alternative_mobile_number = request.POST.get('alternative_mobile_number')
        email = request.POST.get('email')
        pincode = request.POST.get('pincode')
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        city_id = request.POST.get(id=city)
        city = branch_management.objects.get(id=city_id)
        shift_timings = request.POST.get('shift_timings')
        type_of_emp = request.POST.get('type_of_emp')

        r = Admin_staff(
            id=id,

            passport_image=passport_image,
            id_prooof=id_prooof,
            certificates=certificates,
            signature=signature,
            full_name=full_name,
            date_of_joining=date_of_joining,
            employee_age=employee_age,
            gender=gender,
            emp_address=emp_address,
            nationality=nationality,
            mobile_number=mobile_number,
            alternative_mobile_number=alternative_mobile_number,
            email=email,
            pincode=pincode,
            department=department,
            designation=designation,
            city=city,
            shift_timings=shift_timings,
            type_of_emp=type_of_emp,

        )
        r.save()
        return redirect('admin_staff_view')
    return redirect(request, 'food_service.html')


def togglestatus12(request, item_id):
    item = Admin_staff.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('admin_staff_view')


# ==============================================================================================================================
# Food Service
@login_required(login_url='login')
def food_service(request):
    food_b = Food_Services.objects.all()

    context = {
        'food_b': food_b,

    }

    if request.method == 'POST':
        Recepie_name = request.POST.get('Recepie_name')
        Recepie_image = request.POST.get('Recepie_image')
        meal_type = request.POST.get('meal_type')

        Food_category = request.POST.get('Food_category')
        Price = request.POST.get('Price')
        Recepie_Category = request.POST.get('Recepie_Category')
        recepie_description = request.POST.get('recepie_description')

        a = Food_Services(
            Recepie_name=Recepie_name,
            meal_type=meal_type,
            Recepie_image=Recepie_image,
            Food_category=Food_category,
            Price=Price,
            Recepie_Category=Recepie_Category,
            recepie_description=recepie_description,

        )
        a.save()
        return redirect('food_service')

    return render(request, 'food_service.html', context)


def deletefood(request, pk):
    b = Food_Services.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('food_service')


def editfood(request, pk):
    food_e = Food_Services.objects.get(id=pk)
    context = {
        'food_e': food_e
    }
    return render(request, 'food_service.html', context)


def updatefood(request, id):
    if request.method == 'POST':
        Recepie_name = request.POST.get('Recepie_name')
        Recepie_image = request.POST.get('Recepie_image')
        meal_type = request.POST.get('meal_type')

        Food_category = request.POST.get('Food_category')
        Price = request.POST.get('Price')
        Recepie_Category = request.POST.get('Recepie_Category')
        recepie_description = request.POST.get('recepie_description')

        fp = Food_Services(
            id=id,
            Recepie_name=Recepie_name,
            meal_type=meal_type,
            Recepie_image=Recepie_image,
            Food_category=Food_category,
            Price=Price,
            Recepie_Category=Recepie_Category,
            recepie_description=recepie_description,
        )
        fp.save()
        return redirect('food_service')

    return redirect(request, 'food_service.html')


def togglestatusff(request, item_id):
    item = Food_Services.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('food_service')


# ==============================================================================================================================
# Security
@login_required(login_url='login')
def security(request):
    return render(request, 'security.html')


@login_required(login_url='login')
def cctv_view(request):
    cc_a = cctv.objects.all()
    city = branch_management.objects.all()

    context = {
        'cc_a': cc_a,
        'city': city
    }
    return render(request, 'cctv.html', context)


@login_required(login_url='login')
def addcctv(request):
    cc_b = cctv.objects.all()

    if request.method == 'POST':
        city_id = request.POST.get('city')
        city = branch_management.objects.get(id=city_id)
        no_cctv = request.POST.get('no_cctv')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')

        c = cctv(

            city=city,
            no_cctv=no_cctv,
            desc=desc,
            status=status,
            created_at=created_at,

        )
        c.save()
        return redirect('cctv_view')

    return render(request, 'cctv.html', {'cc_b': cc_b})


def deletecctv(request, pk):
    b = cctv.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('cctv_view')


def editcctv(request, pk):
    cc_e = cctv.objects.get(id=pk)
    city = branch_management.objects.all()

    context = {
        'cc_e': cc_e,
        'city': city
    }
    return render(request, 'cctv.html', context)


def updatecctv(request, id):
    if request.method == 'POST':
        city_id = request.POST.get('city')
        city = branch_management.objects.get(id=city_id)
        no_cctv = request.POST.get('no_cctv')
        desc = request.POST.get('desc')

        s = cctv(
            id=id,
            city=city,
            no_cctv=no_cctv,
            desc=desc,

        )
        s.save()
        return redirect('cctv_view')


def togglestatuscctv(request, item_id):
    item = cctv.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('cctv_view')


# ===========================================================================================================
# ===========================================================================================================
@login_required(login_url='login')
def fire_view(request):
    ff_a = fire.objects.all()
    city = branch_management.objects.all()

    context = {
        'ff_a': ff_a,
        'city': city
    }
    return render(request, 'fire.html', context)


@login_required(login_url='login')
def addfire(request):
    ff_b = fire.objects.all()

    if request.method == 'POST':
        city_id = request.POST.get('city')
        city = branch_management.objects.get(id=city_id)
        no_drills = request.POST.get('no_drills')
        desc_d = request.POST.get('desc_d')
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')

        c = fire(

            city=city,
            no_drills=no_drills,
            desc_d=desc_d,
            status=status,
            created_at=created_at,

        )
        c.save()
        return redirect('fire_view')

    return render(request, 'fire.html', {'ff_b': ff_b})


@login_required(login_url='login')
def deletefire(request, pk):
    b = fire.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('fire_view')


def editfire(request, pk):
    cc_e = cctv.objects.get(id=pk)
    city = branch_management.objects.all()
    context = {
        'cc_e': cc_e,
        'city': city
    }
    return render(request, 'fire.html', context)


def updatefire(request, id):
    if request.method == 'POST':
        city_id = request.POST.get('city')
        city = branch_management.objects.get(id=city_id)
        no_drills = request.POST.get('no_drills')
        desc_d = request.POST.get('desc_d')

        s = fire(
            city=city,
            no_drills=no_drills,
            desc_d=desc_d,

        )
        s.save()
        return redirect('fire_view')


def togglestatusfire(request, item_id):
    item = fire.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('fire_view')


# ===========================================================================================================
# ===========================================================================================================
# @login_required(login_url='login')
# def medical_view(request):
#     mm_a = medical.objects.all()
#     city = branch_management.objects.all()

#     context = {
#         'mm_a': mm_a,
#         'city': city
#     }
#     return render(request, 'medical.html', context)


# @login_required(login_url='login')
# def addmd(request):
#     mm_b = medical.objects.all()

#     if request.method == 'POST':
#         city_id = request.POST.get('city')
#         city = branch_management.objects.get(id=city_id)

#         desc_m = request.POST.get('desc_m')
#         status = request.POST.get('status')

#         c = medical(

#             city=city,
#             status=status,

#             desc_m=desc_m,

#         )
#         c.save()
#         return redirect('medical_view')

#     return render(request, 'medical.html', {'mm_b': mm_b})


# @login_required(login_url='login')
# def deletemd(request, pk):
#     b = medical.objects.get(id=pk)
#     b.delete()  # 1=> delete

#     return redirect('medical_view')


# def editmd(request, pk):
#     mm_e = medical.objects.get(id=pk)
#     city = branch_management.objects.all()
#     context = {
#         'mm_e': mm_e,
#         'city': city
#     }
#     return render(request, 'medical.html', context)


# def updatemd(request, id):
#     if request.method == 'POST':
#         city_id = request.POST.get('city')
#         city = branch_management.objects.get(id=city_id)

#         desc_m = request.POST.get('desc_m')

#         s = medical(
#             id=id,

#             city=city,

#             desc_m=desc_m,

#         )
#         s.save()
#         return redirect('medical_view')


# def togglestatusmed(request, item_id):
#     item = medical.objects.get(pk=item_id)
#     item.status = not item.status  # Toggle the status
#     item.save()
#     return redirect('medical_view')


# ============================================================================================================================
# settings
@login_required(login_url='login')
def settings_view(request):
    return render(request, 'settings.html')


# ============================================================================================================================
# Settings Sub modules


@login_required(login_url='login')
def amenities_views(request):
    eme_a = amenities.objects.all()

    context = {
        'eme_a': eme_a,
    }
    return render(request, 'add_amenities.html', context)


def addamenities(request):
    error_message_a = ""

    if request.method == 'POST':
        amenitie = request.POST.get('amenitie')
        image = request.POST.get('image')
        status = request.POST.get('status')
        Ame_description = request.POST.get('Ame_description')
        created_at = request.POST.get('created_at')
        if amenities.objects.filter(amenitie=amenitie).exists():
            error_message_a = "amenities Name already exists."
        if not error_message_a:

            c = amenities(
                amenitie=amenitie,
                image=image,
                status=status,
                Ame_description=Ame_description,
                created_at=created_at,

            )
            c.save()
            return redirect('amenities_views')
        else:
            A = amenities.objects.all()
            context = {
                "A": A,
                "error_message_a": error_message_a,

            }
            return redirect('amenities_views')

    A = amenities.objects.all()

    context = {
        "A": A,
        "error_message_a": error_message_a,

    }
    return render(request, 'add_amenities.html', context)


def deleteeme(request, pk):
    b = amenities.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('amenities_views')


def editeme(request, pk):
    room_e = room.objects.get(id=pk)
    context = {
        'room_e': room_e
    }
    return render(request, 'add_amenities.html', context)


def updateeme(request, id):
    if request.method == 'POST':
        amenitie = request.POST.get('amenitie')
        image = request.POST.get('image')
        Ame_description = request.POST.get('Ame_description')

        e = amenities(
            id=id,
            amenitie=amenitie,
            image=image,
            Ame_description=Ame_description,

        )
        e.save()
        return redirect('amenities_views')


def togglestatusame(request, item_id):
    item = amenities.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('amenities_views')


# ==============================================================================================================

# ================================================================================================================
# CURRENCY
@login_required(login_url='login')
def currency_view(request):
    cur_a = currency.objects.all()

    context = {
        'cur_a': cur_a,
    }
    return render(request, 'add_currency.html', context)


def addcurrency(request):
    error_message_c = ""

    if request.method == 'POST':
        Currency = request.POST.get('Currency')
        status = request.POST.get('status')
        if currency.objects.filter(Currency=Currency).exists():
            error_message_c = "currency Name already exists."
        if not error_message_c:

            c = currency(
                Currency=Currency,
                status=status

            )
            c.save()
            return redirect('currency_view')
        else:
            A = currency.objects.all()
            context = {
                "A": A,
                "error_message_c": error_message_c,

            }
            return redirect('currency_view')

    A = currency.objects.all()

    context = {
        "A": A,
        "error_message_c": error_message_c,

    }
    return render(request, 'add_currency.html', context)


def deletecur(request, pk):
    b = currency.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('currency_view')


def editcur(request, pk):
    cur_e = currency.objects.get(id=pk)
    context = {
        'cur_e': cur_e
    }
    return render(request, 'add_currency.html', context)


def updatecur(request, id):
    if request.method == 'POST':
        Currency = request.POST.get('Currency')

        e = currency(
            id=id,
            Currency=Currency,

        )
        e.save()
        return redirect('currency_view')


def togglestatuscurrency(request, item_id):
    item = currency.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('currency_view')


# ============================================================================================================
# ================================================================================================================
@login_required(login_url='login')
def elmpoyee_view(request):
    emp_a = Designation.objects.all()
    department = Department.objects.all()

    context = {
        'emp_a': emp_a,
        'department': department
    }
    return render(request, 'Designation.html', context)


def addemp(request):
    emp_b = Designation.objects.all()

    if request.method == 'POST':
        designation = request.POST.get('designation')
        department_id = request.POST.get('department')
        department = Department.objects.get(id=department_id)
        created_at = request.POST.get('created_at')
        status = request.POST.get('status')

        e = Designation(

            designation=designation,
            department=department,
            created_at=created_at,
            status=status,

        )
        e.save()
        return redirect('elmpoyee_view')

    return render(request, 'Designation.html', {'emp_b': emp_b})


def deleteemp(request, pk):
    b = Designation.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('elmpoyee_view')


def editemp(request, pk):
    ser_e = Designation.objects.get(id=pk)
    department = Department.objects.get()

    context = {
        'ser_e': ser_e,
        'department': department

    }
    return render(request, 'Designation.html', context)


def updateemp(request, id):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        department_id = request.POST.get('department')
        department = Department.objects.get(id=department_id)

        s = Designation(
            id=id,
            designation=designation,
            department=department,

        )
        s.save()
        return redirect('elmpoyee_view')


def togglestatusemp(request, item_id):
    item = Designation.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('elmpoyee_view')


# ==============================================================================================================

# ==============================================================================================================
@login_required(login_url='login')
def Department_view(request):
    emp_a = Department.objects.all()

    context = {
        'emp_a': emp_a,
    }
    return render(request, 'Department.html', context)


def adddep(request):
    emp_b = Department.objects.all()

    if request.method == 'POST':
        department = request.POST.get('department')
        created_at = request.POST.get('created_at')
        status = request.POST.get('status')

        e = Department(
            department=department,
            created_at=created_at,
            status=status,

        )
        e.save()
        return redirect('Department_view')

    return render(request, 'Department.html', {'emp_b': emp_b})


def deletedep(request, pk):
    b = Department.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('Department_view')


def editdep(request, pk):
    ser_e = Department.objects.get(id=pk)
    context = {
        'ser_e': ser_e,

    }
    return render(request, 'Department.html', context)


def updatedep(request, id):
    if request.method == 'POST':
        department = request.POST.get('department')

        s = Department(
            id=id,
            department=department,

        )
        s.save()
        return redirect('Department_view')


def togglestatusdep(request, item_id):
    item = Department.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('Department_view')


# ==============================================================================================================

# ==============================================================================================================
@login_required(login_url='login')
def hotel_view(request):
    hot_a = hotel.objects.all()

    context = {
        'hot_a': hot_a,
    }
    return render(request, 'add_hotel.html', context)


def addhot(request):
    hot_b = hotel.objects.all()

    if request.method == 'POST':
        image = request.POST.get('image')
        hotel_type = request.POST.get('hotel_type')
        availability = request.POST.get('availability')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        amenities = request.POST.get('amenities')
        policy = bool(request.POST.get('policy'))
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')

        e = hotel(

            image=image,
            hotel_type=hotel_type,
            availability=availability,
            contact=contact,
            location=location,
            amenities=amenities,
            policy=policy,
            status=status,
            created_at=created_at,
        )

        e.save()
        return redirect('hotel_view')
    return render(request, 'add_hotel.html', {'hot_b': hot_b})


def deletehot(request, pk):
    b = hotel.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('hotel_view')


def edithot(request, pk):
    hot_e = hotel.objects.get(id=pk)
    context = {
        'hot_e': hot_e
    }
    return render(request, 'add_hotel.html', context)


def updatehot(request, id):
    if request.method == 'POST':
        image = request.POST.get('image')
        hotel_type = request.POST.get('hotel_type')
        availability = request.POST.get('availability')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        amenities = request.POST.get('amenities')

        # Get the 'policy' value from the request and convert it to a boolean
        policy = request.POST.get('policy') == 'on' if 'policy' in request.POST else False

        e = hotel(
            id=id,
            image=image,
            hotel_type=hotel_type,
            availability=availability,
            contact=contact,
            location=location,
            amenities=amenities,
            policy=policy,
        )

        e.save()
        return redirect('hotel_view')


def togglestatusth(request, item_id):
    item = hotel.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('hotel_view')


# ==============================================================================================================

# ============================================================================================================
# LANGUAGE
@login_required(login_url='login')
def language_view(request):
    lan_a = language.objects.all()

    context = {
        'lan_a': lan_a,
    }
    return render(request, 'add_language.html', context)


def addlanguage(request):
    error_message_l = ""

    if request.method == 'POST':
        Language = request.POST.get('Language')
        status = request.POST.get('status')
        if language.objects.filter(Language=Language).exists():
            error_message_l = "language Name already exists."
        if not error_message_l:

            c = language(
                Language=Language,
                status=status,

            )
            c.save()
            return redirect('language_view')
        else:
            A = language.objects.all()
            context = {
                "A": A,
                "error_message_l": error_message_l,

            }
            return redirect('language_view')

    A = language.objects.all()

    context = {
        "A": A,
        "error_message_l": error_message_l,

    }
    return render(request, 'add_language.html', context)


def deletelan(request, pk):
    b = language.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('language_view')


def editlan(request, pk):
    lan_e = language.objects.get(id=pk)
    context = {
        'lan_e': lan_e
    }
    return render(request, 'add_language.html', context)


def updatelan(request, id):
    if request.method == 'POST':
        Language = request.POST.get('Language')

        e = language(
            id=id,
            Language=Language,

        )
        e.save()
        return redirect('language_view')


def togglestatuslan(request, item_id):
    item = language.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('language_view')


# =======================================================================================================
@login_required(login_url='login')
def room_view(request):
    room_a = room.objects.all()

    context = {
        'room_a': room_a,
    }
    return render(request, 'add_room.html', context)


def addroom(request):
    room_b = room.objects.all()

    error_message_x = ""
    context = {
        "room_b": room_b,

    }

    if request.method == 'POST':
        room_type = request.POST.get('room_type')
        created_at = request.POST.get('created_at')
        status = request.POST.get('status')
        if room.objects.filter(room_type=room_type).exists():
            error_message_x = "Type Is already exists."
        if not error_message_x:

            c = room(
                room_type=room_type,
                created_at=created_at,
                status=status,

            )
            c.save()
            return redirect('room_view')
        else:
            A = room.objects.all()
            context = {
                "A": A,
                "error_message_x": error_message_x,

            }
            return redirect('room_view')

    A = room.objects.all()

    context = {
        "A": A,

        "error_message_x": error_message_x,

    }
    return render(request, 'add_room.html', context)


def deleteroom(request, pk):
    b = room.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('room_view')


def editroom(request, pk):
    room_e = room.objects.get(id=pk)
    context = {
        'room_e': room_e
    }
    return render(request, 'add_room.html', context)


def updateroom(request, id):
    if request.method == 'POST':
        room_type = request.POST.get('room_type')
        no_cots = request.POST.get('no_cots')
        no_rooms = request.POST.get('no_rooms')

        p = room(
            id=id,
            room_type=room_type,
            no_cots=no_cots,
            no_rooms=no_rooms,

        )
        p.save()
        return redirect('room_view')


def togglestatusT(request, item_id):
    item = room.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('room_view')


# ===========================================================================================================
# ===========================================================================================================
@login_required(login_url='login')
def service_view(request):
    ser_a = service.objects.all()

    context = {
        'ser_a': ser_a,
    }
    return render(request, 'add_services.html', context)


def addservice(request):
    error_message_s = ""

    if request.method == 'POST':
        Service = request.POST.get('Service')
        image = request.POST.get('image')
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')
        if service.objects.filter(Service=Service).exists():
            error_message_s = "Service Name already exists."
        if not error_message_s:

            c = service(
                Service=Service,
                image=image,
                status=status,
                created_at=created_at,

            )
            c.save()
            return redirect('service_view')
        else:
            A = service.objects.all()
            context = {
                "A": A,
                "error_message_s": error_message_s,

            }
            return redirect('service_view')

    A = service.objects.all()

    context = {
        "A": A,
        "error_message_s": error_message_s,

    }
    return render(request, 'add_language.html', context)


def deleteservice(request, pk):
    b = service.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('service_view')


def editservice(request, pk):
    ser_e = service.objects.get(id=pk)
    context = {
        'ser_e': ser_e
    }
    return render(request, 'add_services.html', context)


def updateservice(request, id):
    if request.method == 'POST':
        Service = request.POST.get('Service')
        image = request.POST.get('image')
        status = request.POST.get('status')

        s = service(
            id=id,
            Service=Service,
            status=stats,
            image=image,

        )
        s.save()
        return redirect('service_view')


def togglestatusser(request, item_id):
    item = service.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('service_view')


def log_out(request):
    logout(request)
    return redirect('login')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login is successful...!')
            return redirect('dashboard')
        else:
            print('Invalid Credentials')
            messages.info(request, "Invalid Credientials")
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def manageuser_view(request):
    manageuser_b = Manageusers.objects.all()

    context = {
        'manageuser_b': manageuser_b
    }
    return render(request, 'Manage_User.html', context)


def addmanageuser(request):
    manageuser_a = Manageusers.objects.all()

    if request.method == 'POST':
        id_proof = request.POST.get('id_proof')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        Age = request.POST.get('Age')
        Gender = request.POST.get('Gender')
        status = request.POST.get('status')
        a = Manageusers(
            full_name=full_name,
            phone_number=phone_number,
            id_proof=id_proof,
            Age=Age,
            Gender=Gender,
            status=status,

        )
        a.save()
        return redirect('manageuser')

    return render(request, 'Manage_User.html', {'manageuser_a': manageuser_a})


def deleteuser(request, pk):
    b = Manageusers.objects.get(id=pk)
    b.delete()  # 1=> delete

    return redirect('manageuser')


def edit_MU(request, pk):
    AR_e = Manageusers.objects.get(id=pk)
    context = {
        'AR_e': AR_e
    }
    return render(request, 'Manage_User.html', context)


def updateuser(request, id):
    if request.method == 'POST':
        id_proof = request.POST.get('id_proof')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        Age = request.POST.get('Age')
        Gender = request.POST.get('Gender')

        up = Manageusers(
            id=id,
            full_name=full_name,
            phone_number=phone_number,
            id_proof=id_proof,
            Age=Age,
            Gender=Gender,

        )
        up.save()

        return redirect('manageuser')


def togglestatus1(request, item_id):
    item = Manageusers.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('manageuser')