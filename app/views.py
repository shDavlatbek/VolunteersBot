from django.http import JsonResponse
from .models import User, Guest

def get_users_by_category(request):
    categories = request.GET.get('categories')
    if categories:
        categories = list(map(int, categories.split(',')))
        users = User.objects.filter(guests__in=Guest.objects.filter(categories__id__in=categories)).distinct()
        print(users)
        users_data = [{'id': user.id, 'name': user.full_name()} for user in users]
        return JsonResponse({'users': users_data})
    return JsonResponse({'users': []})

def get_users_all(request):
    users_data = [{'id': user.id, 'name': user.full_name()} for user in User.objects.all()]
    return JsonResponse({'users': users_data})