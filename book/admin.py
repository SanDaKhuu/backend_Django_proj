from django.contrib import admin
from book.models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #list_display = ('title', 'author', 'publication_year')
    # 'sip_calling_value', 'sip_calling_ip_address', 'sip_called_value', 'sip_called_ip_address',

    list_display = ('time_stamp', 'sip_calling_party', 'sip_called_party',  'sip_call_duration', 'sip_call_status',     
    'sip_rtp_l4_src_port', 'sip_rtp_l4_dst_port', 'rtp_in_jitter', 'rtp_in_mos', 'pkt_loss_per', 
    'sip_calling_reg', 'sip_called_reg')

admin.site.register(Book, BookAdmin)
