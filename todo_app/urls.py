from django.urls import path, include
from .views import TodoItemViewSet, TagViewSet
from rest_framework.routers import DefaultRouter

# Register the viewsets with the router
router = DefaultRouter()
router.register(r'todoitems', TodoItemViewSet, basename='todoitem')
router.register(r'tags', TagViewSet, basename='tag')

# Manually define the URLs for the custom actions
urlpatterns = [
    path('', include(router.urls)),  # Include all routes registered in the router
    path('todoitems/<int:pk>/mark_completed/', TodoItemViewSet.as_view({'put': 'mark_completed'}), name='todoitem-mark-completed'),
    path('todoitems/<int:pk>/overdue/', TodoItemViewSet.as_view({'get': 'overdue'}), name='todoitem-overdue'),
]
