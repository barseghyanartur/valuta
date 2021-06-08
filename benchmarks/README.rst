Benchmarks
==========
To have a quick view on `valuta` only calls:

.. code-block:: sh

    pycallgraph --include="valuta.*"  graphviz -- benchmarks/profile.py

Helper scripts are available as well. Most of the benchmarks are distributed
through functions. It's possible to choose which function to call.

**python_classes**

.. code-block:: sh

    ./scripts/benchmark.sh --func='python_classes'


**python_iso_string_representation**

.. code-block:: sh

    ./scripts/benchmark.sh --func='python_iso_string_representation'
