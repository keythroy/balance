from rest_framework.serializers import ModelSerializer # type: ignore
from register.models import Register

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'