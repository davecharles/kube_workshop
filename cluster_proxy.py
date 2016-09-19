"""Demonstrate proxy usage.

Exercise 3 - Get our demo replication controller using the cluster proxy.
We also instance a resource item from the raw data.
"""

import kube


with kube.Cluster() as cluster:
    rs_raw = cluster.proxy.get(
        'namespaces', 'pyconuk', 'replicationcontrollers', 'kube-echo')
    rs = kube.ReplicaSetItem(cluster, rs_raw)
    print('Using proxy we got the resource called \'{}\' '
          'which was created on \'{}\''.format(
              rs.meta.name, rs.meta.created.strftime('%A')))
