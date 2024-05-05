import random

def generate_sensor_data():
    # List of predefined colors for sensor signals
    sensor_colors = [
        "#FF5733",  # Orange
        "#3498DB",  # Blue
        "#9B59B6",  # Purple
        "#E74C3C",  # Red
        "#F39C12",  # Yellow
        "#C0392B",  # Dark Red
        "#2ECC71",  # Green
        "#1ABC9C",  # Turquoise
        "#7F8C8D",  # Gray
        "#34495E",  # Dark Gray
        "#E67E22",  # Carrot
        "#D35400",  # Pumpkin
        "#27AE60",  # Nephritis
        "#16A085",  # Green Sea
        "#2980B9",  # Belize Hole
        "#8E44AD",  # Wisteria
        "#2C3E50"   # Midnight Blue
    ]

    # List of 30 different drone types
    drone_types = [
        "Type A",
        "Type B",
        "Type C",
        "Type D",
        "Type E",
        "Type F",
        "Type G",
        "Type H",
        "Type I",
        "Type J",
        "Type K",
        "Type L",
        "Type M",
        "Type N",
        "Type O",
        "Type P",
        "Type Q",
        "Type R",
        "Type S",
        "Type T",
        "Type U",
        "Type V",
        "Type W",
        "Type X",
        "Type Y",
        "Type Z",
        "Type AA",
        "Type BB",
        "Type CC"
    ]

    # Dictionary to store drone details
    drones = {}

    # Generate random colors for each drone's sensors
    for drone_type in drone_types:
        for drone_id in range(1, 101):  # 100 drones
            sensor_color = random.choice(sensor_colors)
            drones[f"{drone_type} - {drone_id}"] = sensor_color
    output=""
    # Example: Printing colors for the first 5 drones
    for drone, color in list(drones.items()):
        output += f" {drone}: {color} "

    color_combinations = {
        "Low battery warning": "#FF5733",  # Orange
        "High winds detected": "#3498DB",  # Blue
        "GPS signal lost": "#9B59B6",  # Purple
        "Obstacle detected in flight path": "#E74C3C",  # Red
        "Drone malfunction": "#F39C12",  # Yellow
        "Emergency landing required": "#C0392B",  # Dark Red
        "Change in flight plan due to airspace restrictions": "#2ECC71",  # Green
        "Communication signal lost with remote controller": "#1ABC9C",  # Turquoise
        "Payload release malfunction": "#7F8C8D",  # Gray
        "Weather conditions deteriorating": "#34495E",  # Dark Gray
        "Bird strike": "#E67E22",  # Carrot
        "Motor failure": "#D35400",  # Pumpkin
        "Propeller damage": "#27AE60",  # Nephritis
        "Collision with a stationary object": "#16A085",  # Green Sea
        "Navigation system failure": "#2980B9",  # Belize Hole
        "Loss of altitude control": "#8E44AD",  # Wisteria
        "Sudden change in temperature": "#2C3E50",  # Midnight Blue
        "Flight range exceeded": "#9B59B6",  # Amethyst
        "Restricted flight zone entered": "#D35400",  # Pumpkin
        "Mechanical failure in landing gear": "#E74C3C"  # Alizarin
    }

    return output,color_combinations
