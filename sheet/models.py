from django.db import models

class Ledger(models.Model):
    lender = models.CharField(max_length = 100, default = "")
    borrower = models.CharField(max_length = 100, default = "")
    amount = models.FloatField(default = 0.0)
    grp = models.CharField(max_length = 100, null = True)
    desc = models.CharField(max_length = 500, null = True)
    
    # def transaction(self):
    #     self.save()

    def __str__(self):
        return self.lender



class Group(models.Model):
    # lenders = models.CharField(max_length = 100, default = "[]")
    # borrowers = models.CharField(max_length = 100, default = "[]")
    # amounts = models.CharField(max_length = 100, default = "[]")
    grp_name = models.CharField(max_length = 100, null = True)
    # descs = models.CharField(max_length = 500, default = "[]")
    pk_vals = models.CharField(max_length = 500, default = "[]")
    
    # def transaction(self):
    #     self.save()

    def __str__(self):
        return self.grp_name


    
    