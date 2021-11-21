#!/usr/bin/env python3

from ortools.linear_solver import pywraplp


def mip_hello_world():
    # mip solver with SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')

    x = solver.IntVar(0.0, solver.infinity(), 'x')
    y = solver.IntVar(0.0, solver.infinity(), 'y')
    z = solver.IntVar(0.0, solver.infinity(), 'z')

    # 2*x + 7*y + 3*z <= 50
    constraint0 = solver.Constraint(-solver.infinity(), 50)
    constraint0.SetCoefficient(x, 2)
    constraint0.SetCoefficient(y, 7)
    constraint0.SetCoefficient(z, 3)

    # Maximize 2*x + 2*y + 3*z
    objective = solver.Objective()
    objective.SetCoefficient(x, 2)
    objective.SetCoefficient(y, 2)
    objective.SetCoefficient(z, 3)
    objective.SetMaximization()

    solver.Solve()

    print(f'Maximum objective function value = {solver.Objective().Value()}')
    print()

    for variable in [x, y, z]:
        print(f'{variable.name()} = {variable.solution_value()}')

    return {var.solution_value() for var in [x, y, z]}


if __name__ == '__main__':
    mip_hello_world()
