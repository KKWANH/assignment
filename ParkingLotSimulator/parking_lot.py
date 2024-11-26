class ParkingZone:
    def __init__(self, zone_id, capacity):
        self.zone_id = zone_id
        self.capacity = capacity
        self.slots = [None] * capacity

    def find_empty_slot(self):
        for index, slot in enumerate(self.slots):
            if slot is None:
                return index
        return -1

    def park_vehicle(self, vehicle):
        slot_index = self.find_empty_slot()
        if slot_index != -1:
            self.slots[slot_index] = vehicle
            return True
        return False

    def release_vehicle(self, vehicle_id):
        for index, slot in enumerate(self.slots):
            if slot is not None and slot.vehicle_id == vehicle_id:
                self.slots[index] = None
                return True
        return False

class ParkingLot:
    def __init__(self, num_zones, slots_per_zone):
        self.zones = [ParkingZone(zone_id, slots_per_zone) for zone_id in range(num_zones)]

    def find_best_zone(self):
        return max(self.zones, key=lambda zone: zone.slots.count(None))

    def park_vehicle(self, vehicle):
        best_zone = self.find_best_zone()
        return best_zone.park_vehicle(vehicle)

    def release_vehicle(self, vehicle_id):
        for zone in self.zones:
            if zone.release_vehicle(vehicle_id):
                return True
        return False
