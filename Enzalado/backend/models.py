from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.sql import func
from database import Base


class CartItem(Base):
    """Modelo para items en el carrito de compras"""
    __tablename__ = "cart_items"
    
    id = Column(Integer, primary_key=True, index=True)
    user_session = Column(String, index=True, nullable=False)  # Identificador de sesión del usuario
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class ContactMessage(Base):
    """Modelo para mensajes de contacto"""
    __tablename__ = "contact_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class OrderHistory(Base):
    """Modelo para historial de órdenes"""
    __tablename__ = "order_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_session = Column(String, index=True, nullable=False)
    customer_name = Column(String, nullable=False)
    customer_email = Column(String, nullable=False)
    customer_phone = Column(String, nullable=True)
    total_amount = Column(Float, nullable=False)
    status = Column(String, default="pending")  # pending, completed, cancelled
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
