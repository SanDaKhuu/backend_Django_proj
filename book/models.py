# In book/models.py
from django.db import models

class Book(models.Model):
    #title = models.CharField(max_length=100)
    #author = models.CharField(max_length=100)
    #publication_year = models.IntegerField()
    
    
    time_stamp = models.CharField(max_length=100)
    sip_calling_party = models.CharField(max_length=100)
    #sip_calling_value = models.IntegerField()
    #sip_calling_ip_address = models.CharField(max_length=100)
    sip_called_party = models.CharField(max_length=100)
    #sip_called_value = models.IntegerField()
    #sip_called_ip_address = models.CharField(max_length=100)
    sip_call_duration = models.IntegerField()
    sip_call_status = models.CharField(max_length=100)
    sip_rtp_l4_src_port = models.IntegerField()
    sip_rtp_l4_dst_port = models.IntegerField()
    rtp_in_jitter = models.IntegerField()
    rtp_in_mos = models.DecimalField(max_digits=6, decimal_places=1)
    pkt_loss_per = models.DecimalField(max_digits=6, decimal_places=1)
    sip_calling_reg = models.CharField(max_length=100)
    sip_called_reg = models.CharField(max_length=100)