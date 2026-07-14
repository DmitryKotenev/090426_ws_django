from django.shortcuts import render
from .forms import ScoringForm
import requests

# Create your views here.

def get_data(request):
    """ 
    Генерация страницы скоринга
    """

    template = 'scoring/index.html'
    title = 'scoring'
    result = 'no info'

    scoring_form = ScoringForm()
    # Получение из форм данных для json-шаблона 
    # после выполнения POST-запроса
    if request.method == 'POST' and scoring_form.is_valid():

        # 1. Получение данных
        scoring_form = ScoringForm(request.POST)
        scoring_form.save()

        # 2. Прогноз
        # result = get_dara -> predict() -> send_result()
        # 3. Отправка результата

    context = {'scoring_form': scoring_form, 'title': title, 'resilt': result}
    return render(request, template, context = context)