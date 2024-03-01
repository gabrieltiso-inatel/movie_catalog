from django.views import generic

from .models import Movie

class IndexView(generic.ListView):
    template_name = "movies/index.html"
    context_object_name = "movies_list"

    def get_queryset(self):
        queryset = Movie.objects.all()

        release_date = self.request.GET.get('release_date')
        if release_date:
            queryset = queryset.filter(release_date=release_date)

        director = self.request.GET.get('director')
        if director:
            queryset = queryset.filter(director__icontains=director)

        gender = self.request.GET.get('gender')
        if gender:
            queryset = queryset.filter(gender__icontains=gender)

        return queryset

