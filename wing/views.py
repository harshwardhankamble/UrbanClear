from django.shortcuts import render
from .models import Item
# Create your views here.
def index(request):
	
	item = Item.objects.all();

	return render(request,'index.html',{'item':item});