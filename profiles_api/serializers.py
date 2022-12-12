from rest_framework import serializers
from profiles_api import models



class HelloSerializer(serializers.Serializer):
    """Serializa un campo para probar nuestra Api view"""
    name = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
    """serializa objeto de perfil de usuario"""

    class Meta:
        model = models.userProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


    def create(self, validated_data):
        """crear y retornar nuevo usuario"""
        user = models.userProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            
        )
        
        return user

    def update(self, instance, validated_data):
        """actualiza cuenta de usuario"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)


        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """esto es el serializador de profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only':True} }