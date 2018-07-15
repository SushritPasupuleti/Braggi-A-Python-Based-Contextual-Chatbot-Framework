from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_api.models import Conversation
from rest_api.serializers import Conv_Serializer
from rest_api import linker
import json

@api_view(['GET', 'POST'])
def conversation_list(request):
    """
    List all conversations, or create a new conversation.
    """
    if request.method == 'GET':
        conversations = Conversation.objects.all()
        serializer = Conv_Serializer(conversations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        req_data = linker.parse_input(request.data)

        serializer = Conv_Serializer(data=req_data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def conversation_detail(request, pk):
    """
    Retrieve, update or delete a conversation.
    """
    try:
        conversation = Conversation.objects.get(pk=pk)
    except Conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Conv_Serializer(conversation)
        return Response("serializer.data")

    elif request.method == 'PUT':
        serializer = Conv_Serializer(conversation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        conversation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
