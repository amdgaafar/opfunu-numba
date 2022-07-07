#!/usr/bin/env python
# Created by "Thieu" at 14:45, 07/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import numpy as np
from opfunu.cec_based.cec import CecBenchmark
from opfunu.utils import operator


class F12015(CecBenchmark):
    """
    .. [1] Chen, Q., Liu, B., Zhang, Q., Liang, J., Suganthan, P., & Qu, B. (2014). Problem definitions and evaluation criteria for CEC 2015
    special session on bound constrained single-objective computationally expensive numerical optimization. Technical Report,
    Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou, China and Technical Report, Nanyang Technological University.
    """
    name = "F1: Rotated Bent Cigar Function"
    latex_formula = r'F_1(x) = \sum_{i=1}^D z_i^2 + bias, z=x-o,\\ x=[x_1, ..., x_D]; o=[o_1, ..., o_D]: \text{the shifted global optimum}'
    latex_formula_dimension = r'2 <= D <= 100'
    latex_formula_bounds = r'x_i \in [-100.0, 100.0], \forall i \in  [1, D]'
    latex_formula_global_optimum = r'\text{Global optimum: } x^* = o, F_1(x^*) = bias = 100.0'

    continuous = True
    linear = False
    convex = True
    unimodal = True
    separable = False

    differentiable = True
    scalable = True
    randomized_term = False
    parametric = True
    shifted = True
    rotated = True

    modality = False  # Number of ambiguous peaks, unknown # peaks
    # n_basins = 1
    # n_valleys = 1

    characteristics = ["Smooth but narrow ridge"]

    def __init__(self, ndim=None, bounds=None, f_shift="shift_data_1_D", f_matrix="M_1_D", f_bias=100.):
        super().__init__()
        self.dim_changeable = True
        self.dim_default = 10
        self.dim_max = 30
        self.dim_supported = [10, 30]
        self.check_ndim_and_bounds(ndim, self.dim_max, bounds, np.array([[-100., 100.] for _ in range(self.dim_default)]))
        self.make_support_data_path("data_2015")
        self.f_shift = self.check_matrix_data(f_shift, needed_dim=True).ravel()
        self.f_matrix = self.check_matrix_data(f_matrix, needed_dim=True)
        self.f_bias = f_bias
        self.f_global = f_bias
        self.x_global = self.f_shift
        self.paras = {"f_shift": self.f_shift, "f_bias": self.f_bias, "f_matrix": self.f_matrix}

    def evaluate(self, x, *args):
        self.n_fe += 1
        self.check_solution(x, self.dim_max, self.dim_supported)
        z = np.dot(self.f_matrix, x - self.f_shift)
        return operator.bent_cigar_func(z) + self.f_bias


class F22015(F12015):
    """
    .. [1] Chen, Q., Liu, B., Zhang, Q., Liang, J., Suganthan, P., & Qu, B. (2014). Problem definitions and evaluation criteria for CEC 2015
    special session on bound constrained single-objective computationally expensive numerical optimization. Technical Report,
    Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou, China and Technical Report, Nanyang Technological University.
    """
    name = "F2: Rotated Discus Function"
    latex_formula = r'F_1(x) = \sum_{i=1}^D z_i^2 + bias, z=x-o,\\ x=[x_1, ..., x_D]; o=[o_1, ..., o_D]: \text{the shifted global optimum}'
    latex_formula_dimension = r'2 <= D <= 100'
    latex_formula_bounds = r'x_i \in [-100.0, 100.0], \forall i \in  [1, D]'
    latex_formula_global_optimum = r'\text{Global optimum: } x^* = o, F_1(x^*) = bias = 200.0'

    characteristics = ["With one sensitive direction"]

    def __init__(self, ndim=None, bounds=None, f_shift="shift_data_2_D", f_matrix="M_2_D", f_bias=200.):
        super().__init__(ndim, bounds, f_shift, f_matrix, f_bias)

    def evaluate(self, x, *args):
        self.n_fe += 1
        self.check_solution(x, self.dim_max, self.dim_supported)
        z = np.dot(self.f_matrix, x - self.f_shift)
        return operator.discus_func(z) + self.f_bias


class F32015(F12015):
    """
    .. [1] Chen, Q., Liu, B., Zhang, Q., Liang, J., Suganthan, P., & Qu, B. (2014). Problem definitions and evaluation criteria for CEC 2015
    special session on bound constrained single-objective computationally expensive numerical optimization. Technical Report,
    Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou, China and Technical Report, Nanyang Technological University.
    """
    name = "F3: Shifted and Rotated Weierstrass Function"
    latex_formula = r'F_1(x) = \sum_{i=1}^D z_i^2 + bias, z=x-o,\\ x=[x_1, ..., x_D]; o=[o_1, ..., o_D]: \text{the shifted global optimum}'
    latex_formula_dimension = r'2 <= D <= 100'
    latex_formula_bounds = r'x_i \in [-100.0, 100.0], \forall i \in  [1, D]'
    latex_formula_global_optimum = r'\text{Global optimum: } x^* = o, F_1(x^*) = bias = 300.0'

    convex = False
    unimodal = False

    characteristics = ["Continuous but differentiable only on a set of points"]

    def __init__(self, ndim=None, bounds=None, f_shift="shift_data_3_D", f_matrix="M_3_D", f_bias=300.):
        super().__init__(ndim, bounds, f_shift, f_matrix, f_bias)

    def evaluate(self, x, *args):
        self.n_fe += 1
        self.check_solution(x, self.dim_max, self.dim_supported)
        z = np.dot(self.f_matrix, 0.5*(x - self.f_shift)/100)
        return operator.weierstrass_func(z) + self.f_bias


