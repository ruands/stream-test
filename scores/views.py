from rest_framework.generics import CreateAPIView

from scores.models import Score
from scores.serializers import TestScoreSerializer


class TestScoreCreateView(CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = TestScoreSerializer
