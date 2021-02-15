from django.views.generic import ListView, TemplateView

from scores.models import Student


class DashView(TemplateView):
    template_name = "dash.html"


class TestResultsView(ListView):
    pass


class SubjectResultsView(ListView):
    pass


class StudentResultsView(ListView):
    model = Student
    template_name = "dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Student"
        context["students"] = Student.objects.all()
        return context
