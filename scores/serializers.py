from rest_framework import serializers


class TestScoreSerializer(serializers.Serializer):
    score = serializers.IntegerField()
