from flask import request
from typing import Dict, List, Optional, Any, Union
from repositories.warehouse import WarehouseRepository

class WarehouseService:
    def __init__(self, warehouse_repository: WarehouseRepository) -> None:
        self.warehouse_repository = warehouse_repository

    def create_truck(self, truck_data: Dict[str, Any]) -> int:
        return self.warehouse_repository.create_truck(truck_data)

    def get_truck(self, truck_id: int) -> Optional[Dict[str, Any]]:
        return self.warehouse_repository.get_truck(truck_id)

    def get_all_trucks(self) -> List[Dict[str, Any]]:
        return self.warehouse_repository.get_all_trucks()

    def update_truck(self, truck_id: int, truck_data: Dict[str, Any]) -> bool:
        return self.warehouse_repository.update_truck(truck_id, truck_data)

    def delete_truck(self, truck_id: int) -> bool:
        return self.warehouse_repository.delete_truck(truck_id)

    def assign_trucks(self, packages_ids: List[int]) -> bool:
        """
        Assign packages to trucks based on available space and delivery day.
        Returns True if all packages were successfully assigned, False otherwise.
        """
        try:
            # Get all available trucks
            trucks = self.warehouse_repository.get_all_trucks()
            if not trucks:
                return False

            # Sort trucks by fill percentage (ascending) to fill trucks evenly
            trucks.sort(key=lambda x: x.get('fill_percentage', 0))

            # Get all packages
            packages = [self.warehouse_repository.get_package(pid) for pid in packages_ids]
            if not all(packages):
                return False

            # Try to assign each package to a truck
            for package in packages:
                package_volume = self.warehouse_repository.calculate_package_volume(package['id'])
                assigned = False

                for truck in trucks:
                    truck_volume = self.warehouse_repository.calculate_truck_volume(truck['id'])
                    current_fill = truck.get('fill_percentage', 0)
                    
                    # Check if package can fit in truck
                    if (current_fill + (package_volume / truck_volume * 100)) <= 100:
                        # Update package with truck_id
                        self.warehouse_repository.update_package(package['id'], {'truck_id': truck['id']})
                        # Update truck's fill percentage
                        self.warehouse_repository.update_truck_fill_percentage(truck['id'])
                        assigned = True
                        break

                if not assigned:
                    return False  # Couldn't assign all packages

            return True
        except Exception as e:
            print(f"Error assigning trucks: {str(e)}")
            return False 