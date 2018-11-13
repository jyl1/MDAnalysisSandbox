"""This is an arbitrary module
"""

import numpy as numpy
def get_first_atom(ag):
    """Get name of first atom
    Parameters
    ----------
    ag : AtomGroup
        the atomgroup to work on
    Returns
    -------
    name : str
        the name of the first atom
    """
    return ag.names[0]