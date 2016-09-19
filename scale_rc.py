"""Demonstrate Replication Controller scaling.

Exercise 4 - Use the cluster proxy to scale an RC.
"""

import kube


new_spec = {
    'kind': 'Scale',
    'apiVersion': 'autoscaling/v1',
    'spec': {
        'replicas': 20
    },
    'metadata': {
        'name': 'kube-echo',
        'namespace': 'pyconuk'
    }
}

with kube.Cluster() as cluster:
    rs_raw = cluster.proxy.patch(
        'namespaces', 'pyconuk', 'replicationcontrollers', 'kube-echo',
        'scale', patch=new_spec)
    replicas = 0
    while replicas < 20:
        replicas = cluster.replicasets.fetch(
            'kube-echo', namespace='pyconuk').fully_labeled_replicas
    print('RC scaled up to:', replicas)
