"""
Copyright 2017 Steven Diamond

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from cvxpy.atoms.affine.affine_atom import AffAtom
import cvxpy.lin_ops.lin_utils as lu
import numpy as np


class reshape(AffAtom):
    """ Reshapes the expression.

    Vectorizes the expression then unvectorizes it into the new shape.
    The entries are stored in column-major order.
    """

    def __init__(self, expr, rows, cols):
        self.rows = rows
        self.cols = cols
        super(reshape, self).__init__(expr)

    @AffAtom.numpy_numeric
    def numeric(self, values):
        """Reshape the value.
        """
        return np.reshape(values[0], (self.rows, self.cols), "F")

    def validate_arguments(self):
        """Checks that the new shape has the same number of entries as the old.
        """
        old_len = self.args[0].size[0]*self.args[0].size[1]
        new_len = self.rows*self.cols
        if not old_len == new_len:
            raise ValueError(
                "Invalid reshape dimensions (%i, %i)." % (self.rows, self.cols)
            )

    def size_from_args(self):
        """Returns the shape from the rows, cols arguments.
        """
        return (self.rows, self.cols)

    def get_data(self):
        """Returns info needed to reconstruct the expression besides the args.
        """
        return [self.rows, self.cols]

    @staticmethod
    def graph_implementation(arg_objs, size, data=None):
        """Convolve two vectors.

        Parameters
        ----------
        arg_objs : list
            LinExpr for each argument.
        size : tuple
            The size of the resulting expression.
        data :
            Additional data required by the atom.

        Returns
        -------
        tuple
            (LinOp for objective, list of constraints)
        """
        return (lu.reshape(arg_objs[0], size), [])