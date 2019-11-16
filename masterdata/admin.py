from django.contrib import admin
from masterdata.models import Movie,Profile,MovieFeedback,Donor

class MovieAdmin(admin.ModelAdmin):
    list_display = ('m_name','d_name','actor','movie_id','budget')


admin.site.register(Movie,MovieAdmin)
admin.site.register(Profile)
admin.site.register(MovieFeedback)
admin.site.register(Donor)