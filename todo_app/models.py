from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

# Create your models here.
class Tag(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Custom primary key
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # Custom primary key
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    # Fields
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-set on creation
    title = models.CharField(max_length=100)  # Mandatory, user editable
    description = models.TextField(max_length=1000)  # Mandatory, user editable
    due_date = models.DateField(null=True, blank=True)  # Optional
    tags = models.ManyToManyField(Tag, blank=True)  # Optional, many-to-many
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )  # Mandatory with default value

    # Validation
    def clean(self):
        # Prevent due_date from being in the past if provided
        if self.due_date and self.due_date < now().date():
            raise ValidationError("Due date cannot be in the past.")

    # Automatically set overdue status
    def save(self, *args, **kwargs):
        if self.due_date and self.due_date < now().date() and self.status not in ['COMPLETED', 'CANCELLED']:
            self.status = 'OVERDUE'
        super().save(*args, **kwargs)

    # String representation
    def __str__(self):
        return self.title

    # Meta options
    class Meta:
        ordering = ['due_date', 'timestamp']

    # Optionally convert timestamp to local time in the model
    @property
    def local_timestamp(self):
        return self.timestamp.astimezone(now().timezone)
