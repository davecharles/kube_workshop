"""Create Demo Replication Controller.

Exercise 1 - insanely simple script to create a replication controller.
"""

import kube
import yaml


with open('yaml/rc.yaml', 'r') as fd:
    data = yaml.safe_load(fd)


with kube.Cluster() as cluster:
    rc = cluster.create(data, namespace='pyconuk')
    print('Create call returned this resource:\n', rc.raw)
