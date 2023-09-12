from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

 
# # Method 2  
# class-based views
class PersonList(APIView):
  def post(self, request):
    name = request.data['name']
    person = Person.objects.filter(name=name).first()
    if person:
      return Response({"error": "Person already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = PersonSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    # serializer.validated_data
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
class PersonView(APIView):
  def get(self, request, identifier):
    if identifier.isdigit():
      person = get_object_or_404(Person, pk=identifier) 
    else:
      person = get_object_or_404(Person, name=identifier)
      
    serializer = PersonSerializer(person)
    return Response(serializer.data)
    
  def post(self, request, identifier):
    if identifier.isdigit():
      return Response({"error": "Wrong URL."}, status=status.HTTP_400_BAD_REQUEST)

    person = Person.objects.filter(name=identifier).first()
    if person:
      return Response({"error": "Person already exists"}, status=status.HTTP_400_BAD_REQUEST)
  
    data = {'name': identifier}
    serializer = PersonSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    # serializer.validated_data
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  # def post(self, request):
  #   print(request.data)
  #   name = request.data['name']
  #   person = get_object_or_404(Person, name=name)
  #   if person:
  #     return Response({"error": "Person already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
  #   serializer = PersonSerializer(data=request.data)
  #   serializer.is_valid(raise_exception=True)
  #   serializer.save()
  #   # serializer.validated_data
  #   return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  def put(self, request, identifier):
    if identifier.isdigit():
      person = get_object_or_404(Person, pk=identifier) 
    else:
      person = get_object_or_404(Person, name=identifier)
    
    serializer = PersonSerializer(person, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def patch(self, request, identifier):
    if identifier.isdigit():
      person = get_object_or_404(Person, pk=identifier) 
    else:
      person = get_object_or_404(Person, name=identifier)

    serializer = PersonSerializer(person, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def delete(self, request, identifier):
    if identifier.isdigit():
      person = get_object_or_404(Person, pk=identifier) 
    else:
      person = get_object_or_404(Person, name=identifier)

    person.delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 

# class PersonDetail(APIView):
#   def get(self, request, id):
#     person = get_object_or_404(Person, pk=id)
#     serializer = PersonSerializer(person)
#     return Response(serializer.data)
    
#   def put(self, request, id):
#     person = get_object_or_404(Person, pk=id)
#     serializer = PersonSerializer(person, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
  
#   def patch(self, request, id):
#     person = get_object_or_404(Person, pk=id)
#     serializer = PersonSerializer(person, data=request.data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)
  
#   def delete(self, request, id):
#     person = get_object_or_404(Person, pk=id)
#     person.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# # Method 1
# # method-based views
# @api_view(['POST'])
# def person_list(request):
#   if request.method == 'POST':
#     name = request.data['name']
#     person = Person.objects.filter(name=name).first()
#     if person:
#       return Response({"error": "Person already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
#     serializer = PersonSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     # serializer.validated_data
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#     # if serializer.is_valid():
#     #   serializer.validated_data
#     #   return Response('ok')
#     # else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def person_detail(request, identifier):
#   if request.method == 'POST':
#     if not identifier.isdigit():
#       person = Person.objects.filter(name=identifier).first()
#       if person:
#         return Response({"error": "Person already exists"}, status=status.HTTP_400_BAD_REQUEST)
      
#       data = {'name': identifier}
#       serializer = PersonSerializer(data=data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       # serializer.validated_data
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
  
#   if identifier.isdigit():
#       person = get_object_or_404(Person, pk=identifier) 
#   else:
#     person = get_object_or_404(Person, name=identifier)
      
#   if request.method == 'GET':
#     serializer = PersonSerializer(person)
#     return Response(serializer.data)
  
    
#   elif request.method == 'PUT':
#     serializer = PersonSerializer(person, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)
   
#   elif request.method == 'PATCH':
#     serializer = PersonSerializer(person, data=request.data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)
   
#   elif request.method == 'DELETE':
#     person.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)  
  
#   # get_object_or_404() automaticcaly implements try/catch
#   # try:
#   #   person = Person.objects.get(pk=id)
#   #   serializer = PersonSerializer(person)
#   #   return Response(serializer.data)
#   # except Person.DoesNotExist:
#   #   return Response(status=status.HTTP_404_NOT_FOUND)

# # Method 4
# # class-based views with viewset to combine Person related views
# # using routers
# class PersonViewSet(ModelViewSet):
#   # queryset = Person.objects.all()
#   def get_queryset(self):
#     if identifier.isdigit():
#       return get_object_or_404(Person, pk=identifier) 
#     else:
#       return get_object_or_404(Person, name=identifier)
  
#   serializer_class = PersonSerializer
#   lookup_field = 'identifier'


# # Method 3
# # class-based views with mixins and generic views
# class PersonList(CreateModelMixin, GenericAPIView):
#   serializer_class = PersonSerializer


# class PersonDetail(RetrieveUpdateDestroyAPIView):
#   queryset = Person.objects.all()
#   serializer_class = PersonSerializer
#   lookup_field = 'id'
  
# class PersonNameDetail(RetrieveUpdateDestroyAPIView):
#   queryset = Person.objects.all()
#   serializer_class = PersonSerializer
#   lookup_field = 'id'
 