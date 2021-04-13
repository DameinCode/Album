from django.shortcuts import render

# Create your views here.
import json

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(company.to_json())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data['name']
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'}, status=204)

@csrf_exempt
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancy_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_json, safe=False)

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancy.to_json())


def top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def by_company(request, company_id):
    companyA = Company.objects.get(id=company_id)
    # vacancy = Vacancy.objects.all()
    vacancies = Vacancy.objects.filter(company=companyA).order_by('id')
    vacancies_json = [vacancies[vacancy].to_json() for vacancy in range(0, 9)]
    return JsonResponse(vacancies_json, safe=False)