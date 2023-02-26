from todo.models import Category


def global_category_context(request):
    return dict(
        global_categories = Category.objects.filter(is_active=True)
    )   