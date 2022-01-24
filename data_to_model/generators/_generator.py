from abc import ABC, abstractmethod


class Generator(ABC):
    """
    Base class for data class generators
    """

    @abstractmethod
    def generate_file_content(self) -> str:
        pass
