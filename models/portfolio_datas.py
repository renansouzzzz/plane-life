from datetime import datetime
from pydantic import BaseModel, Field

from enum import Enum

class TagDatasPortfolio(Enum):
    RendaMensal = 0
    DespesasMensais = 1
    DividasRecorrentes = 2
    DividasEmAtraso = 3

class PortfolioDatas(BaseModel):
    name: str = Field(..., max_length=50)
    created_at: datetime = Field(default_factory=datetime.now)
    id_user: int
    value: float
    tag: TagDatasPortfolio
    installment: int
    
    
class PortfolioDatasCreate(PortfolioDatas):
    pass

class PortfolioDatasUpdate(PortfolioDatas):
    pass