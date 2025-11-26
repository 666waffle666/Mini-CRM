from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapped_column, Mapped

Base = declarative_base()


class Operator(Base):
    __tablename__ = "operators"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    max_load: Mapped[int] = mapped_column(Integer)

    contacts = relationship("Contact", back_populates="operator")
    configs = relationship("SourceConfig", back_populates="operator")


class Lead(Base):
    __tablename__ = "leads"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    external_id: Mapped[str] = mapped_column(String, unique=True, index=True)

    contacts = relationship("Contact", back_populates="lead")


class Source(Base):
    __tablename__ = "sources"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)

    contacts = relationship("Contact", back_populates="source")
    configs = relationship("SourceConfig", back_populates="source")


class SourceConfig(Base):
    __tablename__ = "source_configs"
    source_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("sources.id"), primary_key=True
    )
    operator_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("operators.id"), primary_key=True
    )
    weight: Mapped[int] = mapped_column(Integer)

    source = relationship("Source", back_populates="configs")
    operator = relationship("Operator", back_populates="configs")


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    lead_id: Mapped[int] = mapped_column(Integer, ForeignKey("leads.id"))
    source_id: Mapped[int] = mapped_column(Integer, ForeignKey("sources.id"))
    operator_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("operators.id"), nullable=True
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    message_data: Mapped[str] = mapped_column(String, nullable=True)

    lead = relationship("Lead", back_populates="contacts")
    source = relationship("Source", back_populates="contacts")
    operator = relationship("Operator", back_populates="contacts")
