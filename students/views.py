from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import AllowAny



from django.shortcuts import render

def home_view(request):
    return render(request, 'login.html')

from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(user)

    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    })

class StudentListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/students/   → list all students
    POST /api/students/   → create a new student
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': queryset.count(),
            'results': serializer.data   # ✅ FIX HERE
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Student created', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )



class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/students/<id>/  → get one student
    PUT    /api/students/<id>/  → full update
    PATCH  /api/students/<id>/  → partial update
    DELETE /api/students/<id>/  → delete
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Student updated', 'data': serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        student_id = instance.id
        instance.delete()
        return Response({'message': f'Student {student_id} deleted'}, status=status.HTTP_200_OK)