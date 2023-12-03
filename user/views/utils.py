from rest_framework.generics import UpdateAPIView
from user.serializers import UserBlockSerializer
from rest_framework.permissions import IsAuthenticated


class UserBlockView(UpdateAPIView):
    serializer_class = UserBlockSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
