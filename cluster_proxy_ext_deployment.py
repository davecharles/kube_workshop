"""Demonstrate proxy usage.

Exercise 3 - Get deployment resource from the K8s extensions API.
"""

import kube


with kube.Cluster() as cluster:
    deployment_raw = cluster.proxy.get(
        '..', '..', 'apis', 'extensions', 'v1beta1', 'namespaces',
        'default', 'deployments', 'hello-minikube')
    print('Raw deployment resource data:\n', deployment_raw)
