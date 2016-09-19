"""Create pyconuk namespace.

Exercise 1 - We got a 'Failed to POST (404)' so create
required namespace .
"""

import kube
import yaml


with open('yaml/ns.yaml', 'r') as fd:
    data = yaml.safe_load(fd)


with kube.Cluster() as cluster:
    ns = cluster.create(data)  # We don't specify namespaces for namespaces!
    print('Create call returned this resource:\n', ns.raw)
