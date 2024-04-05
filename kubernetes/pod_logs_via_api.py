import requests

def get_pod_logs(api_url, token, namespace, pod_name):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"{api_url}/api/v1/namespaces/{namespace}/pods/{pod_name}/log"
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve logs. Status code: {response.status_code}")
        return None

# Example usage:
api_url = "https://your.openshift.api.url"
token = "your_token"
namespace = "your_namespace"
pod_name = "your_pod_name"
logs = get_pod_logs(api_url, token, namespace, pod_name)
if logs:
    print(logs)
