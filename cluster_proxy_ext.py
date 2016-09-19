"""Demonstrate proxy usage.

Exercise 3 - Get resources from the K8s extensions API.

Note that luckily, we can instance our ReplicaSetItem because
they're kind of the same.

Also note that we have to use a relative path.
"""

import kube


with kube.Cluster() as cluster:
    real_rs_raw = cluster.proxy.get(
        '..', '..', 'apis', 'extensions', 'v1beta1', 'namespaces',
        'default', 'replicasets', 'hello-minikube-2433534028')
    rs = kube.ReplicaSetItem(cluster, real_rs_raw)
    print('Using proxy we got the resource called \'{}\' '
          'which was created on \'{}\''.format(
              rs.meta.name, rs.meta.created.strftime('%A')))
