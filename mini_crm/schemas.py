from pydantic import BaseModel, Field
from typing import List, Optional

# --- Базовые схемы Pydantic ---


# Схема для создания/обновления Оператора
class OperatorBase(BaseModel):
    name: str
    is_active: bool = Field(True)  # Активен / не активен [cite: 21]
    max_load: int = Field(5)  # Максимальное количество активных лидов [cite: 22]


class OperatorCreate(OperatorBase):
    pass


class Operator(OperatorBase):
    id: int

    class Config:
        orm_mode = True


# Схема для создания Источника
class SourceBase(BaseModel):
    name: str


class SourceCreate(SourceBase):
    pass


class Source(SourceBase):
    id: int

    class Config:
        orm_mode = True


# Схема для настройки весов операторов в источнике
class SourceConfigSchema(BaseModel):
    operator_id: int
    weight: int  # Числовой вес (компетенция) [cite: 24, 53]


# Схема для настройки всех весов для Источника
class SourceConfigUpdate(BaseModel):
    configs: List[SourceConfigSchema]


# Схема для регистрации нового обращения
class ContactRegister(BaseModel):
    # [cite_start]Идентификатор лида (для поиска/создания) [cite: 84]
    lead_external_id: str
    source_id: int
    message_data: Optional[str] = Field(
        None
    )  # Дополнительные данные обращения [cite: 86]


# Схема ответа на регистрацию обращения
class ContactResponse(BaseModel):
    id: int
    lead_id: int
    source_id: int
    operator_id: Optional[int]
    is_active: bool

    class Config:
        orm_mode = True


# Схема для отображения статуса Оператора
class OperatorStatus(Operator):
    current_load: int
