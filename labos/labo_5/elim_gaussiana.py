#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""

import numpy as np


def elim_gaussiana(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, int]:
    cant_op = 0
    m, n = A.shape
    Ac = A.copy()

    if m != n:
        print("Matriz no cuadrada")
        return

    ## desde aqui -- CODIGO A COMPLETAR

    for i in range(m):
        for j in range(i + 1, n):
            factor = Ac[j, i] / Ac[i, i]
            Ac[j, i:] = Ac[j, i:] - factor * Ac[i, i:]
            Ac[j, i] = factor

            cant_op += 2  # DIVISION Y ASIGNACION
            cant_op += n - i  # RESTAS

    # hasta aqui

    L = np.tril(Ac, -1) + np.eye(A.shape[0])
    U = np.triu(Ac)

    return L, U, cant_op


def main():
    n = 7
    B = np.eye(n) - np.tril(np.ones((n, n)), -1)
    B[:n, n - 1] = 1
    print("Matriz B \n", B)

    L, U, cant_oper = elim_gaussiana(B)

    print("Matriz L \n", L)
    print("Matriz U \n", U)
    print("Cantidad de operaciones: ", cant_oper)
    print("B=LU? ", "Si!" if np.allclose(np.linalg.norm(B - L @ U, 1), 0) else "No!")
    print("Norma infinito de U: ", np.max(np.sum(np.abs(U), axis=1)))


if __name__ == "__main__":
    main()
