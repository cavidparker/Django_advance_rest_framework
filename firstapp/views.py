from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
# @permission_classes([AllowAny,])
def firstAPI(request):
    if request.method == "POST":
        name = request.data['name']
        age = request.data['age']
        print(name, age)
        return Response({"name":name, "age":age})
    context = {
        'name': 'John',
        'university': 'UBC',
    }
    return Response(context)

@api_view(['POST'])
def registrationAPI(request):
    if request.method == "POST":
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"})
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"})
        if password1 != password2:
            return Response({"error": "Passwords do not match"})   

        user = User()
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.set_password(raw_password=password1)
        user.save()

        return Response({"success": "User successfully registered"})


from .models import Contact
from rest_framework.views import APIView
#                                 # @api_view(['POST'])
# class ContactAPIView(APIView):   #def contactpost(request):
#     permission_classes=[AllowAny,]
#     def post(self, request):     #if request.method=="POST":    
#         data = request.data
#         name = data['name']
#         email = data['email']
#         phone = data['phone']
#         subject = data['subject']
#         details = data['details']

#         contact = Contact()
#         contact = Contact(name=name, email=email, phone=phone, subject=subject, details=details)
#         contact.save()
#         return Response({"success": "Contact successfully added"})
#     def get(self,request,format=None):
#             return Response({"success": "Contact successfully saved! from get"})

from .serializers import ContactSerializer 
class ContactAPIView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request, format=None):
        # data=request.data
        seralizer = ContactSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
        return Response(seralizer.data)  # respone all the data 
        # return Response({"success": "Contact successfully added"})
    def get(self,request,format=None):
        queryset = Contact.objects.all()
        seralizer = ContactSerializer(queryset, many=True)
        return Response(seralizer.data)
        return Response({"success": "Contact successfully saved! from get"})        
