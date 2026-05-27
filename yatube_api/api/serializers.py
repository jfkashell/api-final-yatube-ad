from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, following):
        user = self.context['request'].user
        if user == following:
            raise serializers.ValidationError(
                'Self-follow is not allowed.'
            )
        return following

    def validate(self, attrs):
        user = self.context['request'].user
        following = attrs['following']
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                'Follow already exists.'
            )
        return attrs
