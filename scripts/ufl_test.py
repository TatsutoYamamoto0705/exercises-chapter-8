import ufl
argyris = ufl.FiniteElement("Argyris", degree=6, cell=ufl.triangle)

def test_symmetric_group_operation():
    assert argyris == ufl.FiniteElement("Argyris", degree=6, cell=ufl.triangle)
