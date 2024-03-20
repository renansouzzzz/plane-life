from sqlalchemy import Column, Integer, Numeric, ForeignKey, String, Enum
from config.database import Base
from sqlalchemy.orm import relationship
from models.portfolio_datas import TagDatasPortfolio
    

class PortfolioDatasSchema(Base):
    __tablename__ = 'port_datas'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    tag: TagDatasPortfolio = Column(Enum(TagDatasPortfolio))
    installment = Column(Integer, nullable=False)
    value = Column(Numeric(18,2), nullable=False)
    
    portfolio = relationship('PortfolioSchema')

    
class PortfolioDatasMapped(PortfolioDatasSchema):
    pass