from rest_framework import serializers
from .models import TodoItem, Tag
from django.utils.timezone import localtime

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TodoItemSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False)
    timestamp = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TodoItem
        fields = ['id', 'timestamp', 'title', 'description', 'due_date', 'tags', 'status']

    def get_timestamp(self, obj):
        return localtime(obj.timestamp).strftime('%Y-%m-%dT%H:%M:%S%z')

    def validate_status(self, value):
        """Ensure that the status is one of the valid choices"""
        if value not in dict(TodoItem.STATUS_CHOICES):
            raise serializers.ValidationError(f"{value} is not a valid choice.")
        return value

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        todo_item = TodoItem.objects.create(**validated_data)

        for tag in tags_data:
            todo_item.tags.add(tag)

        return todo_item

    def update(self, instance, validated_data):
        # Check if 'timestamp' is included in the update data
        if 'timestamp' in validated_data:
            raise ValidationError({'timestamp': 'Timestamp cannot be edited.'})

        tags_data = validated_data.pop('tags', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.tags.clear()
        for tag in tags_data:
            instance.tags.add(tag)

        return instance
