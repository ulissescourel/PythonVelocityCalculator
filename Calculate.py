import math

def projectile_motion(v0, theta_deg):
    # Constants
    g = 9.8  # Acceleration due to gravity (m/s²)
    k = 0.1  # Air resistance coefficient (kg/m)

    # Convert angle from degrees to radians
    theta_rad = math.radians(theta_deg)

    # Initial velocity components
    v0x = v0 * math.cos(theta_rad)
    v0y = v0 * math.sin(theta_rad)

    # Calculate maximum height
    h_max = (v0y**2) / (2 * g)

    # Calculate total time of flight
    t_total = (2 * v0y) / g

    # Calculate horizontal range
    R = (v0x * t_total) - (k * t_total**2 / 2)

    return h_max, t_total, R

# Example usage
initial_velocity = 30  # m/s
launch_angle = 45  # degrees
max_height, time_of_flight, range_distance = projectile_motion(initial_velocity, launch_angle)

print(f"Maximum height: {max_height:.2f} meters")
print(f"Total time of flight: {time_of_flight:.2f} seconds")
print(f"Horizontal range: {range_distance:.2f} meters")