import time

class Drone:
    def __init__(self):
        self.battery_level = 100
        self.collision_warning = False
        self.payload_deployed = False
        self.weather_conditions = "Clear"
        self.navigation_error = False
        self.system_health = "Normal"
        self.security_breach = False
        self.geofence_violation = False
        self.emergency_response = False
        self.obstacle_detected = False
        self.payload_malfunction = False
        self.communication_loss = False
        self.flight_terminated = False

    def send_low_battery_warning(self):
        if self.battery_level < 20:
            message = "Low Battery Warning: Battery level is critically low. Return to base for recharging."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def send_emergency_stop(self):
        message = "Emergency Stop: Critical issue detected. Halting all operations."
        hashed_message = hashing.hash_message(message)
        print("Original message:", message)
        print("Hashed message:", hashed_message)

    def send_collision_warning(self):
        if self.collision_warning:
            message = "Collision Warning: Obstacle detected. Take evasive action."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def execute_flight_plan(self):
        message = "Flight Plan Execution: Initiating flight plan execution."
        hashed_message = hashing.hash_message(message)
        print("Original message:", message)
        print("Hashed message:", hashed_message)

    def send_weather_conditions(self):
        message = f"Weather Conditions: {self.weather_conditions}"
        hashed_message = hashing.hash_message(message)
        print("Original message:", message)
        print("Hashed message:", hashed_message)

    def send_navigation_error(self):
        if self.navigation_error:
            message = "Navigation Error: Deviating from planned route. Requesting assistance."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def send_system_health(self):
        message = f"System Health: {self.system_health}"
        hashed_message = hashing.hash_message(message)
        print("Original message:", message)
        print("Hashed message:", hashed_message)

    def send_security_breach(self):
        if self.security_breach:
            message = "Security Breach: Unauthorized access detected. Taking security measures."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def send_geofence_violation(self):
        if self.geofence_violation:
            message = "Geofence Violation: Drone is approaching restricted area."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def send_emergency_response(self):
        if self.emergency_response:
            message = "Emergency Response: Sending real-time updates on emergency situation."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def send_obstacle_detection(self):
        if self.obstacle_detected:
            message = "Obstacle Detection: Unexpected obstacle detected."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def send_payload_malfunction(self):
        if self.payload_malfunction:
            message = "Payload Malfunction: Payload is malfunctioning. Requesting troubleshooting."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def send_communication_loss(self):
        if self.communication_loss:
            message = "Communication Loss: Lost connection with ground control."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

    def send_flight_termination(self):
        if self.flight_terminated:
            message = "Flight Termination: Mission completed. Initiating landing procedure."
            hashed_message = hashing.hash_message(message)
            print("Original message:", message)
            print("Hashed message:", hashed_message)

# Create Drone instance
drone = Drone()

# Example usage - Triggering various scenarios
drone.battery_level = 15
drone.send_low_battery_warning()

drone.collision_warning = True
drone.send_collision_warning()

drone.execute_flight_plan()

drone.weather_conditions = "Rainy"
drone.send_weather_conditions()

drone.navigation_error = True
drone.send_navigation_error()

drone.system_health = "Degraded"
drone.send_system_health()

drone.security_breach = True
drone.send_security_breach()

drone.geofence_violation = True
drone.send_geofence_violation()

drone.emergency_response = True
drone.send_emergency_response()

drone.obstacle_detected = True
drone.send_obstacle_detection()

drone.payload_malfunction = True
drone.send_payload_malfunction()

drone.communication_loss = True
drone.send_communication_loss()

drone.flight_terminated = True
drone.send_flight_termination()