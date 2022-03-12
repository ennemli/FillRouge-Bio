from django.template import Library
from bbe.models import Product
register = Library()


@register.simple_tag(takes_context=True)
def bbe_user(context):
    user = context["user"]
    return user
@register.simple_tag(takes_context=True)
def is_user_authenticated(context):
    user = context["user"]
    return user.is_authenticated

@register.simple_tag(takes_context=True)
def is_user_anonymous(context):
    user = context["user"]
    return user.is_anonymous
# @register.inclusion_tag("products_template.html")
# def show_products(_len,filter="price"):
#     products_object=Product.objects.all().order_by(f"-{filter}").all()
#     products=[[]]
#     i=0
#     for product in products_object:
#         product_dic={
#             "name":product.product_name,
#             "description":product.product_description,
#             "price":product.price,
#             "is_available":product.is_available,
#             "max_quantity":product.max_quantity,
#             "left_quantity":product.left_quantity,
#             "thumbnail":f"static/uploads/{product.images.image}"

#         }
#         if i==3:
#             i=0
#             products.append([product_dic])
#         else:
#             products[-1].append(product_dic)
#         i+=1
#     return {"products":products}
