from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from . import models
from . import serializers


@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def showBill(request):
    
    try :
        user = User.objects.get(id=request.session['_auth_user_id']).username
        print (user)
    except:
        return Response({
            "status":False
        })
    
    try :   
        bill = models.Bill.objects.all().order_by('-id')
        billData = serializers.billSerializers(bill, many=True).data
        
        expenses = 0
        income = 0
        
        for item in models.Bill.objects.all().order_by('-date'):
            if item.type == 1:
                income += item.amount
            else :
                expenses += item.amount
            
        status = True
    except :
        status = False
        
    return Response(
        {
            "status":status,
            "data":billData,
            "amount":{
                "income":income,
                "expenses":expenses,
                "balance":income-expenses,
            }
            
        }
    )


@csrf_exempt
@api_view(["POST",])
@permission_classes((AllowAny,))
def userLogin(request):

    username = request.data['username']
    password = request.data['password']

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:
        if user.is_active:
            status = True
            msg = 'user is logined'
            login(request, user)
        else:
            status = False
            msg = 'Currently, This user is not active'
    else:
        status = False
        msg = 'Error wrong username/password'

    return Response({'status': status, 'message': msg})


@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def createBill(request):
    try :
        user = User.objects.get(id=request.session['_auth_user_id']).username
        print (user)
    except:
        return Response({
            "status":False
        })
    try :
        name = request.data['name']
        amount = request.data['amount']
        type = request.data['type']
        remark = request.data['remark']
        
        if type == 2:
            amount = amount*-1

        models.Bill.objects.create(
            name=name,
            amount=amount,
            type=type,
            remark=remark,
            user=user
        )
        
        
        
        status = True
        # models.Bill.
    except :
        status = False
        
    return Response(
        {
            "status":status,
            # "data":billData
        }
    )
    
    
    
    
def indexPage(req):
    
    return render(req, 'index.html')