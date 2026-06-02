from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services.agent import ask_agent, ask_agent2
from .models import ChatMessage

def index(request):
    return HttpResponse("Hello world!")



@api_view(['POST'])
def chat(request):
    message = request.data.get("message")

    if not message:
        return Response({"error": "Message is required"},status=status.HTTP_400_BAD_REQUEST)

    answer = ask_agent(message)
    # Save the user message and agent response to the database
    ChatMessage.objects.create(role="user", content=message)
    ChatMessage.objects.create(role="agent", content=answer)

    return Response({
        "reply": answer
    })

# api to ask agent about total customers and sales
@api_view(['POST'])
def chat2(request):
    message = request.data.get("message")

    if not message:
        return Response(
            {
                "success": False,
                "message": "Message is required."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        answer = ask_agent2(message)

        return Response(
            {
                "success": True,
                "reply": answer
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(
            {
                "success": False,
                "error": str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )