import requests

def get_pods(api_url, token, namespace):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"{api_url}/api/v1/namespaces/{namespace}/pods"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        pods_info = response.json()
        pod_names = [item["metadata"]["name"] for item in pods_info["items"]]
        return pod_names
    else:
        print(f"Failed to retrieve pod names. Status code: {response.status_code}")
        return None

# Example usage:
api_url = "https://your.openshift.api.url"
token = "your_token"
namespace = "your_namespace"
pod_names = get_pods(api_url, token, namespace)
if pod_names:
    print("Pod names in the namespace:")
    for name in pod_names:
        print(name)
