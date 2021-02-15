from django.views.generic import ListView, TemplateView

from scores.models import Student, Subject, Score, Test


class DashView(TemplateView):
    template_name = "dash.html"


class TestResultsListView(ListView):
    model = Test
    template_name = "dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Test"
        context["tests"] = Test.objects.all()
        return context



class SubjectResultsListView(ListView):
    model = Subject
    template_name = "dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Subject"
        context["subjects"] = Subject.objects.all()
        return context


class StudentResultsListView(ListView):
    model = Student
    template_name = "dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Student"
        context["students"] = Student.objects.all()
        return context


class StudentResultsView(TemplateView):
    template_name = "results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(id=kwargs.get("pk"))
        scores = Score.objects.filter(student=student)
        stats = []
        for score in scores:
            test = {
                "title": score.test.title,
                "subject": score.test.subject,
                "score": score.score,
                "max": score.test.max_score,
                "avg": score.score / score.test.max_score
            }
            stats.append(score)
        context = {
            "student": student,
            "scores": stats
        }
        return context
