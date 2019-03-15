# -*- coding: utf-8 -*-
# Python function that creates a simple, two qubit quantum cirquit and sets up and measures a Bell, or entangled, state.

# Start by importing and simplifying required modules. 
from sense_hat import SenseHat
hat = SenseHat()

# Define the execute function that is called by the main controller.
def execute():
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
    from qiskit import execute
    import numpy as np
    #Set number of bits and number of shots
    n = 2
    print(n)
    sh = 1024
    # Create a Quantum Register with n qubits
    qr = QuantumRegister(n)
    # Create a Classical Register with n bits
    cr = ClassicalRegister(n)
    # Create a Quantum Circuit acting on the qr and cr register
    circuit = QuantumCircuit(qr, cr)
    # Add gates to the circuit
    circuit.h(qr[0])
    circuit.cx(qr[0], qr[1])
    circuit.measure(qr[0], cr[0])
    circuit.measure(qr[1], cr[1])
    # Set the backend to execute on
    from qiskit import BasicAer
    backend = BasicAer.get_backend('qasm_simulator'
    # Create a Quantum Program for execution of the circuit on the selected backend
    job = execute(circuit, backend, shots=sh)
    # Get the result of the execution
    result = job.result()
    # Provide the results
    print ("Results:")
    #print (result)
    Qdictres = result.get_counts(circuit)
    print(Qdictres)
    
    # Import the Raspberry PI SenseHat display function.
    from qc_sensehat_func import SenseDisplay
    # Display the quantum dictionary as a bar graph on the SenseHat 8x8 pixel display by calling the SenseDisplay function.
    SenseDisplay(Qdictres,n)
