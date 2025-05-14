from repositories.warehouse import WarehouseRepository
from repositories.interfaces import IWarehouseRepository

def create_warehouse_repository() -> IWarehouseRepository:
    """
    Factory function to create and return a WarehouseRepository instance.
    This allows for dependency injection and easier testing.
    
    Returns:
        IWarehouseRepository: A new instance of WarehouseRepository implementing the interface
    """
    return WarehouseRepository()