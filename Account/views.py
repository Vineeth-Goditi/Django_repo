from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status



# Create your views here.
# The RegisterView class is a subclass of APIView. It has a post method that takes in a request
# object. It then tries to serialize the data in the request object. If the serialization is
# successful, it saves the data and returns a response with a message. If the serialization is not
# successful, it returns a response with an error message

class RegisterView(APIView):

    def post(self, request):
        try:
            data =request.data

            serializer = RegisterSerializer(data= data)

            if not serializer.is_valid():
                return Response({
                   'data' : serializer.errors,
                   'message' : 'something went wrong'
                }, status= status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data' : {},
                'message': 'Your Account is created'
            }, status= status.HTTP_201_CREATED)   

        except Exception as e:
            return Response({
                   'data' : {},
                   'message' : 'something went wrong'
                }, status= status.HTTP_400_BAD_REQUEST)

# It takes in a request, validates the request, and returns a response

class LoginView(APIView):

    def post(self, request):
        try:
            
            data = request.data
            serializer = LoginSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "something went wrong"
                }, status= status.HTTP_400_BAD_REQUEST)
                
            response= serializer.get_jwt_token(serializer.data) 
            
            return Response(response, status= status.HTTP_200_OK)   

            
        except Exception as e:
            print(e)
            return Response({
                   'data' : {},
                   'message' : 'something went wrong bb'
                }, status= status.HTTP_400_BAD_REQUEST)      