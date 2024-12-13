from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TodoItem, Tag
from .serializers import TodoItemSerializer, TagSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['put'])
    def mark_completed(self, request, pk=None):
        todo_item = self.get_object()
        todo_item.status = 'COMPLETED'
        todo_item.save()
        return Response({"status": "completed"}, status=200)

    @action(detail=True, methods=['get'])
    def overdue(self, request, pk=None):
        todo_item = self.get_object()
        if todo_item.due_date < timezone.now().date():
            return Response({"status": "overdue"}, status=200)
        return Response({"status": "not overdue"}, status=200)