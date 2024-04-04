from kubernetes import client, config

def query_openshift_logs(pod_name, keyword):
    # Load Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client
    v1 = client.CoreV1Api()

    try:
        # Retrieve logs from the specified pod
        logs = v1.read_namespaced_pod_log(pod_name, namespace="default")

        # Search for the keyword in the logs
        keyword_count = logs.count(keyword)

        return keyword_count, logs
    except client.ApiException as e:
        print("Exception when calling CoreV1Api->read_namespaced_pod_log: %s\n" % e)

# Example usage
if __name__ == "__main__":
    pod_name = "your-pod-name"
    keyword = "your-keyword"
    count, logs = query_openshift_logs(pod_name, keyword)
    print(f"Keyword '{keyword}' found {count} times in logs:\n{logs}")
