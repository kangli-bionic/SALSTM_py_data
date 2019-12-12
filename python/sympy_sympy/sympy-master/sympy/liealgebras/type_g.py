# -*- coding: utf-8 -*-

from .cartan_type import Standard_Cartan
from sympy.matrices import Matrix

class TypeG(Standard_Cartan):

    def __new__(cls, n):
        if n != 2:
            raise ValueError("n should be 2")
        return Standard_Cartan.__new__(cls, "G", 2)


    def dimension(self):
        """Dimension of the vector space V underlying the Lie algebra

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("G2")
        >>> c.dimension()
        3
        """
        return 3

    def simple_root(self, i):
        """The ith simple root of G_2

        Every lie algebra has a unique root system.
        Given a root system Q, there is a subset of the
        roots such that an element of Q is called a
        simple root if it cannot be written as the sum
        of two elements in Q.  If we let D denote the
        set of simple roots, then it is clear that every
        element of Q can be written as a linear combination
        of elements of D with all coefficients non-negative.

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("G2")
        >>> c.simple_root(1)
        [0, 1, -1]

        """
        if i == 1:
            return [0, 1, -1]
        else:
            return [1, -2, 1]

    def positive_roots(self):
        """Generate all the positive roots of A_n

        This is half of all of the roots of A_n; by multiplying all the
        positive roots by -1 we get the negative roots.

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("A3")
        >>> c.positive_roots()
        {1: [1, -1, 0, 0], 2: [1, 0, -1, 0], 3: [1, 0, 0, -1], 4: [0, 1, -1, 0],
                5: [0, 1, 0, -1], 6: [0, 0, 1, -1]}

        """

        roots = {1: [0, 1, -1], 2: [1, -2, 1], 3: [1, -1, 0], 4: [1, 0, 1],
                5: [1, 1, -2], 6: [2, -1, -1]}
        return roots

    def roots(self):
        """
        Returns the total number of roots of G_2"
        """
        return 12

    def cartan_matrix(self):
        """The Cartan matrix for G_2

        The Cartan matrix matrix for a Lie algebra is
        generated by assigning an ordering to the simple
        roots, (alpha[1], ...., alpha[l]).  Then the ijth
        entry of the Cartan matrix is (<alpha[i],alpha[j]>).

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("G2")
        >>> c.cartan_matrix()
        Matrix([
            [ 2, -1],
            [-3,  2]])

        """

        m = Matrix( 2, 2, [2, -1, -3, 2])
        return m

    def basis(self):
        """
        Returns the number of independent generators of G_2
        """
        return 14

    def dynkin_diagram(self):
        diag = "0≡<≡0\n1   2"
        return diag