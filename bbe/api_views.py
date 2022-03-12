from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from bbe.models import Product,ProductImage
from bbe.serializers import ProductSerializer,ProductImageSerializer
import time
@api_view(["GET"])
def get_all_products(request,f):
    if request.method=="GET":
        try:
            products=Product.objects.all().order_by(f"{f}")[:10]
        except:
            return HttpResponse(status=404)
        products_serializer=ProductSerializer(products,many=True)
        return JsonResponse(products_serializer.data,safe=False)
    return HttpResponse(status=404)
@api_view(["GET"])
def search_product(request,filter_query):
    if request.method=="GET":

        if search_product:
            results=Product.objects.filter(product_name__startswith=filter_query)
            results_serializer=ProductSerializer(results,many=True)
            results_json=results_serializer.data
        else:
            results_json={}
        return JsonResponse(results_json,safe=False)
    return HttpResponse(status=404) 

        
@api_view(["GET"])
def get_product_image(request,pk):
    if request.method=="GET":
        try:
            productImage=ProductImage.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        productImage_serializer=ProductImageSerializer(productImage)
        return JsonResponse(productImage_serializer.data,safe=False)
    return HttpResponse(status=404)
    