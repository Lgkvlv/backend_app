from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from myapp1.models import TelegramUsers, Roles


# Create your views here.
# MODEL-VIEW-TEMPLATE

def show_index_page(request):
    users = TelegramUsers.objects.all()
    return render(request, 'index.html', context={'data': users })

def show_roles_page(request):
    all_roles = Roles.objects.all()

    # Способ 1.Фильтр через связанное поле
    #users_adm_roles = TelegramUsers.objects.filter (role__name ='Администратор')

    # Способ 2.Фильтр через предварительно полученный объект
    #role_design = Roles.objects.get(name='Дизайнер')
    #users_designer_role = TelegramUsers.objects.filter(role=role_design)

    # Способ 2. Обратный запрос через Related Manager
    #role_develop = Roles.objects.get(name='Разработчик')
    #users_develop_role = role_develop.telegramusers_set.all()
    #print(users_develop_role)

    return render(request, 'roles.html', context={'data': all_roles})

def get_user_data(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        try:
            user = TelegramUsers.objects.get(user_id=user_id)
            data = {
                'username': user.username,
                'role': user.role.name,
                'user_id': user.user_id
            }
            return JsonResponse(data)
        except TelegramUsers.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)








