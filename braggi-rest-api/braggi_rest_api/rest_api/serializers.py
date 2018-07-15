from rest_framework import serializers
from rest_api.models import Conversation

class Conv_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'username', 'user_in', 'braggi_out', 'intent', 'invoked_event')

    def create(self, validated_data):
        """
        Create and return a new `Conversation` instance, given the validated data.
        """
        return Conversation.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Conversation` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.user_in = validated_data.get('user_in', instance.user_in)
        instance.braggi_out = validated_data.get('braggi_out', instance.braggi_out)
        instance.intent = validated_data.get('intent', instance.intent)
        instance.invoked_event = validated_data.get('invoked_event', instance.invoked_event)
        instance.save()
        return instance