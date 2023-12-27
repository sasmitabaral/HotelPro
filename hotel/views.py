from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def get_hotel(request):
    try:
        hotel_objs=Hotel.objects.all()
        if request.GET.get('sort_by'):
            sort_by_value=request.GET.get('sort_by')
            if sort_by_value=='asc':
                hotel_objs=hotel_objs.order_by('hotel_price')
            elif sort_by_value=='des':
                hotel_objs=hotel_objs.order_by('-hotel_price')
        if request.GET.get('amount'):
            amount=request.GET.get('amount')
            hotel_objs=hotel_objs.filter(hotel_price_lte=amount)


        payload=[]
        for hotel_obj in hotel_objs:
            payload.append({
                'hotel_name':hotel_obj.hotel_name,
                'hotel_price':hotel_obj.hotel_price,
                'hotel_description':hotel_obj.hotel_description,
                'banner_image':str(hotel_obj.banner_image),

            })
        return JsonResponse(payload,safe=False)    



    except Exception as e:  
        print(e) 
    return JsonResponse({'message':'something went wrong,'})     
