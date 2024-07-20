from django.shortcuts import render
from django.shortcuts import render,redirect
from adminapk.views import Adding_Rooms,amenities_views,amenities,service,room,branch_management,reservation,Manageusers
from django.contrib import messages
import random, uuid, json
import requests
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from adminapk.views import Adding_Rooms,amenities_views,amenities,service
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.shortcuts import render
  # Import your Room model
from django.db.models import Q
# Create your views here.


def send_otp(phone_number, otp):
    api_key = '3f8fb95c-a3d8-11ee-8cbb-0200cd936042'
    url = f'https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/{otp}'

    response = requests.post(url)
    if response.status_code == 200:
        response_data = response.json()
        if response_data['Status'] == 'Success':
            session_id = response_data['Details']
            return session_id
        return None

def user_signin(req):

    if req.method == 'GET':
        return render(req,'user_login.html')
    else:
        user_name = req.POST.get('username')
        user_password = req.POST.get('password')
        print('user_name',user_name,':','user_password',user_password)
        try:
            # Use objects.get() to retrieve a student by student_user_name
            user = User_Signup.objects.get(user_name=user_name)

            if user.user_password == user_password:
                req.session['user'] = user.id
                print(req.session['user'])
                return redirect('home_view')
            else:
                error_message = 'Username or Password invalid !!'
                print('Username or Password invalid !!!')
        except User_Signup.DoesNotExist:
            error_message = 'Username or Password invalid !!'
            print('Username or Password invalid !!!')

    return render(req, 'home.html', {'error': error_message})


def validateuser(customer_user):
    error_message = None
    if customer_user.isExistsemail():
        error_message = 'Phone Number Already Registered..'
    elif customer_user.isExistsphone():
        error_message = 'Phone Number Already Registered..'
    # saving

    return error_message

def user_signup(request):

    if request.method == 'POST':
        postData = request.POST
        user_full_name = postData.get('fullName')  # Retrieve the full name here
        user_name = postData.get('username')
        user_mobile_number = postData.get('phoneNumber')
        user_email = postData.get('email')
        user_password = postData.get('password')
        user_confirm_password = postData.get('confirmPassword')
        print(user_full_name)


        # validation
        value = {
            'user_name': user_name,
            'user_mobile_number': user_mobile_number,
            'user_email': user_email,

        }
        error_message = None
        if user_password == user_confirm_password:
            error_message = "Password and Confirm Password Must be Same"
        otp = random.randint(111111, 999999)
        user = User_Signup(
                        user_full_name = user_full_name,
                        user_name=user_name,
                        user_mobile_number=user_mobile_number,
                        user_email=user_email,
                        user_password=user_password,
                        user_otp=otp,
                        )
        error_message = validateuser(user)
        print(error_message)
        if not error_message:

            user.save()
            send_otp(user.user_mobile_number, user.user_otp)
            form_url = reverse('user_otp', args=[user.id])
            return redirect(form_url)
        else:
            data = {
                'error': error_message,
                'values': value
            }
        return render(request, 'user_reg.html',data)
    else:
        return render(request, 'user_reg.html')

def user_otp_verification(request,pk):
    otp_user = User_Signup.objects.get(id=pk)
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        if int(user_otp) == int(otp_user.user_otp):
            return redirect('user_login')
        else:
            return redirect('/')

    last_three_numbers = otp_user.user_mobile_number[-3:]

    print(last_three_numbers)

    context = {
        'otp_user': otp_user,
        'last_three_numbers':last_three_numbers,
    }
    return render(request, 'user_otp_verification.html', context)

def user_signout(req):
    req.session.clear()
    return redirect('user_login')


# Create your views here.
def home_view(request):
    eme_a = amenities.objects.all()
    ser_a = service.objects.all()
    ad_a = Adding_Rooms.objects.all()
    city = branch_management.objects.all()
    room_type = room.objects.all()
    user_full_name=User_Signup.objects.all()


    context = {
        'eme_a': eme_a,
        'ser_a': ser_a,
        'ad_a': ad_a,
        'city':city,
        'room_type':room_type,
        'user_full_name':user_full_name,
    }

    return render(request,'home.html',context)
#
#===================================================================================

def about_view(request):
    eme_a = amenities.objects.all()
    ad_a = Adding_Rooms.objects.all()
    room_type = room.objects.all()
    user_full_name = User_Signup.objects.all()



    context = {
        'eme_a': eme_a,
        'ad_a':ad_a,
        'room_type':room_type,
        'user_full_name': user_full_name,

    }
    return render(request,'about.html',context)

#===================================================================================

def blog_view(request):
    ad_a = Adding_Rooms.objects.all()
    room_type = room.objects.all()
    user_full_name = User_Signup.objects.all()
    context = {

        'ad_a': ad_a,
        'room_type':room_type,
        'user_full_name': user_full_name,

    }
    return render(request,'blogs.html',context)

#===================================================================================

