class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def __str__(self):
        return f"Vehicle({self.vehicle_id})"