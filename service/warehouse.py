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