from apps.product.models import Category

def menu_categories(request):
    categories = Category.objects.all() [0:3]

    return {'menu_categories': categories}

def other_categories(request):
    other = Category.objects.all() [4:]
    
    return {'other_categories': other}