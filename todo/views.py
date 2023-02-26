from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Bu şekilde de yazılabilirdi " from todo.models import Todo "
from .models import Todo, Category, Tag
from django.http import Http404

@login_required(login_url='/admin/login/')  # Bu yapısayesinde login görülmemesi durumunda zorunlu oarak girişe yönlendirir.
def home_view(request):
    # todos = Todo.objects.filter(is_active = True)

    #  Bu arama şeklinde title sütununda todo içerenleri getir dedik.
    # todos = todos.filter(title__icontains="todo")

    # Bu şekilde de tek tapıda istedğimiz kadar sorgulama yapabiliriz. Sıraya dikkat edilerek yapılması daha iyi sonuçlar vercektir.
    todos = Todo.objects.filter(
        user=request.user,
        is_active=True,
        # title__icontains="todo",
    )

    context = dict(
        todos=todos,
    )
    return render(request, 'todo/todo_list.html', context)


# def todo_detail_view(request, id):
#     try:
#         todo = Todo.objects.get(pk=id)
#         context = dict(
#             todo=todo,
#         )
#         return render(request, 'todo/todo_detail.html', context)
#     except Todo.DoesNotExist:
#         raise Http404

# Yukarıdaki yapımım daha kısaltımış halini de kullanabiliriz.
@login_required(login_url='/admin/login/')
def todo_detail_view(request, id, category_slug):
    todo = get_object_or_404(Todo, category__slug=category_slug, pk=id, user=request.user)
    context = dict(
        todo=todo,
        category_slug=category_slug,
    )
    return render(request, 'todo/todo_detail.html', context)

@login_required(login_url='/admin/login/')
def category_detail_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    todos_category = Todo.objects.filter(
        user=request.user,
        is_active=True,
        category=category,
    )
    context = dict(
        category=category,
        todos_category=todos_category,
    )
    return render(request, 'todo/todo_list.html', context)


@login_required(login_url='/admin/login/')
def tag_detail_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    context=dict(
        tag=tag,
        todos=tag.todo_set.filter(user=request.user)
    )
    return render(request, 'todo/todo_list.html', context)