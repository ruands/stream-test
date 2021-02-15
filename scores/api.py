from django.db.utils import IntegrityError

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from scores.models import Score, Student, Subject, Test
from scores.serializers import TestScoreSerializer


class TestScoreCreateView(CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = TestScoreSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Serializer confirms these fields are present, no need to do .get()
            test_id = serializer.validated_data["test_id"]
            scores = serializer.validated_data["scores"]

            # Get Test object and Subject object to limit the lookup of Student objects
            test = Test.objects.get(id=test_id)
            test_subject = Subject.objects.get(id=test.subject.id)

            for score in scores:
                # Keys might be missing, do a .get() that returns None if the key is not present.
                student_id = score.get("student_id")
                test_score = score.get("score")
                
                student = test_subject.students.filter(id=student_id).first()

                try:
                    _score = Score.objects.create(
                        test=test,
                        student=student,
                        score=test_score
                    )
                except IntegrityError:
                    return Response(status=400, data=f"Score for student: {student_id} could not be captured.")

            return Response(status=201, data="Scores created")
        return Response(status=400, data=serializer.errors)
