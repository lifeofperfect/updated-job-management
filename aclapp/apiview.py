from django.shortcuts import render
from .models import Acldb
import datetime
from django.http import JsonResponse
from django.views.generic import ListView

class ApiView(ListView):
    model = Acldb
    template_engine = 'apiAlert/apiUnreact.html'
    context_object_name = 'queryset'




def alertUnreactedApi(request):
    querysetUnreacted = Acldb.objects.filter(statusCheck='False')
    template_name='alerts/unreacted.html'
    data = []

    for queryset in querysetUnreacted:
        data.append(
            {'id':queryset.id,
            'exception':queryset.Exception_Category,
            'affiliateCode':queryset.Affiliate_Code,
            'accountName':queryset.Account_Name,
            'accountNumber':queryset.Acccount_Number,
            'branch':queryset.Initiating_Branch,
            'class':queryset.ACCOUNT_CLASS,
            'tier':queryset.account_tier,
            'currency':queryset.Currency,
            'LcyAmountInvolved':queryset.Amount_Involved_LCY,
            'pnd':queryset.AcctPND,
            'balance':queryset.ACY_CURR_BALANCE,
            'dateDiscovered':queryset.Date_Discovered
            }
        )
    
    return JsonResponse(data, safe=False)