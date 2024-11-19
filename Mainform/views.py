from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse



def main_view(request):   
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    user_email = request.session.get('user_email')
    
   
    return render(request, 'main.html',{
        'user_id': user_id,
        'user_name': user_name,
        'user_email': user_email
    })


def Disconnect(request):

    return redirect('login')

    



    
def Create_Task(request):
    if request.method=='GET':
        user_id = request.session.get('user_id')
        user_name = request.session.get('user_name')
        user_email = request.session.get('user_email')
        
        return render(request,'Send_task.html',{
        'user_id': user_id,
        'user_name': user_name,
        'user_email': user_email
    })


    if request.method == 'POST':
       
        email_to_send = request.POST['emailtoSend']
        description = request.POST['Description']

    token = request.session.get('token')
    if not token:
        return JsonResponse({"error": "Invalid Token."}, status=401)
    
    Headers = {
            'x-access-token': token
    }
        
    task_data = {
            'description': description,
            'email': email_to_send
        }


    response = requests.post('https://seal-app-9z3i8.ondigitalocean.app/Tasks/', headers=Headers, json=task_data)

    if response.status_code == 200:
        response_data = response.json()
        return redirect('Create_Task')
    
    elif response.status_code == 401:
        return JsonResponse({"error": "Token error1"}, status=401)
    elif response.status_code == 403:
        return JsonResponse({"error": "Token error2"}, status=403)
    else:
        return JsonResponse({"error": "Token error3"}, status=response.status_code)
    
    


def Task_Assigned(request):
    if request.method=='GET':
        
        token = request.session.get('token')
        Headers = {
            'x-access-token': token
        }
        response=requests.get('https://seal-app-9z3i8.ondigitalocean.app/Tasks/assignedto/',headers=Headers)
       
        if response.status_code == 200:
            
            tasks = response.json().get('task', [])  
            print(tasks)
        else:
            tasks = []
        return render(request,'Assigned_Task.html',{'tasks':tasks})

    


    

def task_sent(request):
     if request.method=='GET':
        
        token = request.session.get('token')

        Headers = {
            'x-access-token': token
        }
        response=requests.get('https://seal-app-9z3i8.ondigitalocean.app/Tasks/createdby/',headers=Headers)
       
        if response.status_code == 200:
            
            tasks = response.json().get('task', [])  
            print(tasks)
        else:
            tasks = []
        return render(request,'Assigned_Task.html',{'tasks':tasks})
           
 

def task_updated(request, taskUid): 
    

    if request.method=='POST':
        token = request.session.get('token')
        Headers = {
            'x-access-token': token
        }
       
        responsed=requests.patch(f'https://seal-app-9z3i8.ondigitalocean.app/Tasks/{taskUid}',headers=Headers)
       

        if responsed.status_code == 200:
            return redirect('task_assigned') 
        else:
            return JsonResponse({"error": "failed task LLLL"}, status=responsed.status_code)
        
   
   

def task_deleted(request, taskUid):
   
 
    if request.method=='POST':
        token = request.session.get('token')
        Headers = {
            'x-access-token': token
        }
        response=requests.delete(f'https://seal-app-9z3i8.ondigitalocean.app/v1/Tasks/{taskUid}',headers=Headers,)
        if response.status_code == 200:
            return redirect('task_assigned') 
        else:
            return JsonResponse({"error": "failed"}, status=response.status_code)