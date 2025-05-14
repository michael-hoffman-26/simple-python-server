from repositories.warehouse import WarehouseRepository as ConcreteWarehouseRepository
from repositories.interfaces import IWarehouseRepository
from service.warehouse import WarehouseService


# Singleton instances
_warehouse_repository = None
_warehouse_service = None

def get_warehouse_repository() -> IWarehouseRepository:
    """
    Returns a singleton instance of the WarehouseRepository.
    This ensures we have only one repository instance across the application.
    
    Returns:
        IWarehouseRepository: The singleton repository instance
    """
    global _warehouse_repository
    if _warehouse_repository is None:
        _warehouse_repository = ConcreteWarehouseRepository()
    return _warehouse_repository

def get_warehouse_service() -> WarehouseService:
    """
    Returns a singleton instance of the WarehouseService.
    This ensures we have only one service instance across the application.
    
    Returns:
        WarehouseService: The singleton service instance
    """
    global _warehouse_service
    if _warehouse_service is None:
        _warehouse_service = create_warehouse_service(get_warehouse_repository())
    return _warehouse_service

def create_warehouse_service(repository: IWarehouseRepository) -> WarehouseService:
    """
    Factory function to create and return a WarehouseService instance.
    This allows for dependency injection and easier testing.
    
    Args:
        repository (IWarehouseRepository): The repository instance to use
        
    Returns:
        WarehouseService: A new instance of WarehouseService
    """
    return WarehouseService(repository)