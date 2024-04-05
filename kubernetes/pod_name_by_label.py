import requests

def get_pods(api_url, token, namespace, label_selector):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "labelSelector": label_selector
    }
    url = f"{api_url}/api/v1/namespaces/{namespace}/pods"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        pods_info = response.json()
        return pods_info["items"]
    else:
        print(f"Failed to retrieve pod names. Status code: {response.status_code}")
        return None

# Example usage:
api_url = "https://your.openshift.api.url"
token = "your_token"
namespace = "your_namespace"
container_name = "your_container_name"

label_selector = f"app={container_name}"  # Assuming the container name is also the label
pods = get_pods(api_url, token, namespace, label_selector)
if pods:
    print("Pods in the namespace containing the specified container:")
    for pod in pods:
        print(pod["metadata"]["name"])
else:
    print(f"No pods found in the namespace containing container '{container_name}'")
