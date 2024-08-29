# In book/views.py
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Book
import json
from rest_framework import generics,viewsets
from .serializers import BookSerializer
from rest_framework import filters

#from rest_framework.views import APIView
#from rest_framework.response import Response 

#class BookListCreateView(generics.ListCreateAPIView):
  #queryset = Book.objects.all()
  #serializer_class = BookSerializer


def rest_get_books(request):

    queryset = Book.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            sip_calling_reg__icontains=request.GET.get('search'))

    data = serializers.serialize('json', queryset)
    return HttpResponse(data, content_type='application/json')


def books(request):
    if request.method == 'POST':
        data = request.POST

        #title = data.get('title')
        #author = data.get('author')
        #publication_year = data.get('publication_year')

        time_stamp = data.get('time_stamp')
        sip_calling_party = data.get('sip_calling_party')
        #sip_calling_value = data.get('sip_calling_value')
        #sip_calling_ip_address = data.get('sip_calling_ip_address')
        sip_called_party = data.get('sip_called_party')
        #sip_called_value = data.get('sip_called_value')
        #sip_called_ip_address = data.get('sip_called_ip_address') 
        sip_call_duration = data.get('sip_call_duration')
        sip_call_status = data.get('sip_call_status')
        sip_rtp_l4_src_port = data.get('sip_rtp_l4_src_port')
        sip_rtp_l4_dst_port = data.get('sip_rtp_l4_dst_port')
        rtp_in_jitter = data.get('rtp_in_jitter')
        rtp_in_mos = data.get('rtp_in_mos')
        pkt_loss_per = data.get('pkt_loss_per')
        sip_calling_reg = data.get('sip_calling_reg') 
        sip_called_reg = data.get('sip_called_reg')

        Book.objects.create(
            #title=title,
            #author=author,
            #publication_year=publication_year,
            
            time_stamp = time_stamp,
            sip_calling_party = sip_calling_party,
            sip_called_party = sip_called_party,
            #sip_calling_value = sip_calling_value,
            #sip_calling_ip_address = sip_calling_ip_address,
            #sip_called_value = sip_called_value,
            #sip_called_ip_address = sip_called_ip_address,
            sip_call_duration = sip_call_duration,
            sip_call_status = sip_call_status,
            sip_rtp_l4_src_port = sip_rtp_l4_src_port,
            sip_rtp_l4_dst_port = sip_rtp_l4_dst_port,
            rtp_in_jitter = rtp_in_jitter,
            rtp_in_mos = rtp_in_mos,
            pkt_loss_per = pkt_loss_per,
            sip_calling_reg = sip_calling_reg,
            sip_called_reg = sip_called_reg
        )
        return redirect('/')

    queryset = Book.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            sip_calling_reg__icontains=request.GET.get('search'))

    context = {'books': queryset}
    return render(request, 'books.html', context)


def rest_import_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for item in data:
            book = Book(
                #title=item['title'],
                #author=item['author'],
                #publication_year=item['publication_year'],

                time_stamp = item['time_stamp'],
                sip_calling_party = item['sip_calling_party'],
                sip_called_party = item['sip_called_party'],                
                #sip_calling_value = item['sip_calling_value'],
                #sip_calling_ip_address = item['sip_calling_ip_address'],
                #sip_called_value = item['sip_called_value'],
                #sip_called_ip_address = item['sip_called_ip_address'],
                sip_call_duration = item['sip_call_duration'],
                sip_call_status = item['sip_call_status'],
                sip_rtp_l4_src_port = item['sip_rtp_l4_src_port'],
                sip_rtp_l4_dst_port = item['sip_rtp_l4_dst_port'],
                rtp_in_jitter = item['rtp_in_jitter'],
                rtp_in_mos = item['rtp_in_mos'],
                pkt_loss_per = item['pkt_loss_per'],
                sip_calling_reg = item['sip_calling_reg'],
                sip_called_reg = item['sip_called_reg']
            )
            book.save()

    queryset = Book.objects.all()
    data = serializers.serialize('json', queryset)    
    return HttpResponse(data, content_type='application/json')


def import_data(request):
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        for item in data:
            book = Book(
                #title=item['title'],
                #author=item['author'],
                #publication_year=item['publication_year'],

                time_stamp = item['time_stamp'],
                sip_calling_party = item['sip_calling_party'],
                sip_called_party = item['sip_called_party'],                 
                #sip_calling_value = item['sip_calling_value'],
                #sip_calling_ip_address = item['sip_calling_ip_address'],
                #sip_called_value = item['sip_called_value'],
                #sip_called_ip_address = item['sip_called_ip_address'],
                sip_call_duration = item['sip_call_duration'],
                sip_call_status = item['sip_call_status'],
                sip_rtp_l4_src_port = item['sip_rtp_l4_src_port'],
                sip_rtp_l4_dst_port = item['sip_rtp_l4_dst_port'],
                rtp_in_jitter = item['rtp_in_jitter'],
                rtp_in_mos = item['rtp_in_mos'],
                pkt_loss_per = item['pkt_loss_per'],
                sip_calling_reg = item['sip_calling_reg'],
                sip_called_reg = item['sip_called_reg']
            )
            book.save()
        return render(request, 'success.html')
    return render(request, 'form.html')


