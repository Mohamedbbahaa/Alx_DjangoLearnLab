from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework import status
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import logout
from rest_framework import generics
# Create your views here.



class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return render(request, 'logout.html')

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class follow_user(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try: 
            user = User.objects.get(id=user_id)
            if user == request.user:
                return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                request.user.following.add(user)
                return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
class unfollow_user(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try: 
            if user_id == request.user.id:
                return Response({"error": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = User.objects.get(id=user_id)
                request.user.following.remove(user)
                return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        


#CustomUser.objects.all()