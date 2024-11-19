from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse


def get_login(request):
    if request.method == 'POST':
        Email=request.POST['email1']
        Password=request.POST['password']
   

   
        data={
            'email': Email,
            'password': Password
        }
       
        response=requests.post(url='http://localhost:5000/v0/users/login',json=data)
        if response.status_code==200:
         
            login_data=response.json()
            print(login_data)

            #TROUVER LERREUR
            request.session['user_email'] = login_data['logged_user'].get('email')
            request.session['user_id'] = login_data['logged_user'].get('id')
            request.session['user_name'] = login_data['logged_user'].get('name')
            request.session['token'] = login_data['token']
            return redirect('main')
        
        elif response.status_code==400:
            myError = "Invalide credentiel"
        elif response.status_code==500:
            myError = "Invalide credentiel"

    if request.method=='GET':
        return render(request,'login.html')
     
      

def get_user_data(request):
    token=request.session.get('token')

    header={
        'x-access-token':token
    }
    if  response.status_code == 200:
        response=requests.get("http://127.0.0.1:5000/v0/users/all",headers=header)
        user_data = response.json().get("user",[])
        return JsonResponse(user_data)
    else:
        myError = "Invalide Token"
        return render(request, 'CreateAccount.html', {'error': myError})
    
    

def CreateAccount(request):
    if request.method =='POST':
        Username=request.POST['username']
        Email=request.POST['email']
        Password=request.POST['password']

        data={
            'name':Username,
            'email':Email,
            'password':Password}
        
        response=requests.post(url='http://localhost:5000/v0/users/signup',json=data)
        return redirect('login')
    
    if request.method=='GET':
        return render(request,'CreateAccount.html')
