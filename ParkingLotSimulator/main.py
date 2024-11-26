from parking_lot import ParkingLot
from vehicle import Vehicle
from parking_manager import ParkingManager
from queue_manager import QueueManager

def main():
    # Create Parking Lot
    parking_lot = ParkingLot(num_zones=3, slots_per_zone=10)
    queue_manager = QueueManager()
    parking_manager = ParkingManager(parking_lot, queue_manager)
    
    # 예시 차량 생성
    vehicle1 = Vehicle("1234AB")
    vehicle2 = Vehicle("5678CD")
    
    # 차량 입장 및 대기열 관리
    parking_manager.add_vehicle(vehicle1)
    parking_manager.add_vehicle(vehicle2)
    
    # 시뮬레이션 진행
    parking_manager.process_queue()
    parking_manager.release_vehicle("1234AB")

if __name__ == "__main__":
    main()
