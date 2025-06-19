SPARC-SSV
=========

A collection of tutorials in the form of iPython Jupyter notebooks, detailing how to work with SPARC vagus scaffolds and data.

Required environment
--------------------

Python version 3.7+ for which jupyter and cmlibs.zinc are available on https://pypi.org.

.. list-table:: Required Python Packages
   :widths: 15 25 50
   :header-rows: 1

   * - Package
     - Installation
     - More info
   * - jupyter
     - pip install jupyter
     - https://jupyter-notebook.readthedocs.io/en/latest/
   * - cmlibs.zinc
     - pip install cmlibs.zinc
     - Zinc Library for Finite Element model representation and visualization. API documentation is at: https://cmlibs.org/documentation.
   * - cmlibs.utils
     - pip install cmlibs.utils
     - Python support utilities for using with Zinc.
   * - cmlibs.maths
     - pip install cmlibs.maths
     - Useful mathematical functions for working with Zinc in Python.
   * - ssvtools
     - pip install ssvtools
     - High-level tools for querying and transforming vagus scaffolds. https://github.com/ABI-Software/ssvtools


Running the tutorials
---------------------

1. At the command line in the top folder of this downloaded repository, with your python environment activated, enter::

    jupyter notebook

2. The above should open a window in your default browser. Click on and run through the notebook files, in suggested order:

    1_introduction_ssv_scaffolds.ipynb
    2_query_structure.ipynb

More details on using jupyter notebooks can be found at https://docs.jupyter.org/en/latest/running.html
