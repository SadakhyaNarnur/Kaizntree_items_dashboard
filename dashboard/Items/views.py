from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import Q

from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, ItemsForm
from .models import Itemlist, Category
from dashboard.settings import LOW_QUANTITY
from django.contrib import messages
from Items.models import Itemlist, Category
from Items.serializers import ItemSerializer, CategorySerializer
from django.core.files.storage import default_storage

class Index(TemplateView):
    	template_name = 'inventory/index.html'

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('index')

        return render(request, 'inventory/signup.html', {'form': form})

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        # items = Itemlist.objects.filter(user=self.request.user.id).order_by('id')

        
        items = Itemlist.objects.filter(user=self.request.user.id).order_by('id')
        # low_inventory = Itemlist.objects.filter(
        #     user=self.request.user.id,
        #     quantity__lte=LOW_QUANTITY
        # )

        # if low_inventory.count() > 0:
        #     if low_inventory.count() > 1:
        #         messages.error(request, f'{low_inventory.count()} items have low inventory')
        #     else:
        #         messages.error(request, f'{low_inventory.count()} item has low inventory')

        # low_inventory_ids = Itemlist.objects.filter(
        #     user=self.request.user.id,
        #     quantity__lte=LOW_QUANTITY
        # ).values_list('id', flat=True)  
        # Sorting
        sort_by = request.GET.get('sort_by')
        if sort_by:
            items = items.order_by(sort_by)

        # Searching
        search_query = request.GET.get('search')
        if search_query:
            items = items.filter(
                Q(SKU__icontains=search_query) |
                Q(Name__icontains=search_query) |
                Q(Tags__icontains=search_query) |
                Q(Category__icontains=search_query)
            )

        # Filtering
        # category = request.GET.get('category')
        # if category:
        #     items = items.filter(Category__icontains=category)

        items_serializer=ItemSerializer(items,many=True)
        # return JsonResponse(items_serializer.data,safe=False)
        print(items_serializer)
        return render(request, 'inventory/dashboard.html', {'items': items_serializer.data})

class AddItem(LoginRequiredMixin, CreateView):
    model = Itemlist
    form_class = ItemsForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditItem(LoginRequiredMixin, UpdateView):
	model = Itemlist
	form_class = ItemsForm
	template_name = 'inventory/item_form.html'
	success_url = reverse_lazy('dashboard')

class DeleteItem(LoginRequiredMixin, DeleteView):
	model = Itemlist
	template_name = 'inventory/delete_item.html'
	success_url = reverse_lazy('dashboard')
	context_object_name = 'item'


# Create your views here.
@csrf_exempt
def CountsApi(request, id=0):
    if request.method=='GET':
        items_count = Itemlist.objects.count()
        categories_count = Category.objects.count()
        data = {
            'items_count': items_count,
            'categories_count': categories_count
        }
        return JsonResponse(data)

@csrf_exempt
def ItemApi(request, id=0):
    if request.method=='GET':
        items = Itemlist.objects.all()

        # Sorting
        sort_by = request.GET.get('sort_by')
        if sort_by:
            items = items.order_by(sort_by)

        # Searching
        search_query = request.GET.get('search')
        if search_query:
            items = items.filter(
                Q(SKU__icontains=search_query) |
                Q(Name__icontains=search_query) |
                Q(Tags__icontains=search_query) |
                Q(Category__icontains=search_query)
            )

        # Filtering
        category = request.GET.get('category')
        if category:
            items = items.filter(Category__icontains=category)

        items_serializer=ItemSerializer(items,many=True)
        return JsonResponse(items_serializer.data,safe=False)
    elif request.method=='POST':
        item_data=JSONParser().parse(request)
        items_serializer=ItemSerializer(data=item_data)
        if items_serializer.is_valid():
            items_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        item_data=JSONParser().parse(request)
        items=Itemlist.objects.get(item_id=id)
        items_serializer=ItemSerializer(items,data=item_data)
        if items_serializer.is_valid():
            print("Valid")
            items_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        department=Itemlist.objects.get(item_id=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt    
def CategoryApi(request, id=0):
    if request.method=='GET':
        categories = Category.objects.all()
        category_serializer=CategorySerializer(categories,many=True)
        return JsonResponse(category_serializer.data,safe=False)
    elif request.method=='POST':
        categories=JSONParser().parse(request)
        category_serializer=CategorySerializer(data=categories)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        category_data=JSONParser().parse(request)
        categories=Category.objects.get(category_id=id)
        category_serializer=CategorySerializer(categories,data=category_data)
        if category_serializer.is_valid():
            print("Valid")
            category_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        categories=Category.objects.get(item_id=id)
        categories.delete()
        return JsonResponse("Deleted Successfully",safe=False)