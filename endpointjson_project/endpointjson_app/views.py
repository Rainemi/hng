from django.views.decorators.http import require_GET
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
@require_GET
def Get_info(request):
    # Get query parameters from the request
    slack_name = request.GET.get('slack_name', 'Raine')
    track = request.GET.get('track', 'backend')

    # Get the current day of the week and UTC time
    current_day = datetime.utcnow().strftime('%A')
    current_utc_time = datetime.utcnow().isoformat(timespec='seconds')+ 'Z'


    # Get the GitHub URL of the file being run
    github_repo_url = 'https://github.com/Rainemi/hng'

    # Get the GitHub URL of the full source code (replace with your repository URL)
    github_file_url = 'https://github.com/Rainemi/hng/blob/main/endpointjson_project/endpointjson_app/views.py'

    # Create a dictionary to hold the response data
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200  # Success status code
    }

    return JsonResponse(response_data)



