from queue_manager import QueueManager
from parking_lot import ParkingLot

class ParkingManager:
    def __init__(self, parking_lot, queue_manager):
        self.parking_lot = parking_lot
        self.queue_manager = queue_manager

    def add_vehicle(self, vehicle):
        if not self.parking_lot.park_vehicle(vehicle):
            self.queue_manager.add_to_queue(vehicle)

    def process_queue(self):
        while not self.queue_manager.is_empty():
            vehicle = self.queue_manager.peek_queue()
            if self.parking_lot.park_vehicle(vehicle):
                self.queue_manager.remove_from_queue()

    def release_vehicle(self, vehicle_id):
        if not self.parking_lot.release_vehicle(vehicle_id):
            print(f"Vehicle {vehicle_id} is not found in the parking lot.")
