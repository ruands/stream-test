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


class SubjectResultsView(TemplateView):
    template_name = "results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Subject.objects.get(id=kwargs.get("pk"))
        # subject_tests = Test.objects.filter()
        scores = Score.objects.filter(subject=subject)
        stats = []
        total_score = 0
        total_max = 0
        for score in scores:
            test = {
                "title": score.test.title,
                "subject": score.test.subject,
                "score": score.score,
                "max": score.test.max_score,
                "avg": score.score / score.test.max_score * 100
            }
            stats.append(test)
            total_score += score.score
            total_max += score.test.max_score
        context = {
            "subject": subject,
            "scores": stats,
            "total_avg": total_score / total_max * 100
        }
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
        total_score = 0
        total_max = 0
        for score in scores:
            test = {
                "title": score.test.title,
                "subject": score.test.subject,
                "score": score.score,
                "max": score.test.max_score,
                "avg": score.score / score.test.max_score * 100
            }
            stats.append(test)
            total_score += score.score
            total_max += score.test.max_score
        context = {
            "student": student,
            "scores": stats,
            "total_avg": total_score / total_max * 100
        }
        return context
