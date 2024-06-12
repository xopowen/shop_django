from django.views.decorators.csrf import  ensure_csrf_cookie

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import Response,Request

@api_view(['HEAD'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def set_csrf_token(request: Request):
    """
    set CSRF token into request
    This will be `/api/set-csrf-cookie/` on `urls.py`

    """

    return Response(status=200)



