import requests

def get_pod_logs(namespace, pod_name, container_name=None, since_time=None, grep=None):
    # Set your OpenShift cluster details
    openshift_url = "https://openshift.example.com"
    token = "YOUR_OPENSHIFT_API_TOKEN"

    # Create the API endpoint URL
    api_url = f"{openshift_url}/api/v1/namespaces/{namespace}/pods/{pod_name}/log"

    # Define headers with authorization token
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    # Define query parameters
    params = {}
    if container_name:
        params["container"] = container_name
    if since_time:
        params["sinceTime"] = since_time

    try:
        # Make GET request to fetch pod logs with optional query parameters
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            # If successful, filter logs if grep is provided
            logs = response.text
            if grep:
                filtered_logs = [line for line in logs.split('\n') if grep in line]
                return '\n'.join(filtered_logs)
            else:
                return logs
        else:
            # If not successful, print error message
            print(f"Failed to fetch logs. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Handle any exceptions
        print(f"Error: {e}")
        return None

# Example usage:
namespace = "your_namespace"
pod_name = "your_pod_name"
container_name = "your_container_name"  # Optional
since_time = "your_since_time"          # Optional
grep = "AB"  # Optional, to filter logs containing "AB"
logs = get_pod_logs(namespace, pod_name, container_name, since_time, grep)
if logs:
    print("Pod Logs:")
    print(logs)
