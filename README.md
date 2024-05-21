# Traffic Flow Optimization using Reinforcement Learning

This repository contains the implementation of a dynamic traffic light control system using Deep Q-Networks (DQN) to optimize traffic flow and reduce congestion. The project simulates and evaluates the performance of the RL-based system in various traffic scenarios.

## Steps to Run the Code

### Requirements

- [SUMO (Simulation of Urban MObility)](https://www.eclipse.org/sumo/)
- Python 3.6+
- Required Python packages (listed in `requirements.txt`)

### Installation

1. **Install SUMO:** Follow the instructions on the [SUMO website](https://www.eclipse.org/sumo/) to install SUMO and configure it on your system.

2. **Clone the repository:**
   ```bash
   git clone git@github.com:ayogenthiran/traffic-flow-optimization.git
   cd traffic-flow-optimization
   
Install Python dependencies:
pip install -r requirements.txt

Running the Simulation
You can run the SUMO simulation with different step lengths using the following commands:

1. Run SUMO with a step length of 0.1:

      sumo-gui -c sumo_config.sumocfg --step-length 0.1

2. Run SUMO with a step length of 0.05:

      sumo-gui -c sumo_config.sumocfg --step-length 0.05

3. Run SUMO with a step length of 0.01:

      sumo-gui -c sumo_config.sumocfg --step-length 0.01


Training and Testing the Model

1. Train the model:

      python training_main.py

2. Test the model:

      python testing_main.py

Report
For detailed information about the project, including the methodology, results, and analysis, please refer to the following documents:

   Project Proposal
   
   Final Report
