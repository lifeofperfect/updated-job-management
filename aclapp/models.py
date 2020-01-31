from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Exception_By_Category(models.Model):
    exception_type = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Exception By Category"

    def __str__(self):
        return self.exception_type

class Dropdown_Category_root_cause_tag(models.Model):
    category_tag = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Root Cause Tag"

    def __str__(self):
        return self.category_tag

class Dropdown_by_root_cause(models.Model):
    root_cause = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Root Cause category'

    def __str__(self):
        return self.root_cause

class Dropdown_status(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status


class Dropdown_activity(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Activity'

    def __str__(self):
        return self.status

class Dropdown_loss_category(models.Model):
    loss_category = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Loss Category'

    def __str__(self):
        return self.loss_category
    

class Acldb(models.Model):
    choices = (

        ('Pending', 'Pending'),

        ('Closed', 'Closed'),
        ('Unreacted', 'Unreacted')

    )

    Exception_Category = models.CharField(max_length=200)	
    Exception_By_Category_Type =models.ForeignKey(Exception_By_Category, blank=True, null=True, on_delete=models.SET_NULL)	
    Affiliate_Code = models.CharField(max_length=5, null=True, blank=True)	
    Affiliate_Name = models.CharField(max_length=30,blank=True, null=True)	
    Initiating_Branch = models.CharField(max_length=200, null=True, blank=True)	
    Zone = models.CharField(max_length=20, null=True, blank=True)	
    Region = models.CharField(max_length=20, blank=True, null=True)	
    Trn_Ref_no	= models.CharField(max_length=200,blank=True, null=True)
    Acccount_Number	= models.CharField(max_length=30,blank=True, null=True)
    Account_Name	= models.CharField(max_length=200, null=True)
    msisdn	= models.CharField(max_length=20,blank=True, null=True)
    ACCOUNT_CLASS = models.CharField(max_length=10, null=True, blank=True)	
    account_tier = models.IntegerField(null=True, blank=True)
    DRCR_IND = models.CharField(max_length=5,blank=True, null=True)
    ACY_CURR_BALANCE = models.FloatField(default=0)	
    AC_OPEN_DATE = models.DateField(blank=True, null=True)
    AcctPND	= models.CharField(max_length=3, null=True, blank=True)
    TnxCount = models.IntegerField(default=1, null=True)
    DrMeanMaxAmt = models.IntegerField(default=0, null=True, blank=True)
    CrMeanMaxAmt = models.IntegerField(default=0, null=True, blank=True)
    Summary_Of_Incidence_and_CAMT_observation_during_Investigation = models.TextField(max_length=100, blank=True, null=True)	
    OPERATORS_RESPONSE = models.CharField(max_length=100, blank=True, null=True)
    Date_Discovered	= models.DateField(auto_now=True,null=True, blank=True)
    Date_Regularised = models.DateTimeField(auto_now=True)	
    Root_Cause_Tag = models.ForeignKey(Dropdown_Category_root_cause_tag, on_delete=models.SET_NULL, null=True, blank=True)	
    Category_By_Root_Cause = models.ForeignKey(Dropdown_by_root_cause, on_delete=models.SET_NULL, null=True, blank=True)
    Status_REGULARIZED_UNREGULARIZED = models.ForeignKey(Dropdown_status, on_delete=models.SET_NULL, null=True, blank=True)	
    Currency = models.CharField(max_length=5, blank=True, null=True)	
    LCY_USD_RATE = models.FloatField(default=1)	
    Amount_Involved_LCY = models.FloatField(default=0)
    Amount_at_Risk_LCY = models.FloatField(default=0)	
    Loss_prevented_LCY = models.FloatField(default=0)
    Loss_prevented_USD = models.FloatField(default=0)
    Inputter = models.CharField(max_length=100, null=True)
    Authoriser = models.CharField(max_length=100, null=True)
    USERID_Inputter = models.CharField(max_length=20, null=True)
    USERID_Authoriser = models.CharField(max_length=20, null=True)
    CAMT_Reveiewer	= models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    Month = models.CharField(max_length=20, blank=True, null=True)
    Activity = models.ForeignKey(Dropdown_activity, on_delete=models.SET_NULL, null=True, blank=True)	
    Loss_Category = models.ForeignKey(Dropdown_loss_category, on_delete=models.SET_NULL, null=True, blank=True)
    Count2 = models.IntegerField(default=1)
    statusCheck = models.CharField(choices=choices, default='Unreacted', max_length=20)
    ONBOARDING_DATE = models.DateField(null=True, blank=True) 


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.Exception_Category
    
