from .models import Scoring
from django.contrib import admin

# Register your models here.

class ScoringAdmin(admin.ModelAdmin):
    list_display = ('job_LE', 'marital_LE', 'education_LE', 'default_LE',
            'housing_LE', 'loan_LE', 'contact_LE', 'month_LE', 'poutcome_LE', 'age', 'balance',
            'day', 'duration', 'compaign', 'pdays', 'previous')
    search_fields = ("")
    list_filter = ("")

admin.site.register(Scoring)