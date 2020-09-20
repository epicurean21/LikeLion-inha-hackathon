from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import MerchandiserApply

# Create your views here.
def merchandiserApply(request):
    return render(request, 'merchandiserApply.html')

def merchandiserApplyTry(request):
    if not request.user.is_authenticated: #로그인 되어있지 않다면 로그인 화면으로
        # 원래는 로그인 회원이 소상공인인지도 확인해야함....
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        applyContent = request.POST.get('applyContent')
        location = request.POST.get('location')
        price = request.POST.get('price')
        date = request.POST.get('date')
        profile = MerchandiserApply(name = name, email = email, contact = contact, applyContent = applyContent,
            price = price, date = date, location = location)
        profile.save()
        messages.add_message(request, messages.INFO, '신청이 완료되었습니다.')
    return render(request, 'main.html')

def studentApply(request):
    return render(request, 'studentApply.html')

def studentApplyTry(request):
    if not request.user.is_authenticated:
        # 원래는 대학생인지도 확인을 해야함
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')
        department = request.POST.get('department')
        grade = request.POST.get('grade')
        subject = request.POST.getlist('subject')
        applyContent = request.POST.get('applyContent')
        profile = StudentApply(name = name, email = email, contact = contact, applyContent = applyContent, school=school, grade=grade,subject=subject, department=department)