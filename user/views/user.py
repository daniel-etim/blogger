from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from user.models.user import User
from user.serializers.auth import LoginSerializer, RegisterSerializer
from user.serializers.user import UserModelSerializer


@api_view(["GET"])
def home(request: Request):
    return Response(data = "This is Home", status=status.HTTP_200_OK)

@api_view(["GET"])
def greeting(request: Request):
    name = request.query_params.get("name") # gets the name of user
    if name is None:
        return Response(data={"error": "provide a query_param 'name'"}, status=status.HTTP_400_BAD_REQUEST)
    
    # return a greeting with user name
    return Response(data = {"message": f"Hello {name.capitalize()}, you're welcome to Home Page"}, status=status.HTTP_200_OK)

@api_view(["POST"])
def register(request: Request):
    # gets the data and validates it
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # clean data
    clean_data = serializer.validated_data

    # authenticate data
    try:
        user = User.objects.create_user(
            username=clean_data["email"],
            first_name=clean_data["first_name"],
            last_name=clean_data["last_name"],
            email=clean_data["email"],
            password=clean_data["password"]
        )
    except IntegrityError:
        return Response(data={"error": "this email already existed"}, status=status.HTTP_409_CONFLICT)
    
    # data would have been successfully authenticated by here
    serializer = UserModelSerializer(user)
    return Response(data={"message": "Successfully Registered!", "data": serializer.data}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def login(request: Request):
    # gets the data and validates it
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # clean data
    clean_data = serializer.validated_data

    # authenticate data
    user = authenticate(username=clean_data["username"], password=clean_data["password"])
    if not user:
        return Response(data={"error": "incorrect name or password"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # data would have been successfully authenticated by here
    serializer = UserModelSerializer(user)
    return Response(data={"message": "Login Successful", "data": serializer.data}, status=status.HTTP_200_OK)