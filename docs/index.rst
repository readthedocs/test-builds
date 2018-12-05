auto-wipe
=========

When a project changes its

* version of Python or
* Docker image name or
* Docker image hash

the environment has to be Auto-Wiped before building the new documentation.

To QA this branch, you have to change ``build: image:`` and/or ``python: version:``
from ``.readthedocs.yml`` file and commit it.

The new documentation built should match the values you set in the YAML file
in the following output:


.. runblock:: pycon

   >>> # Python Version used
   >>> import sys
   >>> print(sys.version)


.. runblock:: pycon

   >>> import os
   >>> import pprint
   >>> import json
   >>> filepath = '../../../envs/{version}/readthedocs-environment.json'.format(version=os.environ['READTHEDOCS_VERSION'])
   >>> pprint.pprint(json.loads(open(filepath, 'r').read()))


.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
