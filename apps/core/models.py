
from django.db import models


class tr_get3BData(models.Model):	
    GSTIN	= models.CharField(max_length=200, blank=True, null=True)	
    ReturnPeriod = models.CharField(max_length=200, blank=True, null=True)	
    Three_BTable	= models.CharField(max_length=200, blank=True, null=True)	# actually columns 3BTable
    NatureOfSupplyType	= models.CharField(max_length=200, blank=True, null=True)	
    TaxableValue =  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    IGSTAmount	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    CGSTAmount	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    SGSTAmount	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    CESSAmount	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    POS	= models.CharField(max_length=200, blank=True, null=True)	
    InterStateSupplies	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    IntraStateSupplies	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    LiablityLedgerID	= models.CharField(max_length=200, blank=True, null=True)	
    LiablityReturnPeriod	= models.CharField(max_length=200, blank=True, null=True)	
    TransactionType	= models.CharField(max_length=200, blank=True, null=True)	
    IGSTInterest	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    IGSTFee	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    CGSTInterest	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    CGSTFee	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    SGSTInterest	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    SGSTFee	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    CESSInterest	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    CESSFee	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    IGSTPaidAsCGST	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    IGSTPaidAsSGST	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    CGSTPaidAsIGST	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    SGSTPaidAsIGST	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    Raw3b_ID = models.IntegerField(null=True)
    CreatedOn = models.DateTimeField(auto_now=True)	
    IsActive = models.BooleanField(default=False)	
    DeletedOn =  models.DateTimeField(null=True)	
    FP = models.CharField(max_length=200, blank=True, null=True)	
    SyncID = models.IntegerField(null=True)

    class Meta():
        db_table = 'tr_get3BData'



class tr_gstr2b_itcsumm(models.Model):		
    Eid	= models.IntegerField(blank=True, null=True)
    gstin = models.CharField(max_length=50, blank=True, null=True)	
    fp = models.CharField(max_length=50, blank=True, null=True)	
    summ_type = models.CharField(max_length=50, blank=True, null=True)	
    supply_type = models.CharField(max_length=50, blank=True, null=True)	
    invoice_category = models.CharField(max_length=50, blank=True, null=True)	
    summary_igst =  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    summary_cgst =  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    summary_sgst =  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    summary_cess =  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    tr_igst	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    tr_cgst	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    tr_sgst	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    tr_cess	=  models.DecimalField(max_digits=18, decimal_places=2, blank = True, null=True)	
    TableName2B = models.CharField(max_length=50, blank=True, null=True)	
    TableName3B = models.CharField(max_length=50, blank=True, null=True)	
    user_id = models.IntegerField(blank=True, null=True)	
    batch_no = models.CharField(max_length=50, blank=True, null=True)	
    row_version = models.DateTimeField(null=True)	
    CreatedOn = models.DateTimeField(auto_now=True)	
    SyncID  =	models.IntegerField(blank=True, null=True)	
    fpNew = models.DateField(null=True)

    class Meta():
        db_table = 'tr_gstr2b_itcsumm'