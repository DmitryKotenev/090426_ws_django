from django.shortcuts import render
from .forms import ScoringForm
import requests

# Create your views here.

TEST_DICT = {
            'job_LE' : 0,
            'marital_LE' : 1,
            'education_LE' : 2,
            'default_LE' : 3,
            'housing_LE' : 4,
            'loan_LE' : 5,
            'contact_LE' : 6,
            'month_LE' : 7,
            'poutcome_LE' : 8,
            'age' : 9,
            'balance' : 10,
            'day' : 11,
            'duration' : 12,
            'compaign' : 13,
            'pdays' : 14,
            'previous' : 15
        }

TEST_DICT2 = {
            'marital_LE' : 1,
            'job_LE' : 0,
            'education_LE' : 2,
            'previous' : 15,
            'default_LE' : 3,
            'housing_LE' : 4,
            'pdays' : 14,
            'poutcome_LE' : 8,
            'loan_LE' : 5,
            'month_LE' : 7,
            'age' : 9,
            'balance' : 10,
            'day' : 11,
            'duration' : 12,
            'contact_LE' : 6,
            'compaign' : 13,
        }

def test_prepare_data():
    print('Input Dictionary:')
    print(TEST_DICT)
    print('Output')
    print(prepare_data_from_form(TEST_DICT))

    print('Input Dictionary:')
    print(TEST_DICT2)
    print('Output')
    print(prepare_data_from_form(TEST_DICT2))

def prepare_data_from_form(data_dict):
    """
    Convert data from data_dict to list
    of these dictionary values
    with correct order.
    """

    keys_list = ['job_LE', 'marital_LE', 'education_LE', 'default_LE',
        'housing_LE', 'loan_LE', 'contact_LE', 'month_LE', 'poutcome_LE',
        'age', 'balance', 'day', 'duration', 'compaign', 'pdays', 
        'previous']

    return list(map(lambda x: data_dict[x], keys_list))

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
    #if request.method == 'POST' and scoring_form.is_valid():
    if request.method == 'POST':

        # 1. Получение данных
        scoring_form = ScoringForm(request.POST)
        scoring_form.save()
        
        #print(type(scoring_form.cleaned_data))
        #print(scoring_form.cleaned_data)
        data_dict = scoring_form.cleaned_data
        data_list = prepare_data_from_form(data_dict)
        api_message = requests.post('http://127.0.0.1:5000/api/v1/get_data',
                                    json = {'client_form': [data_list]})
        result = api_message.json()['result']
        print(result)
        

        # 2. Прогноз
        # result = get_dara -> predict() -> send_result()
        # 3. Отправка результата

    context = {'scoring_form': scoring_form, 'title': title, 'result': result}
    print(result)
    return render(request, template, context = context)