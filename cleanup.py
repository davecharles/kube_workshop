"""Clean up Demo resources.

Exercise 6 -  Calls delete method on the namespace resource.  This will
cause K8s to mop up *all* resources in that namespace.  All of them.
Maybe don't do this on `default` or `production` for example.

By the way, it can take time for K8s to clean up so running this multiple
times might not raise an exception - even though you called delete.
Notice the delete method's idempotency in this case - that's deliberate.
"""

import kube


with kube.Cluster() as cluster:
    try:
        ns = cluster.namespaces.fetch('pyconuk')
    except LookupError as e:
        print('Poof - \'tis already gone!')
    else:
        print('Cleaning up everything in Namespace:', ns.meta.name)
        ns.delete()
