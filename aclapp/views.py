from django.shortcuts import render, get_object_or_404, redirect
from .models import Acldb
import datetime
from django.http import JsonResponse
from django.views.generic import ListView
from .forms import Alert_update_form, SearchForm, CreateUserForm
from .filters import AlertFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('unreacted')

        else:
            messages.info(request, 'Username OR password is incorrect')
        

    template_name = 'alerts/login.html'
    context = {
        
    }
    return render(request, template_name, context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " +user)
            return redirect('login')


    template_name = 'alerts/register.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)

@login_required()
def alertUnreactedView(request):
    userOrder = Acldb.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    total_closed_query = closedQuery.count()
    #closedQuery = Acldb.objects.filter(Status_REGULARIZED_UNREGULARIZED__in=['3', '1']).filter(Date_Regularised__gte=datetime.date.today())
    

    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())

    #pendingQuery_today = userOrder.filter(Status_REGULARIZED_UNREGULARIZED__in=['8','7','2']).filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()
    pending_query = userOrder.filter(statusCheck='Pending')

    #pending_query = userOrder.filter(Status_REGULARIZED_UNREGULARIZED__in=['8','7','2'])

    treated = userOrder.filter(statusCheck__in=['Pending','Closed']).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()
    
    queryset = Acldb.objects.filter(statusCheck='Unreacted')
    

    myFilter = AlertFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 50)

    queryset = paginator.get_page(page)

    template_name='alerts/unreacted.html'
    context = {
        'queryset':queryset,
        'myFilter':myFilter,
        'total_closed_query':total_closed_query,
        'pending_count':pending_count,
        'total_treated':total_treated,
        'pending_query':pending_query
        }

    return render(request, template_name, context)

@login_required()
def alertPending(request):
    userOrder = Acldb.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    total_closed_query = closedQuery.count()
    #closedQuery = Acldb.objects.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    #closedQuery = Acldb.objects.filter(Status_REGULARIZED_UNREGULARIZED__in=['3', '1']).filter(Date_Regularised__gte=datetime.date.today())
    #total_closed_query = closedQuery.count()

    userOrder = Acldb.objects.filter(CAMT_Reveiewer=request.user)
    pendingQuery = userOrder.filter(statusCheck='Pending').order_by('Date_Regularised')
    
    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())
    #pendingQuery = userOrder.filter(Status_REGULARIZED_UNREGULARIZED__in=['8','7','2']).order_by('Date_Regularised')

    #pendingQuery_today = userOrder.filter(Status_REGULARIZED_UNREGULARIZED__in=['8','7','2']).filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()

    treated = userOrder.filter(statusCheck__in=['Pending','Closed']).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()

    template_name = 'alerts/pending.html'
    context = {
        'pendingQuery':pendingQuery,
        'total_closed_query':total_closed_query,
        'pending_count':pending_count,
        'total_treated':total_treated
        }
    return render(request, template_name, context)


@staff_member_required()
def alertClosed_staff(request):
    userOrder = Acldb.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = Acldb.objects.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today()).order_by('Date_Regularised')


    treated = userOrder.filter(statusCheck__in=['Pending','Closed']).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()


    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()

    #closedQuery = Acldb.objects.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    #total_closed_query = closedQuery.count()
    userOrder = Acldb.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery_count = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    total_closed_query = closedQuery_count.count()

    pending_query = userOrder.filter(statusCheck='Pending')
    


    template_name='alerts/regularised_staff.html'
    context = {
        'pendingQuery':closedQuery,
        'total_treated':total_treated,
        'pending_count':pending_count,
        'total_closed_query':total_closed_query,
        'pending_query':pending_query
        }
    return render(request, template_name, context)

@login_required()
def alertClosed_user(request):
    userOrder = Acldb.objects.filter(CAMT_Reveiewer=request.user)
    closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    #userOrder = Acldb.objects.filter(CAMT_Reveiewer=request.user)
    #closedQuery = userOrder.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today()).order_by('Date_Regularised')
    total_closed_query = closedQuery.count()


    treated = userOrder.filter(statusCheck__in=['Pending','Closed']).filter(Date_Regularised__gte=datetime.date.today())
    total_treated = treated.count()

    
    pendingQuery_today = userOrder.filter(statusCheck='Pending').filter(Date_Regularised__gte=datetime.date.today())
    pending_count = pendingQuery_today.count()

    #closedQuery = Acldb.objects.filter(statusCheck='Closed').filter(Date_Regularised__gte=datetime.date.today())
    #total_closed_query = closedQuery.count()
    pending_query = userOrder.filter(statusCheck='Pending')


    template_name='alerts/regularised.html'
    context = {
        'pendingQuery':closedQuery,
        'total_treated':total_treated,
        'pending_count':pending_count,
        'total_closed_query':total_closed_query,
        'pending_query':pending_query
        }
    return render(request, template_name, context)


def alertDetail(request, pk):
    alertDetail = get_object_or_404(Acldb, id=pk)

    template_name = 'alerts/alertDetail.html'
    context = {
        'alertDetail':alertDetail
    }
    return render(request, template_name, context)


@login_required()
def acl_update(request, id):
    queryset = get_object_or_404(Acldb, id=id)
    forms = Alert_update_form(request.POST or None, instance=queryset)

    if forms.is_valid():
        queryset.CAMT_Reveiewer = request.user
        queryset.Date_Regularised = datetime.datetime.now()
        forms.save()
        forms = Alert_update_form()

        return redirect('unreacted')

    template_name = 'alerts/updateAlert.html'
    context = {
        'alerts': queryset,
        'forms':forms,
    }

    return render(request, template_name, context)






#the API SIDE OF THINGS
class ApiView(ListView):
    model = Acldb
    template_name = 'apiAlert/apiUnreact.html'
    context_object_name = 'queryset'


def alertUnreactedApi(request):
    querysetUnreacted = Acldb.objects.filter(statusCheck='False')
    #template_name='alerts/unreacted.html'
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
