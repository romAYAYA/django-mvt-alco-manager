from django.http import HttpRequest


def get_active_user(request: HttpRequest) -> dict[str, any]:
    if request.user.is_authenticated:
        return {'user_name': request.user.username}
    else:
        return {'user_name': None}
