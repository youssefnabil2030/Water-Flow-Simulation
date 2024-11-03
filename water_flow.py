import math

# Constants
WATER_DENSITY = 998.2  # kg/m^3
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pascal seconds
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2

PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013   # unitless
SUPPLY_VELOCITY = 1.65                # meters/second
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018    # unitless
HOUSEHOLD_VELOCITY = 1.75             # meters/second

# Function to calculate water column height
def water_column_height(tower_height, tank_height):
    return tower_height + (tank_height / 2)

# Function to calculate pressure gain from water height
def pressure_gain_from_water_height(water_height):
    return WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * water_height / 1000  # Convert to kilopascals

# Function to calculate pressure loss from pipe friction
def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    return -(friction_factor * length * WATER_DENSITY * velocity**2) / (2 * diameter * 1000)  # Convert to kilopascals

# Function to calculate pressure loss from fittings
def pressure_loss_from_fittings(velocity, quantity_fittings):
    return -(0.04 * WATER_DENSITY * velocity**2 * quantity_fittings) / 2000  # Convert to kilopascals

# Function to calculate Reynolds number
def reynolds_number(hydraulic_diameter, velocity):
    return (WATER_DENSITY * hydraulic_diameter * velocity) / WATER_DYNAMIC_VISCOSITY

# Function to calculate pressure loss from pipe reduction
def pressure_loss_from_pipe_reduction(larger_diameter, velocity, reynolds_number, smaller_diameter):
    k = 0.1 + 50 / reynolds_number * (larger_diameter / smaller_diameter)**4 - 1
    return -(k * WATER_DENSITY * velocity**2) / 2000  # Convert to kilopascals

# Main function to calculate and output the pressure at the house
def main():
    try:
        tower_height = float(input("Height of water tower (meters): "))
        tank_height = float(input("Height of water tank walls (meters): "))
        length1 = float(input("Length of supply pipe from tank to lot (meters): "))
        quantity_angles = int(input("Number of 90° angles in supply pipe: "))
        length2 = float(input("Length of pipe from supply to house (meters): "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Calculate water height and pressure gain
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    
    # Pressure loss from supply pipe
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    
    # Pressure loss from fittings
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    
    # Pressure loss from pipe reduction
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    # Pressure loss from house supply pipe
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    # Display the result
    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
