from django.shortcuts import render, redirect
from .models import Project_topic, Project_issue, Feedback_history
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import feedback_historyForm
from django.http import HttpResponse
import requests
from django.contrib import messages

# import psycopg2

# Create your views here.

# @csrf_exempt
# def Emp_login(request):
#     if request.method == 'POST':
#         if request.session.get('email'):
#             print('aaaaaaaaaaaaaaaa',request.session.get('email'))

#             return JsonResponse({"Login":'You already login'}) 
#         else:
#             # try:
#                 email = request.POST.get('email')
#                 password = request.POST.get('password')
#                 user = User.objects.get(email=email) # | Employee.objects.get(email=email)
#                 print('========user=======',user)
#                 checkpassword=check_password(password,user.password)
#                 print('3333333333333',checkpassword)

#                 if checkpassword == True:
#                     session = request.session['email'] = user.email
                
#                     return JsonResponse({'session ' : session ,'Login ' : ' login succesfully'}) 
#                 else:
#                     return JsonResponse({'user':'Enter valid email-password'})


    

def login(request):
    
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        url = "https://dwr.dataio.fun/api/v1/user/login"

        data = {
            "email":email,
            "password": password,  
        } 

        # headers = {"Content-Type": "application/json",'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjM3LCJuYW1lIjoiRGluZXNoIHByYWphcGF0aSIsImlhdCI6MTcxMDQyMjQ5OCwiZXhwIjoxNzExMDI3Mjk4fQ.pz-zammJDPgI9zP609dKfWU6FUyTYMXgN-i6q7eREOE'}  
        
        headers = {"Content-Type": "application/json"} #or
        response = requests.post(url, json=data, headers=headers)
        data = response.json()

        try :
            if data['code'] == 200 :

                session = request.session['email'] = email
                print('==============session==============',session)
                return redirect('feedback')
        
        except :
            messages.info(request, "Invalid Credential")

            return redirect('login')
        
    else:
        
        return render(request, "login.html")
    

def user_logout(request):
 
    print('=====logout=====')
    try:
        del request.session['email']
        print('====after=log=11====')
        return HttpResponse('<h1>User logout</h1>')
    
    except:
        print('======22==============')
        return HttpResponse('<h1>User logout2</h1>')     

       
    

def add_project(request):
    
    if request.method == "POST" :

        topic = request.POST['topic'] 
        Project_topic.objects.create(topic=topic) 

        return HttpResponse("Project add successfully")  

    else:  
        
        if request.session.get('email'):
            
            return render(request, "addproject.html") 
        else:
            return redirect('login')
        

     

# def feedback(request):
#     if request.method == 'POST':
#         form = feedback_historyForm(request.POST, request.FILES)
#         if form.is_valid():
#             # project_topic = form.cleaned_data['project_topic']
#             # print('=========project_topic==============',project_topic)

#             form.save()
#             return HttpResponse('Feedback saved')
#             # return redirect('upload_success')
#     else:
#         form = feedback_historyForm()
#     return render(request, 'feedback2.html', {'form': form})    




# @login_required(login_url="login")
def feedback(request):
    topics = Project_topic.objects.all()
    issues = Project_issue.objects.all()
    
    if request.method == 'POST' and request.FILES['attached_file']:

        project_topic = request.POST.get("project_topic")
        
        # project_issue = request.POST["project_issue"]
        project_issue = request.POST.get("roject_issue")
        print('==========project_issue==========',project_issue)
        reporting_manager = request.POST.get("reporting_manager")
        discussed_with_rm = request.POST.get("discussed_with_rm")
        message = request.POST.get("message")
        attached_file = request.FILES['attached_file']

        topic = Project_topic.objects.get(id=project_topic)
        issue = Project_issue.objects.get(id=project_issue)
        
        user = Feedback_history.objects.create(
            project_topic = topic,
            project_issue = issue,
            reporting_manager = reporting_manager,
            discussed_with_rm = discussed_with_rm,
            message = message,
            attached_file = attached_file
        )

        return redirect('feedback_history')
        
    else:

        if request.session.get('email') : 
            return render(request, "feedback.html", {'topics': topics, 'issues': issues})   

        else :
            return redirect('login')




def feedback_history(request) :

    if request.method == 'GET' :

        history_data = Feedback_history.objects.all() 

        if request.session.get('email') :   
            return render(request, "feedback_history.html", {'history_data': history_data})   

        else :
            return redirect('login')



#----API Postman--------------------------------

@csrf_exempt
def dwr_feedback(request):

    if request.method == 'POST' or request.FILES.get('file'):
        print('=======working========') 

        project_topic = request.POST['project_topic']
        project_issue = request.POST['project_issue']
        reporting_manager = request.POST['reporting_manager']
        discussed_with_rm = request.POST['discussed_with_rm']
        message = request.POST['message']
        attached_file = request.FILES['attached_file']
      
        topic = Project_topic.objects.get(id=project_topic)
        issue = Project_issue.objects.get(id=project_issue)
        
        Feedback_history.objects.create(project_topic = topic,
                                        project_issue = issue,
                                        reporting_manager = reporting_manager,
                                        discussed_with_rm = discussed_with_rm,
                                        message = message,
                                        attached_file = attached_file

        )

        return JsonResponse({'status':200,'Feedback':'Feedback submited'},status = 200)


