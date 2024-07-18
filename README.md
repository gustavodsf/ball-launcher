# Ball Launcher Simulation

This project is a simulation software for a ball launcher. The software models the launch distances of a ball as a function of starting angle, motor torque, and ball release angle. It also allows the hardware team to test various possibilities for the motor’s torque and maximum speed to see how these values affect the ball’s maximum travel distance.

## Features

- **Simulation of Ball Launch**: Models the launch distances based on various parameters.
- **Motor Testing**: Allows testing of different motor torque and speed values.
- **Interactive Interface**: Provides a way to interact with the simulator.

## Requirements

- Python 3.x
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ball-launcher-simulation.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ball-launcher-simulation
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the simulation:
    ```sh
    python main.py
    ```
2. Follow the on-screen instructions to input parameters and view the results.


### Tests

1. Run tests with the following command:

```sh
  python3 -m unittest discover -s tests
```

## Project Structure

- `main.py`: The main script to run the simulation.
- `ball_launcher.py`: Contains the `BallLauncher` class that models the ball launcher.
- `simulator.py`: Contains the `Simulator` class that runs the simulation.
- `genetic_algorithm.py`: Contains the `GeneticAlgorithm` class to find the best parameters.
- `requirements.txt`: List of required Python packages.

## Classes

### BallLauncher

Encapsulates the properties and behavior of the ball launcher.

#### Methods

- `__init__(self, arm_length, ball_diameter, max_torque, max_speed)`: Initializes the ball launcher with given parameters.
- `launch(self, angle, torque)`: Simulates the launch of the ball and returns the distance.

### Simulator

Encapsulates the simulation process.

#### Methods

- `__init__(self, launcher)`: Initializes the simulator with a `BallLauncher` instance.
- `run_simulation(self, angles, torques)`: Runs the simulation for given angles and torques.

### GeneticAlgorithm

Encapsulates the genetic algorithm to find the best parameters.

#### Methods

- `__init__(self, simulator)`: Initializes the genetic algorithm with a `Simulator` instance.
- `optimize(self, generations, population_size)`: Runs the genetic algorithm to optimize parameters.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Thanks to the software and hardware teams for their input and requirements.
- Special thanks to the open-source community for providing the tools and libraries used in this project.

### Video
[loom video](https://www.loom.com/share/74dd6e9d6c064c8bb5a585bf350f009a?sid=fb416a37-7b48-49e2-ba50-a9c7ad063066)