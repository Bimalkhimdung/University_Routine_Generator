from email import message
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib import messages
from matplotlib.style import context
from routine.packages.pdf_code import pdf_code
from .forms import Computer1ModelForm,Computer2ModelForm,Computer3ModelForm,Computer4ModelForm,Electrical1ModelForm, Electrical2ModelForm, Electrical3ModelForm, Electrical4ModelForm,LabroomModelForm
from .packages.run import call
from .packages.teacher_code import LecturerCode
from routine.packages.teacher_pdf_gen import make_teach_pdf
import pickle
import sys
from .forms import CustomerRegistrationForm
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'routine/dashboard.html')

@login_required(login_url='/login/')
def generate_routine(request):
    print(sys.argv)
    call()  
    print(sys.argv)  
    with open(r'D:\NCE_Project\output.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename = output.pdf'
        return response

@login_required(login_url='/login/')    
def view_routine(request):
    return render(request, 'routine/routine_output.html')


@login_required(login_url='/login/')
def generate_teacher_routine(request):
    with open('file8.txt','rb') as f:
        allTeacherMatrix=pickle.load(f)
    make_teach_pdf(allTeacherMatrix)
    
    with open(r'D:\NCE_Project\output_teacher', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename = output_teacher'
        return response

def view_routine_computerFirst(request):
    with open(r'D:\NCE_Project\output5_fun.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'filename = output5_fun.pdf'
            return response

def view_routine_computerSecond(request):
    with open(r'D:\NCE_Project\output2_fun.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'filename = output4_fun.pdf'
            return response

def view_routine_computerThird(request):
    with open(r'D:\NCE_Project\output4_fun.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'filename = output3_fun.pdf'
            return response

def view_routine_computerFourth(request):
    with open(r'D:\NCE_Project\output3_fun.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'filename = output2_fun.pdf'
            return response


@login_required(login_url='/login/')
def computerBatch(request):
    return render(request, 'routine/year_computer.html')


def aboutus(request):
    return render(request, 'routine/aboutus.html')

def computerData_first(request):
    if request.method == "POST":
        form = Computer1ModelForm(request.POST)

        period = int(form['Lecturer_Period'].value())
        print('Period Type',type(period))
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(377)  
        if lab_lst != []:   
            print(period)       
            period = period + max(lab_lst)
 
        if period <= 42:
            if form.is_valid():
            
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
            else:
             
                messages.error(request, 'Please enter the valid data.')
        else:
           
            messages.error(request, 'You cant add more lecturer.')
# return redirect('/')
    return render(request, 'routine/computer_first.html')


def computerData_second(request):
    if request.method == "POST":
        form = Computer2ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(376)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')
# return redirect('/')
    return render(request, 'routine/computer_second.html')

def computerData_third(request):
    if request.method == "POST":
        form = Computer3ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(375)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')
    return render(request, 'routine/computer_third.html')

def computerData_fourth(request):
    if request.method == "POST":
        form = Computer4ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(374)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')
    return render(request, 'routine/computer_fourth.html')


def electricalData_first(request):
    if request.method == "POST":
        form = Electrical1ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(277)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')

    return render(request, 'routine/electrical_first.html')

def electricalData_second(request):
    if request.method == "POST":
        form = Electrical2ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(276)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')

    return render(request, 'routine/electrical_second.html')

def electricalData_third(request):
    if request.method == "POST":
        form = Electrical3ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(275)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')

    return render(request, 'routine/electrical_third.html')

def electricalData_fourth(request):
    if request.method == "POST":
        form = Electrical4ModelForm(request.POST)
        period = int(form['Lecturer_Period'].value())
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(274)
        if lab_lst != []:          
            period = period + max(lab_lst)
        if period <= 42:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data has been entered into the database.')
        else:
            messages.error(request, 'You cant add more lecturer.')

    return render(request, 'routine/electrical_fourth.html')

# authentication part
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'routine/registration.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation !! Registered Succesfully')
            form.save()
        return render(request, 'routine/registration.html', {'form':form}) 