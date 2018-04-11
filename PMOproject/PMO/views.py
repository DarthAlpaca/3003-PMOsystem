from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Case
from .serializers import CaseSerializer
from django.urls import reverse
from rest_framework import generics

# Create your views here.

def index(request):
	latest_case_list = Case.objects.order_by('-created_time')[:10]
	context = {'latest_case_list':latest_case_list}
	
	return render(request, 'PMO/caseindex.html' , context)


def authorise(request, case_id):
	case = get_object_or_404(Case, pk = case_id)
	try:
		approved=request.POST['approved']
		comment = request.POST['comment']
		if approved=="approve":
			authorise = True
		elif approved == "reject":
			authorise = False
		
		
	except (KeyError):
		return render(request, 'PMO/detail.html',{
			'case':case,
			'error_message' : "you did not select a choice.",
		})
	else:
		case.approved =  authorise
		case.comment = comment
		case.save()
		
		return HttpResponseRedirect(reverse('PMO:index'))
		
	
def detail(request, case_id):
	case = get_object_or_404(Case, pk = case_id)
	return render(request,'PMO/detail.html',{'case':case})
	
class CaseList(generics.ListCreateAPIView):
	queryset = Case.objects.all()
	serializer_class = CaseSerializer
	
class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Case.objects.all()
	serializer_class = CaseSerializer
		
@api_view(['GET'])
def api_root(reqeust, format = None):
	return Response({
		'cases':reverse('case_list', request = request, format = format)
	})