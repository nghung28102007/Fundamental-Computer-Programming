from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.transpiler.preset_pass_managers import generate_preset_pass_manager

# 1. Map: Create a Bell State circuit (Entanglement)
qc = QuantumCircuit(2)
qc.h(0)           # Hadamard gate on qubit 0
qc.cx(0, 1)       # CNOT gate (0 is control, 1 is target)
qc.measure_all()  # Add measurements

# 2. Optimize: Prepare the circuit for the simulator
backend = AerSimulator()
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
isa_circuit = pm.run(qc)

# 3. Execute: Run the simulation
# 'shots' is the number of times the experiment is repeated
job = backend.run(isa_circuit, shots=1024)
result = job.result()

# 4. Analyze: Get the counts (bitstring results)
counts = result.get_counts()
print(f"Simulation results: {counts}")

# To see the circuit layout
qc.draw('mpl')

# To see the probability distribution
plot_histogram(counts)