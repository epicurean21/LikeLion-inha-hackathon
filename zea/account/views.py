from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import ProfileMer, ProfileStu

# Create your views here.
# 회원 가입
# 소상공인
def signup01(request):
    if request.user.is_authenticated :
        return redirect('/')
    elif request.method == 'POST':
        if request.POST['password01'] == request.POST['confirm01']:
            try:
                user = User.objects.get(username = request.POST['username01'])
                return render(request, 'signup01.html', {'error' : 'username has already been used'})
            except User.DoesNotExist:
                # user 객체를 새로 생성
                #user = User.objects.create_user(username=request.POST['username01'], password=request.POST['password01'])
                user = User.objects.create_user(
                    request.POST['username01'], password=request.POST['password01']
                    )
                fullname01 = request.POST['fullname01']
                email = request.POST['email01']
                num1 = request.POST['num1']
                num2 = request.POST['num2']
                num3 = request.POST['num3']
                #photo = request.FILES['photo']
                profile = ProfileMer(user=user, fullname=fullname, email = email, num1 = num1, num2 = num2, num3 = num3)
                profile.save()
                # 로그인 한다
                auth.login(request, user)
                return redirect('/')
    return render(request, 'signup01.html')

def signup00(request):
    return render(request, 'signup00.html')

# 대학생 회원가입
def signup02(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.user.is_authenticated :
        return redirect('/')
    elif request.method == 'POST':
        if request.POST['password02'] == request.POST['confirm02']:
            try:
                user = User.objects.get(username = request.POST['username02'])
                return render(reuqest, 'signup02.html', {'error' : 'username has already been used'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username02'], password=request.POST['password02']
                    )
                fullname02 = request.POST['fullname02']
                school = request.POST['school']
                email = request.POST['email']
                department = request.POST['department']
                grade = request.POST['grade']
                bank2 = request.POST['bank2']
                bank = request.POST['bank']
                subject = request.POST.getlist('subject')
                profile = ProfileStu(user = user, fullname = fullname, email = email, school = school, grade = grade, department=department,bank2=bank2,bank=bank,subject=subject)
                profile.save()
                auth.login(request, user)
                return redirect('/')
    return render(request, 'signup02.html')


# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'login.html')