@csrf_exempt
def dwr_feedback_history(request) :
    if request.method == 'GET' :

        history = Feedback_history.objects.all()

        history_list = []
        
        for data in history :
            
            file = data.attached_file
            history_dict = {
                'id' : data.id,
                'project topic' : data.project_topic.topic,
                'project issue' : data.project_issue.issue_type,
                'reporting manager' : data.reporting_manager,
                'dicussed with rm' : data.discussed_with_rm,
                'message' : data.message,
                'attached file' : str(file)
            }

            history_list.append(history_dict)                             
                                                                                    
        return JsonResponse({'status':200,'history_list':history_list},status = 200)                                                                
            


# def feedback(request):  

    # if request.method == "POST":  
    #     data = request.POST
    #     print('============data=============',data)
    #     # fm = feedback_historyForm(request.POST, request.FILES)  
    #     fm = feedback_historyForm(request.POST, request.FILES)

    #     if fm.is_valid():
    #         print('==========working===')
    #         fm.save()

            # print('==============working======')
            # project_topic = fm.cleaned_data['project_topic']
            # print('=========project_topic==============',project_topic)
            # project_issue = fm.cleaned_data['project_issue']
            # reporting_manager = fm.cleaned_data['reporting_manager']
            # discussed_with_rm = fm.cleaned_data['discussed_with_rm']
            # message = fm.cleaned_data['message']
            # attached_file = fm.cleaned_data['attached_file']
            # print('============project_topic=============',project_topic)
            # print('==================attache=====',attached_file)

            # 'project_topic','project_issue','reporting_manager','discussed_with_rm','message','attached_file'
            # feedback_history.objects.create(project_topic = project_topic, project_issue = project_issue, reporting_manager =reporting_manager, discussed_with_rm = discussed_with_rm, message = message, attached_file = attached_file )
            
            # return redirect("show_book")
 
    # else:  
    #     fm = feedback_historyForm()  
    
    # return render(request,'feedback2.html',{'fm':fm})    
    






# @csrf_exempt
# def feedback(request):

#     if request.method == 'POST' or request.FILES.get('file'):
#         print('=======working========') 

#         id = request.POST['id']
#         project = request.POST['project']
#         issue_type = request.POST['issue_type']
#         reporting_manager = request.POST['reporting_manager']
#         discussed_with_rm = request.POST['discussed_with_rm']
#         input_box = request.POST['input_box']
#         # attached_file = request.POST['attached_/file']
#         # attached_file = request.POST.get('attached_file')
#         attached_file = request.FILES['attached_file']

#         print('=========attached_file============',attached_file)

#         # MEDIA_ROOT = os.path.join(BASE_DIR,"media")
#         # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#         file_path = os.path.join(settings.MEDIA_ROOT, str(attached_file))
#         # file_path = "/Desktop/dwr_feedback/attached_file" 

#         print('============file_path============',file_path)
#         cursor = connection.cursor()
#         cursor.execute("""INSERT INTO public."feedback" (id,project, issue_type, reporting_manager, discussed_with_rm, input_box, attached_file)
#                                     SELECT %s, %s, %s, %s, %s, %s, %s""", (id,project, issue_type, reporting_manager, discussed_with_rm, input_box, file_path))
        

#         # cursor.execute("""SELECT id, "projectCode", "projectName" FROM public.project;""")
#         # project_code = cursor.fetchall()

#         return JsonResponse({'status':200,'Feedback':'Feedback submited'},status = 200)





# def feedback(request):

#     if request.method == "POST":
#         print('============working=======')
        # project_topic = request.POST["project_topic"]
       
        # # project_issue = request.POST["project_issue"]
        # project_issue = request.POST.get("roject_issue")
        # print('==========project_topic==========',project_topic)
        # print('==========project_issue==========',project_issue)
        # reporting_manager = request.POST["reporting_manager"]
        # discussed_with_rm = request.POST["discussed_with_rm"]
        # message = request.POST["message"]
        # attached_file = request.POST["attached_file"]
#         # print('==========project_topic==========',project_topic)
#         # print('==========project_issue==========',project_issue)
                
#         user = Feedback_history.objects.create(
#             project_topic=project_topic,
#             project_issue=project_issue,
#             reporting_manager=reporting_manager,
#             discussed_with_rm=discussed_with_rm,
#             message=message,
#             attached_file=attached_file
#         )

#         # data = Project_topic.objects.all()
#         # print('===========data======',data)
    
#     else : 
#         data = Project_topic.objects.values('topic')
#         isssue = Project_issue.objects.values('issue_type')
#         print('===========isssue======',isssue)      
        
#         context = {
#         'data': data,
#         'isssue': isssue,
#                 }
#         return render(request, "feedback3.html",{"data":data})
    

  