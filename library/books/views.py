from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from books.helpers import *
from books.models import Books, Members


# Create your views here.
@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        data = request.body
        data_dict = json.loads(data.decode("utf-8"))

        if is_book_available(data_dict.get('book_id')) and not is_book_allocated(data_dict.get('book_id'), data_dict.get('member_id')):

            registerCirculationEvent(data_dict, ACTION_CHECKOUT)
            updateBooks(data_dict['book_id'], ACTION_CHECKOUT)

            return HttpResponse(
                json.dumps({"response": "Book allocated"}), 
                content_type="application/json")
    
        else:
            return HttpResponse(
                json.dumps({"response": "Book not available"}), 
                content_type="application/json")
    else:
        return HttpResponseBadRequest("Bad Request")



@csrf_exempt
def return_book(request):
    if request.method == 'POST':
        data = request.body
        data_dict = json.loads(data.decode("utf-8"))

        registerCirculationEvent(data_dict, ACTION_RETURN)
        updateBooks(data_dict['book_id'], ACTION_RETURN)

        return HttpResponse(
            json.dumps({"response": "Book returned"}), 
            content_type="application/json")

    else:
        return HttpResponseBadRequest("Bad Request")



@csrf_exempt
def overdues(request):
    if request.method == 'GET':
        data = request.GET.dict()
        response = get_overdues_data(data.get('member_id'))
        return HttpResponse(
            json.dumps(response), 
            content_type="application/json")

    else:
        return HttpResponseBadRequest("Bad Request")

