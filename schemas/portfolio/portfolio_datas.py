from datetime import datetime
from sqlalchemy import Column, Integer, Numeric, ForeignKey, String, Enum, DateTime, Boolean
from config.db.database import Base
from sqlalchemy.orm import relationship
from models.portfolio.portfolio_datas import TagDatasPortfolio


class PortfolioDatasSchema(Base):
    __tablename__: str = 'port_datas'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id', onupdate='CASCADE'), nullable=False)
    name = Column(String(100), nullable=False)
    tag: TagDatasPortfolio = Column(Enum(TagDatasPortfolio))
    installment = Column(Integer, nullable=True)
    value = Column(Numeric(18, 2), nullable=False)
    expiration_day = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    is_recurring = Column(Boolean, nullable=False, default=False)

    user = relationship('UserSchema')


class PortfolioDatasMapped(PortfolioDatasSchema):
    pass
