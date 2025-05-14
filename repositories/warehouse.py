from datetime import datetime, date
from typing import Dict, List, Optional
from repositories.interfaces import IWarehouseRepository

class WarehouseRepository(IWarehouseRepository):
    def __init__(self):
        # Simulating in-memory databases for trucks and packages
        self._trucks: Dict[int, dict] = {}
        self._packages: Dict[int, dict] = {}
        print("WarehouseRepository initialized")

    def _validate_dimensions(self, length: float, width: float, height: float) -> bool:
        """Validate that all dimensions are positive numbers"""
        return length > 0 and width > 0 and height > 0

    def create_truck(self, truck_data: dict) -> int:
        """Create a new truck"""
        # Validate dimensions
        if not self._validate_dimensions(truck_data.get('length', 0), 
                                       truck_data.get('width', 0), 
                                       truck_data.get('height', 0)):
            raise ValueError("All dimensions must be positive numbers")

        # Validate delivery_day
        if 'delivery_day' not in truck_data or not isinstance(truck_data['delivery_day'], date):
            raise ValueError("delivery_day is required and must be a date object")

        truck_id = len(self._trucks) + 1
        truck_data['id'] = truck_id
        truck_data['created_at'] = datetime.now()
        truck_data['fill_percentage'] = 0.0  # Initialize fill percentage to 0
        self._trucks[truck_id] = truck_data
        print(f"Creating truck with data: {truck_data}")
        return truck_id

    def get_truck(self, truck_id: int) -> dict:
        """Get a truck by ID"""
        print(f"Fetching truck with ID: {truck_id}")
        return self._trucks.get(truck_id)

    def get_all_trucks(self) -> list:
        """Get all trucks"""
        print("Fetching all trucks")
        return list(self._trucks.values())

    def update_truck(self, truck_id: int, truck_data: dict) -> bool:
        """Update a truck"""
        if truck_id in self._trucks:
            # Validate dimensions if they are being updated
            if any(dim in truck_data for dim in ['length', 'width', 'height']):
                current_data = self._trucks[truck_id]
                length = truck_data.get('length', current_data['length'])
                width = truck_data.get('width', current_data['width'])
                height = truck_data.get('height', current_data['height'])
                if not self._validate_dimensions(length, width, height):
                    raise ValueError("All dimensions must be positive numbers")

            # Validate fill_percentage if it's being updated
            if 'fill_percentage' in truck_data:
                fill = truck_data['fill_percentage']
                if not 0 <= fill <= 100:
                    raise ValueError("Fill percentage must be between 0 and 100")

            print(f"Updating truck {truck_id} with data: {truck_data}")
            self._trucks[truck_id].update(truck_data)
            return True
        return False

    def delete_truck(self, truck_id: int) -> bool:
        """Delete a truck"""
        if truck_id in self._trucks:
            print(f"Deleting truck with ID: {truck_id}")
            del self._trucks[truck_id]
            return True
        return False

    def create_package(self, length: float, width: float, height: float, truck_id: Optional[int] = None) -> int:
        """Create a new package"""
        # Validate dimensions
        if not self._validate_dimensions(length, width, height):
            raise ValueError("All dimensions must be positive numbers")

        # Validate truck_id if provided
        if truck_id is not None and truck_id not in self._trucks:
            raise ValueError(f"Truck with ID {truck_id} does not exist")

        package_id = len(self._packages) + 1
        package_data = {
            'id': package_id,
            'length': length,
            'width': width,
            'height': height,
            'truck_id': truck_id,
            'created_at': datetime.now()
        }
        self._packages[package_id] = package_data
        print(f"Creating package with data: {package_data}")
        return package_id

    def get_package(self, package_id: int) -> dict:
        """Get a package by ID"""
        print(f"Fetching package with ID: {package_id}")
        return self._packages.get(package_id)

    def get_all_packages(self) -> list:
        """Get all packages"""
        print("Fetching all packages")
        return list(self._packages.values())

    def get_packages_by_truck(self, truck_id: int) -> list:
        """Get all packages assigned to a specific truck"""
        print(f"Fetching packages for truck ID: {truck_id}")
        return [pkg for pkg in self._packages.values() if pkg['truck_id'] == truck_id]

    def update_package(self, package_id: int, package_data: dict) -> bool:
        """Update a package"""
        if package_id in self._packages:
            print(f"Updating package {package_id} with data: {package_data}")
            self._packages[package_id].update(package_data)
            return True
        return False

    def delete_package(self, package_id: int) -> bool:
        """Delete a package"""
        if package_id in self._packages:
            print(f"Deleting package with ID: {package_id}")
            del self._packages[package_id]
            return True
        return False

    def calculate_truck_volume(self, truck_id: int) -> float:
        """Calculate the total volume of a truck"""
        truck = self.get_truck(truck_id)
        if truck:
            return truck['length'] * truck['width'] * truck['height']
        return 0.0

    def calculate_package_volume(self, package_id: int) -> float:
        """Calculate the volume of a package"""
        package = self.get_package(package_id)
        if package:
            return package['length'] * package['width'] * package['height']
        return 0.0

    def update_truck_fill_percentage(self, truck_id: int) -> bool:
        """Update the fill percentage of a truck based on its assigned packages"""
        truck = self.get_truck(truck_id)
        if not truck:
            return False

        truck_volume = self.calculate_truck_volume(truck_id)
        if truck_volume == 0:
            return False

        packages = self.get_packages_by_truck(truck_id)
        total_package_volume = sum(self.calculate_package_volume(pkg['id']) for pkg in packages)
        
        fill_percentage = (total_package_volume / truck_volume) * 100
        return self.update_truck(truck_id, {'fill_percentage': fill_percentage}) 