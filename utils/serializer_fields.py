from rest_framework import serializers
from django.db.models import QuerySet


class QuerySetField(serializers.ListField):
    
    def __init__(self, queryset : QuerySet, filter_field="pk", **kwargs):
        self.queryset = queryset
        self.filter_field = filter_field
        
        kwargs.setdefault(
            "child", serializers.IntegerField()
        )
        
        self.default_error_messages.update(
            {'does_not_exist': ('Object with {filter_field}={value} does not exist.')}
        )
        super().__init__(**kwargs)
        
    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        filter_kwargs = {
            f"{self.filter_field}__in" : data
        }

        queryset = self.queryset.filter(**filter_kwargs)
        
        self.validate_queryset(original_list=data, queryset=queryset)
        
        return queryset    
    
    def validate_queryset(self, original_list, queryset : QuerySet):
        unpacked_qs = {obj.id : True for obj in queryset}
        
        for i in original_list:
            try:
                unpacked_qs[i]
            except KeyError as e:
                self.fail('does_not_exist', filter_field=self.filter_field, value=i)

    def to_representation(self, data):
        return [obj.id for obj in data.all()]