def restarunts_view(request):
    eme_a = amenities.objects.all()
    ad_a = Adding_Rooms.objects.all()
    room_type = room.objects.all()
    user_full_name = User_Signup.objects.all()


    context = {
        'eme_a': eme_a,
        'ad_a':ad_a,
        'room_type':room_type,
        'user_full_name': user_full_name,

    }

    return render(request,'restarunts.html',context)

#===================================================================================

def rooms_view(request):
    ad_a = Adding_Rooms.objects.all()
    city = branch_management.objects.all()
    room_type = room.objects.all()
    user_full_name = User_Signup.objects.all()
    context = {

        'ad_a': ad_a,
        'city':city,
        'room_type':room_type,
        'user_full_name': user_full_name,
    }
    if request.method == 'POST':
        city_id = request.POST.get('city')
        room_type_id = request.POST.get('room_type')

        # Check if both city and room type are selected
        if city_id and room_type_id:
            try:
                # Retrieve the selected city and room type
                selected_city = get_object_or_404(city, pk=city_id)
                selected_room_type = get_object_or_404(room_type, pk=room_type_id)

                # Filter rooms based on selected location and room type
                filtered_rooms = Adding_Rooms.objects.filter(city=selected_city, room_type=selected_room_type)

                # Pass the filtered rooms to the template
                return render(request, 'rooms.html', {'filtered_rooms': filtered_rooms})
            except (city.DoesNotExist, room_type.DoesNotExist):
                # Handle the case where the selected city or room type does not exist
                return render(request, 'rooms.html', {'filtered_rooms': []})
        else:
            # Handle the case where either city or room type is not selected
            return render(request, 'rooms.html', {'filtered_rooms': []})

        # Handle the case when the form is not submitted
    return render(request, 'rooms.html',context)  # Replace 'rooms.html' with your original form template





#===================================================================================

def contact_view(request):
    ad_a = Adding_Rooms.objects.all()
    room_type = room.objects.all()
    user_full_name = User_Signup.objects.all()
    context = {

        'ad_a': ad_a,
        'room_type':room_type,
        'user_full_name':user_full_name,
    }
    return render(request, 'contact.html', context)

#===================================================================================

#===================================================================================

def my_account_view(request):
    ad_a = Adding_Rooms.objects.all()
    room_type = room.objects.all()
    user_full_name = User_Signup.objects.all()

    context = {

        'ad_a': ad_a,
        'room_type':room_type,
        'user_full_name': user_full_name,
    }
    return render(request,'my_accounts.html',context)

#===================================================================================
#===================================================================================

def user_login(request):
    return render(request,'user_login.html')
#===================================================================================
#===================================================================================

def user_reg(request):
    return render(request,'user_reg.html')

def book_view(request,pk):


    eachroom = Adding_Rooms.objects.get(id=pk)

    context = {

        'eachroom': eachroom,

    }
    return render(request,'book.html',context)


def addreservation(request):
    ar_b = reservation.objects.all()
    room_type = room.objects.all()

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
        for each_reservation in reservation.objects.all().filter(check_in=check_in,check_out=check_out):
            if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(
                    request.POST['check_out']):
                pass
            elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(
                    each_reservation.check_out) > str(request.POST['check_out']):
                pass
            else:
                messages.warning(request, "Sorry This Room is unavailable for Booking")
                return redirect("rooms_view")


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
        return redirect('rooms_view')

    return render(request, 'room_view.html', {'ar_b': ar_b,'room_type':room_type})

#===================================================================================

def room_view1(request,pk):
    eachroom = Adding_Rooms.objects.get(id=pk)
    eme_a = amenities.objects.all()
    ad_a = Adding_Rooms.objects.all()
    city = branch_management.objects.all()
    room_type = room.objects.all()
    user_full_name = User_Signup.objects.all()

    context = {

        'eachroom': eachroom,
        'eme_a':eme_a,
        'ad_a':ad_a,
        'city':city,
        'room_type':room_type,
        'user_full_name':user_full_name,

    }
    return render(request,'room_view.html',context)

#===================================================================================


def my_view(request):
    context = {'user': request.user}
    return render(request, 'home.html', context)

def terms(request):
    return render(request,'terms.html')
def mybooking(request):
    rr_a = reservation.objects.all()
    ad_a = Adding_Rooms.objects.all()


    context = {
        'rr_a': rr_a,
        'ad_a':ad_a,

    }
    return render(request,'my_bookings.html',context)

def togglestatus(request, item_id):
    item = reservation.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('mybooking')

# def addmanage(request):
#     if request.method == 'POST':
#         user_full_name = request.POST.get('user_full_name')
#         user_mobile_number = request.POST.get('user_mobile_number')
#
#         user_adhaar_pdf = request.POST.get('user_adhaar_pdf')
#         user_age = request.POST.get('user_age')
#         user_gender =  request.POST.get('user_gender')
#
#
#
#     d = Manageusers(
#
#         user_full_name= user_full_name,
#         user_mobile_number= user_mobile_number,
#         user_adhaar_pdf= user_adhaar_pdf,
#         cuser_genderity= user_gender,
#         user_age= user_age,
#
#
#         )
#     d.save()
#     return redirect('rooms_view')
#
#     return render(request, 'home.html' )