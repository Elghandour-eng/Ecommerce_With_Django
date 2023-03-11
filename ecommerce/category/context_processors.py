from .models import Category

# this method is used to return a dictionary of values that will be added to the template context
# values is the links of the categories
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links) 