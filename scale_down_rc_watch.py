"""Demonstrate Replication Controller scaling.

Exercise 4 - Use the cluster proxy to scale an RC.
"""

import kube
import time


def watch(item):
    with item.watch() as watcher:
        deadline = time.monotonic() + 1
        while time.monotonic() < deadline:
            try:
                update = watcher.next(timeout=0.2)
            except TimeoutError:
                continue
            except StopIteration:
                print('Exhausted')
            else:
                print('Replicas:', update.item.fully_labeled_replicas)


new_spec = {
    'kind': 'Scale',
    'apiVersion': 'autoscaling/v1',
    'spec': {
        'replicas': 1
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
    rs = cluster.replicasets.fetch('kube-echo', namespace='pyconuk')
    while rs.fully_labeled_replicas > 1:
        watch(rs)
        rs = cluster.replicasets.fetch('kube-echo', namespace='pyconuk')
    print('Done')
