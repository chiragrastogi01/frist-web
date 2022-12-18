
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request, "index.html")

# def result(request):
#     # name=request.GET['user_name']
#     # email=request.GET['user_email']
#     # message=f"Hi {name} , your email is {email}"
#     num1=request.GET['user_num1']
#     num2=request.GET['user_num2']
#     num3 = request.GET['user_num3']
#     # result=int(num1)+int(num2)
#     if num3=='*':
#         result=int(num1)*int(num2)
#     elif num3=='+':
#         result=int(num1)+int(num2)
#     elif num3=='-':
#         result=int(num1)-int(num2)
#     elif num3=='/':
#         result=int(num1)/int(num2)
#     else:
#         print("chose ! ")
#     return render(request,"result.html",{'result': result})

def result(request):
    # name=request.GET['user_name']
    # email=request.GET['user_email']
    # message=f"Hi {name} , your email is {email}"
    num1=request.GET['value_num1']
    # result=int(num1)+int(num2)
    if num3=='*':
        result=int(num1)*int(num2)
    elif num3=='+':
        result=int(num1)+int(num2)
    elif num3=='-':
        result=int(num1)-int(num2)
    elif num3=='/':
        result=int(num1)/int(num2)
    else:
        print("chose ! ")
    return render(request,"result.html",{'result': result})


def classroom(request):
    return render(request,"classroom.html")