import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'mlapp/index.html')

def aboutus(request):
    return render(request,'mlapp/about.html')

def output(request):
    if request.method == 'POST':
        # Get the file from the request
        uploaded_file = request.FILES.get('file')

        if uploaded_file:
            # Send the file to the FastAPI service for processing
            response = requests.post(
                'http://localhost:5000/analyze/',  # Replace with your FastAPI URL
                files={'file': uploaded_file}
            )

            # Assuming the response contains the result in JSON format
            result = response.json()
            
            # Render the output template with the result
            return render(request, 'mlapp/output.html', {'result': result})

        else:
            # Handle case where no file is uploaded
            return HttpResponse("No file uploaded.")

    # Handle non-POST requests or redirect after processing
    return render(request, 'mlapp/index.html')
