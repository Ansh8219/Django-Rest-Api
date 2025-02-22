# accounts/views.py
from rest_framework import generics , status
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.response import Response
# Signup API view: Handles POST requests to register a new user.
class SignupAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # This will raise an exception and return a 400 with errors if invalid.
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "message": "User account successfully created",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )