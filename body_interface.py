from abc import ABC, abstractmethod

class BodyInterface(ABC):
    @abstractmethod
    async def connect(self):
        """Connect to the visual display software."""
        pass

    @abstractmethod
    async def trigger_expression(self, expression_name: str):
        """Trigger an emotion/expression by name."""
        pass

    @abstractmethod
    async def close(self):
        """Clean up connection."""
        pass