def rest_delete_book(request, id):
    queryset = Book.objects.get(id=id)
    queryset.delete()
    
    queryset = Book.objects.all()
    data = serializers.serialize('json', queryset)
    return HttpResponse(data, content_type='application/json')


def delete_book(request, id):
    queryset = Book.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def rest_update_book(request, id):
    queryset = Book.objects.get(id=id)

    if request.method == 'POST':

        data = json.loads(request.body)

        #title = data[0]['title']
        #author = data[0]['author']
        #publication_year = data[0]['publication_year']

        time_stamp = data[0]['time_stamp']
        sip_calling_party = data[0]['sip_calling_party']
        sip_called_party = data[0]['sip_called_party']         
        #sip_calling_value = data[0]['sip_calling_value']
        #sip_calling_ip_address = data[0]['sip_calling_ip_address']
        #sip_called_value = data[0]['sip_called_value']
        #sip_called_ip_address = data[0]['sip_called_ip_address']
        sip_call_duration = data[0]['sip_call_duration']
        sip_call_status = data[0]['sip_call_status']
        sip_rtp_l4_src_port = data[0]['sip_rtp_l4_src_port']
        sip_rtp_l4_dst_port = data[0]['sip_rtp_l4_dst_port']
        rtp_in_jitter = data[0]['rtp_in_jitter']
        rtp_in_mos = data[0]['rtp_in_mos']
        pkt_loss_per = data[0]['pkt_loss_per']
        sip_calling_reg = data[0]['sip_calling_reg']
        sip_called_reg = data[0]['sip_called_reg']
        
        #queryset.title = title
        #queryset.author = author
        #queryset.publication_year = publication_year

        queryset.time_stamp = time_stamp
        queryset.sip_calling_party = sip_calling_party
        queryset.sip_called_party = sip_called_party
        #queryset.sip_calling_value = sip_calling_value
        #queryset.sip_calling_ip_address = sip_calling_ip_address
        #queryset.sip_called_value = sip_called_value
        #queryset.sip_called_ip_address = sip_called_ip_address
        queryset.sip_call_duration = sip_call_duration
        queryset.sip_call_status = sip_call_status
        queryset.sip_rtp_l4_src_port = sip_rtp_l4_src_port
        queryset.sip_rtp_l4_dst_port = sip_rtp_l4_dst_port
        queryset.rtp_in_jitter = rtp_in_jitter
        queryset.rtp_in_mos = rtp_in_mos
        queryset.pkt_loss_per = pkt_loss_per
        queryset.sip_calling_reg = sip_calling_reg
        queryset.sip_called_reg = sip_called_reg

        queryset.save()

    queryset = Book.objects.all()
    data = serializers.serialize('json', queryset)
    return HttpResponse(data, content_type='application/json')
    

def update_book(request, id):
    queryset = Book.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        #title = data.get('book_title')
        #author = data.get('book_author')
        #publication_year = data.get('book_publication_year')

        time_stamp = data.get('timestamp')
        sip_calling_party = data.get('sipcallingparty')
        sip_called_party = data.get('sipcalledparty')
        #sip_calling_value = data.get('sip_calling_value')
        #sip_calling_ip_address = data.get('sip_calling_ip_address') 
        #sip_called_value = data.get('sip_called_value')
        #sip_called_ip_address = data.get('sip_called_ip_address') 
        sip_call_duration = data.get('sipcallduration')
        sip_call_status = data.get('sipcallstatus')
        sip_rtp_l4_src_port = data.get('siprtpl4srcport')
        sip_rtp_l4_dst_port = data.get('siprtpl4dstport')
        rtp_in_jitter = data.get('rtpinjitter')
        rtp_in_mos = data.get('rtpinmos')
        pkt_loss_per = data.get('pktlossper')
        sip_calling_reg = data.get('sipcallingreg') 
        sip_called_reg = data.get('sipcalledreg')

        #queryset.title = title
        #queryset.author = author
        #queryset.publication_year = publication_year

        queryset.time_stamp = time_stamp
        queryset.sip_calling_party = sip_calling_party
        queryset.sip_called_party = sip_called_party
        #queryset.sip_calling_value = sip_calling_value
        #queryset.sip_calling_ip_address = sip_calling_ip_address
        #queryset.sip_called_value = sip_called_value
        #queryset.sip_called_ip_address = sip_called_ip_address
        queryset.sip_call_duration = sip_call_duration
        queryset.sip_call_status = sip_call_status
        queryset.sip_rtp_l4_src_port = sip_rtp_l4_src_port
        queryset.sip_rtp_l4_dst_port = sip_rtp_l4_dst_port
        queryset.rtp_in_jitter = rtp_in_jitter
        queryset.rtp_in_mos = rtp_in_mos
        queryset.pkt_loss_per = pkt_loss_per
        queryset.sip_calling_reg = sip_calling_reg
        queryset.sip_called_reg = sip_called_reg

        queryset.save()
        return redirect('/')

    context = {'book': queryset}
    return render(request, 'update_book.html', context)


class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['sip_calling_reg']
