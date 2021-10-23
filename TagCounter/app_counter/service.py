from rest_framework.response import Response


def not_found():
    return Response({'response': 'Not Found'})
