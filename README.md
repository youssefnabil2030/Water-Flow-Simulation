

# Water Flow Simulation Program

This repository contains a Python program designed to calculate water flow characteristics in a pipe system, allowing users to simulate various aspects of water pressure, flow rate, and loss within a system. The program is especially useful for understanding water distribution in systems involving water towers, pipes, and various pipe fittings.

## Features

The `water_flow.py` module provides the following core functions:

- **Water Column Height Calculation**: Calculates the height of the water column based on the elevation of the water tower and tank.
- **Pressure Gain from Water Height**: Computes the pressure gain due to water height using the density of water and gravitational acceleration.
- **Pressure Loss Due to Pipe Friction**: Estimates the pressure drop along a pipe due to factors like length, diameter, flow velocity, and material friction.
- **Pressure Loss from Fittings**: Accounts for pressure loss caused by pipe fittings (such as elbows or bends).
- **Reynolds Number Calculation**: Determines the Reynolds number to assess the flow type (laminar or turbulent) within the pipe.
- **Pressure Loss from Pipe Reduction**: Calculates pressure loss when there is a change in pipe diameter along the system.

## How It Works

The `main()` function in `water_flow.py` prompts the user for the specifications of a water distribution system, including water tower height, pipe length, diameter, velocity, and other details. Using these inputs, the program calculates and outputs the final pressure at the endpoint, such as a household outlet.

### Testing

The `test_water_flow.py` script includes unit tests for each function in `water_flow.py`, ensuring that each calculation produces accurate results within an acceptable tolerance range. The tests can be executed with the following command:

```bash
pytest -v test_water_flow.py
```

## Dependencies

- **Python 3.x**
- **pytest**: Install with `pip install pytest`

## Usage

1. Clone the repository.
2. Run `water_flow.py` to simulate a water distribution system.
3. Run `test_water_flow.py` to verify calculations with `pytest`.

This program is an ideal tool for students, engineers, and professionals looking to simulate and analyze water flow and pressure behavior in various pipe configurations.

