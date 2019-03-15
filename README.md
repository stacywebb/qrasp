# Two and three qubit Qiskit user interface on Raspberry PI


Python scripts creating two or three qubit quantum circuits and displaying results as bar graphs on a Raspberry PI 3.


![qrasp_3qubit_GHZ.jpg](qrasp_3qubit_GHZ.jpg)


## Requirements  

- Hardware
   - Raspberry PI 3
   - Raspberry Pi Sense HAT
   
- Software
  - Python 3 (2.7 should work)
  
- Installation (Required Software)
  - ```sudo apt-get install sense-hat```
  - ```sudo pip3 install qiskit==0.7.1```
  - ```git clone https://github.com/stacywebb/qrasp/qrasp.git```


## Usage

- python3 main_controller.py

## Contents

- Scripts
   - main_controller.py  - Main Loading Script


- Quantum program scripts
   
   - q2_calling_sense_func.py - creates two qubit quantum circuit and measures each qubit in a superposition state.
   
   
    ```
                      ┌───┐┌─┐
     q0_0: |0>────────┤ H ├┤M├
              ┌───┐┌─┐└───┘└╥┘
     q0_1: |0>┤ H ├┤M├──────╫─
              └───┘└╥┘      ║
      c0_0: 0 ══════╬═══════╩═
                    ║         
      c0_1: 0 ══════╩═════════
     ```
   
   
   - q3_calling_sense_func.py - creates a three qubit quantum circuit and measures each qubit in a superposition state.
   
   
     ```
                              ┌───┐┌─┐
     q1_0: |0>────────────────┤ H ├┤M├
                      ┌───┐┌─┐└───┘└╥┘
     q1_1: |0>────────┤ H ├┤M├──────╫─
              ┌───┐┌─┐└───┘└╥┘      ║
     q1_2: |0>┤ H ├┤M├──────╫───────╫─
              └───┘└╥┘      ║       ║
      c1_0: 0 ══════╬═══════╬═══════╩═
                    ║       ║         
      c1_1: 0 ══════╬═══════╩═════════
                    ║                 
      c1_2: 0 ══════╩═════════════════
     ```
   
   
   - bell_calling_sense_func.py - creates a two qubit quantum circuit and measures a Bell, or entangled, state.
   
   
     ```
              ┌───┐        ┌─┐
     q2_0: |0>┤ H ├──■─────┤M├
              └───┘┌─┴─┐┌─┐└╥┘
     q2_1: |0>─────┤ X ├┤M├─╫─
                   └───┘└╥┘ ║
      c2_0: 0 ═══════════╬══╩═
                         ║    
      c2_1: 0 ═══════════╩════
     ```
     
     
   - GHZ_calling_sense_func.py - creates a three qubit quantum circuit and measures an entangled GHZ state.
   
   
     ```
                                     ┌───┐             ┌───┐┌─┐
     q3_0: |0>───────────────────────┤ H ├──■──────────┤ H ├┤M├
                   ┌───┐     ┌───┐┌─┐└───┘  │          └───┘└╥┘
     q3_1: |0>─────┤ H ├──■──┤ H ├┤M├───────┼────────────────╫─
              ┌───┐└───┘┌─┴─┐└───┘└╥┘     ┌─┴─┐┌───┐┌─┐      ║
     q3_2: |0>┤ X ├─────┤ X ├──────╫──────┤ X ├┤ H ├┤M├──────╫─
              └───┘     └───┘      ║      └───┘└───┘└╥┘      ║
      c3_0: 0 ═════════════════════╬═════════════════╬═══════╩═
                                   ║                 ║         
      c3_1: 0 ═════════════════════╩═════════════════╬═════════
                                                     ║         
      c3_2: 0 ═══════════════════════════════════════╩═════════
     ```
     
     
   - qc_sensehat_func.py - utilizes SenseHat 8x8 display to show bar graph of 2 or 3 qubit Qiskit results dictionaries.


### Usage (Physical interaction)

The four quantum scripts demostrate superposition and entanglement with two and three qubits.

 - Using the joystick (on the SenseHat) select the script to run:
 
 ```
   Up: Two qubit Bell state (entanglement)
   Down: Three qubit GHZ state (entanglement)
   Right: Three qubit superposition
   Left: Two qubit superposition
```

Quantum circuits currently run on the qasm_simulator backend.
