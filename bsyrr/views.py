from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from bsyrr.models import NewUser
import json



class UserRegistrationView(APIView):

    def validate(self):
     
        data = json.loads(self.request.body.decode('utf-8'))
        self.first_name = data.get("first_name", '')
        self.email = data.get("email", '')
        self.password = data.get("password", '')
    
        print("Data we are getting with using create post request : - ",self.first_name, self.email, self.password)

    def create_new_user(self):
        u = NewUser()
        u.email = self.email
        u.first_name = self.first_name
        u.save()
        print("user created success ")

    def post(self, request, format=None):
        self.validate()
        self.create_new_user()
        return Response({'msg': 'registration success'}, status=status.HTTP_201_CREATED)

        
        # serializer = UserRegistrationSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     User = serializer.save()
        #     return Response({'msg': 'registration success'}, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
# {
# "email":"fd@fd.com",
# "first_name":"fd",
# "password":"fd"

# }