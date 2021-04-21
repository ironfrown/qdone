#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020

@author: hassi
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram
from IPython.core.display import display

print("Ch 4: Three-qubit coin toss")
print("---------------------------")


qc = QuantumCircuit(3, 6)

qc.h([0,1,2])
qc.measure([0,1,2],[0,1,2])

display(qc.draw('mpl'))

backend = Aer.get_backend('qasm_simulator')

counts = execute(qc, backend, shots=1000).result().get_counts(qc)
display(plot_histogram(counts))

qc.barrier([0,1,2])
qc.reset([0,1,2])

qc.h(0)
qc.cx(0,1)
qc.cx(0,2)
qc.measure([0,1,2],[3,4,5])

display(qc.draw('mpl'))

counts = execute(qc, backend, shots=1000).result().get_counts(qc)
display(plot_histogram(counts))


