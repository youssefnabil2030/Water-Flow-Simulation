import pytest
from pytest import approx
from water_flow import (
    water_column_height, pressure_gain_from_water_height, 
    pressure_loss_from_pipe, pressure_loss_from_fittings, 
    reynolds_number, pressure_loss_from_pipe_reduction
)

# Constants for the tests
WATER_DENSITY = 998.2  # kg/m^3
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pascal seconds
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2

PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013   # unitless
SUPPLY_VELOCITY = 1.65                # meters/second
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018    # unitless
HOUSEHOLD_VELOCITY = 1.75             # meters/second

def test_water_column_height():
    assert water_column_height(36.6, 9.1) == approx(41.15)
    assert water_column_height(50.0, 20.0) == approx(60.0)
    assert water_column_height(0, 10.0) == approx(5.0)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(41.15) == approx(402.7, rel=0.1)  # Adjust relative tolerance for real-world accuracy
    assert pressure_gain_from_water_height(60.0) == approx(588.5, rel=0.1)
    assert pressure_gain_from_water_height(5.0) == approx(49.0, rel=0.1)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.28687, 1524.0, 0.013, 1.65) == approx(-206.1, rel=0.1)
    assert pressure_loss_from_pipe(0.048692, 15.2, 0.018, 1.75) == approx(-7.8, rel=0.1)
    assert pressure_loss_from_pipe(0.1, 100.0, 0.015, 2.0) == approx(-11.98, rel=0.1)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(1.65, 3) == approx(-0.2, rel=0.1)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.24, rel=0.1)
    assert pressure_loss_from_fittings(2.0, 5) == approx(-0.5, rel=0.1)

def test_reynolds_number():
    assert reynolds_number(0.28687, 1.65) == approx(472826, rel=0.1)
    assert reynolds_number(0.048692, 1.75) == approx(86094, rel=0.1)
    assert reynolds_number(0.1, 2.0) == approx(199640, rel=0.1)

def test_pressure_loss_from_pipe_reduction():
    reynolds = reynolds_number(PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY)
    assert pressure_loss_from_pipe_reduction(PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY, reynolds, HDPE_SDR11_INNER_DIAMETER) == approx(-5.8, rel=0.1)
    reynolds = reynolds_number(0.1, 2.0)
    assert pressure_loss_from_pipe_reduction(0.1, 2.0, reynolds, 0.05) == approx(-7.0, rel=0.1)
    reynolds = reynolds_number(0.5, 2.0)
    assert pressure_loss_from_pipe_reduction(0.5, 2.0, reynolds, 0.25) == approx(-7.7, rel=0.1)

# No need for pytest.main() call when run using pytest CLI
