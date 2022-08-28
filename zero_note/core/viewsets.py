from requests import delete
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactSerializer
from .firebase import database

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        queryset = []
        objects = database.child("contacts").get().val()
        
        if objects:
            for item in objects:
                if objects[item]["created_by"] == request.user.id:
                    queryset.append(
                        { **objects[item], "id": item }
                    )

        return Response(queryset)

    def destroy(self, request, *args, **kwargs):
        database.child("contacts").child(kwargs["pk"]).remove()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        data['created_by'] = request.user.id
        pk = database.child("contacts").push(data).get("name")
        instance_data = {
            **database.child("contacts").child(pk).get().val(),
            "id": pk,
        }

        return Response(instance_data, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        database.child("contacts").child(pk).update(request.data)
        instance_data = {
            **database.child("contacts").child(pk).get().val(),
            "id": pk,
        }

        return Response(instance_data)