class F42015(F12015):
    """
    .. [1] Chen, Q., Liu, B., Zhang, Q., Liang, J., Suganthan, P., & Qu, B. (2014). Problem definitions and evaluation criteria for CEC 2015
    special session on bound constrained single-objective computationally expensive numerical optimization. Technical Report,
    Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou, China and Technical Report, Nanyang Technological University.
    """
    name = "F4: Shifted and Rotated Schwefel’s Function"
    latex_formula = r'F_1(x) = \sum_{i=1}^D z_i^2 + bias, z=x-o,\\ x=[x_1, ..., x_D]; o=[o_1, ..., o_D]: \text{the shifted global optimum}'
    latex_formula_dimension = r'2 <= D <= 100'
    latex_formula_bounds = r'x_i \in [-100.0, 100.0], \forall i \in  [1, D]'
    latex_formula_global_optimum = r'\text{Global optimum: } x^* = o, F_1(x^*) = bias = 400.0'

    convex = False
    unimodal = False
    modality = True

    characteristics = ["Local optima’s number is huge",  "The second better local optimum is far from the global optimum"]

    def __init__(self, ndim=None, bounds=None, f_shift="shift_data_4_D", f_matrix="M_4_D", f_bias=400.):
        super().__init__(ndim, bounds, f_shift, f_matrix, f_bias)

    def evaluate(self, x, *args):
        self.n_fe += 1
        self.check_solution(x, self.dim_max, self.dim_supported)
        z = np.dot(self.f_matrix, 1000*(x - self.f_shift)/100)
        return operator.modified_schwefel_func(z) + self.f_bias


class F52015(F12015):
    """
    .. [1] Chen, Q., Liu, B., Zhang, Q., Liang, J., Suganthan, P., & Qu, B. (2014). Problem definitions and evaluation criteria for CEC 2015
    special session on bound constrained single-objective computationally expensive numerical optimization. Technical Report,
    Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou, China and Technical Report, Nanyang Technological University.
    """
    name = "F5: Shifted and Rotated Katsuura Function"
    latex_formula = r'F_1(x) = \sum_{i=1}^D z_i^2 + bias, z=x-o,\\ x=[x_1, ..., x_D]; o=[o_1, ..., o_D]: \text{the shifted global optimum}'
    latex_formula_dimension = r'2 <= D <= 100'
    latex_formula_bounds = r'x_i \in [-100.0, 100.0], \forall i \in  [1, D]'
    latex_formula_global_optimum = r'\text{Global optimum: } x^* = o, F_1(x^*) = bias = 500.0'

    convex = False
    unimodal = False
    differentiable = False
    modality = True

    characteristics = ["Continuous everywhere yet differentiable nowhere"]

    def __init__(self, ndim=None, bounds=None, f_shift="shift_data_5_D", f_matrix="M_5_D", f_bias=500.):
        super().__init__(ndim, bounds, f_shift, f_matrix, f_bias)

    def evaluate(self, x, *args):
        self.n_fe += 1
        self.check_solution(x, self.dim_max, self.dim_supported)
        z = np.dot(self.f_matrix, 5*(x - self.f_shift)/100)
        return operator.katsuura_func(z) + self.f_bias


class F62015(F12015):
    """
    .. [1] Chen, Q., Liu, B., Zhang, Q., Liang, J., Suganthan, P., & Qu, B. (2014). Problem definitions and evaluation criteria for CEC 2015
    special session on bound constrained single-objective computationally expensive numerical optimization. Technical Report,
    Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou, China and Technical Report, Nanyang Technological University.
    """
    name = "F6: Shifted and Rotated HappyCat Function"
    latex_formula = r'F_1(x) = \sum_{i=1}^D z_i^2 + bias, z=x-o,\\ x=[x_1, ..., x_D]; o=[o_1, ..., o_D]: \text{the shifted global optimum}'
    latex_formula_dimension = r'2 <= D <= 100'
    latex_formula_bounds = r'x_i \in [-100.0, 100.0], \forall i \in  [1, D]'
    latex_formula_global_optimum = r'\text{Global optimum: } x^* = o, F_1(x^*) = bias = 600.0'

    convex = False
    unimodal = False
    separable = False
    differentiable = False

    characteristics = ["Continuous everywhere yet differentiable nowhere"]

    def __init__(self, ndim=None, bounds=None, f_shift="shift_data_6_D", f_matrix="M_6_D", f_bias=600.):
        super().__init__(ndim, bounds, f_shift, f_matrix, f_bias)

    def evaluate(self, x, *args):
        self.n_fe += 1
        self.check_solution(x, self.dim_max, self.dim_supported)
        z = np.dot(self.f_matrix, 5*(x - self.f_shift)/100)
        return operator.happy_cat_func(z) + self.f_bias






