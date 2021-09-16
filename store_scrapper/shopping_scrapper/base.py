from abc import ABC, abstractmethod

class BaseShoppingScrapper(ABC):
    def __init__(self, shooping_name, base_url):
        self.shooping_name = shooping_name
        self.base_url = base_url
    @abstractmethod
    def run(self) -> pd.DataFrame:
        raise NotImplementedError
    