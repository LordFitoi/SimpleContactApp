from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sheet', 'category']
    
    def create(self, request, *args, **kwargs):
        request.data["created_by"] = self.request.user 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        self.perform_create(serializer)
        return super().create(self, request, *args, **kwargs)

