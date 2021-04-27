from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from offers.models import Category, Offer
from offers.serializers import CategorySerializer, OfferSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def categoryApi(request,id=0):
    if request.method=='GET':
        categorys = Category.objects.all()
        categorys_serializer = CategorySerializer(categorys, many=True)
        return JsonResponse(categorys_serializer.data, safe=False)
    
    elif request.method=='POST':
        category_data=JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added SuccessFully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category=Category.objects.get(id=category_data['id'])
        category_serializer=CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        category=Category.objects.get(id=id)
        category.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def offerApi(request,id=0):
    if request.method=='GET':
        offers = Offer.objects.all()
        offers_serializer = OfferSerializer(offers, many=True)
        return JsonResponse(offers_serializer.data, safe=False)
    
    elif request.method=='POST':
        offer_data=JSONParser().parse(request)
        offer_serializer = OfferSerializer(data=offer_data)
        if offer_serializer.is_valid():
            offer_serializer.save()
            return JsonResponse("Added SuccessFully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        offer_data = JSONParser().parse(request)
        offer=Offer.objects.get(id=offer_data['id'])
        offer_serializer=OfferSerializer(offer, data=offer_data)
        if offer_serializer.is_valid():
            offer_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        offer=Offer.objects.get(id=id)
        offer.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def offerApiId(request,id=0):
    if request.method=='GET':
        offers = Offer.objects.filter(Cat_id=id)
        offers_serializer = OfferSerializer(offers, many=True)
        return JsonResponse(offers_serializer.data, safe=False)


@csrf_exempt
def offerApibyId(request,id=0):
    if request.method=='GET':
        offers = Offer.objects.get(id=id)
        offers_serializer = OfferSerializer(offers)
        return JsonResponse(offers_serializer.data, safe=False)


@csrf_exempt
def offerApibyOfferId(request,id=0):
    if request.method=='GET':
        offers = Offer.objects.filter(id=id)
        offers_serializer = OfferSerializer(offers,  many=True)
        return JsonResponse(offers_serializer.data, safe=False)


@csrf_exempt
def offerByUserId(request,id=0):
    if request.method=='GET':
        offers = Offer.objects.filter(user_id=id)
        offers_serializer = OfferSerializer(offers, many=True)
        return JsonResponse(offers_serializer.data, safe=False)