"""Create Demo Service.

Exercise 2 - insanely simple script to create a service.
"""

import kube
import yaml


with open('yaml/svc.yaml', 'r') as fd:
    data = yaml.safe_load(fd)


with kube.Cluster() as cluster:
    svc = cluster.create(data, namespace='pyconuk')
    print('Create call returned this resource:\n', svc.raw)
