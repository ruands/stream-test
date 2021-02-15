from rest_framework import serializers


class TestScoreSerializer(serializers.Serializer):
    test_id = serializers.IntegerField()
    scores = serializers.JSONField()
