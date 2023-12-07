from pydantic import BaseModel, model_validator


class OficerData(BaseModel):
  firstname: str
  lastname: str
  rank: str


class ShipData(BaseModel):
  alignment: str
  name: str
  shipClass: str
  size: int
  armed: bool
  officer: list[OficerData]
  status: str

  @model_validator(mode='after')
  def validate_name(self):
    if self.status != 'Enemy' and self.name == 'Unknown':
      raise ValueError('Name can only be "Unknown" for Enemy ships')
    if (self.shipClass == 'Frigate' or self.shipClass == 'Destroyer') and self.status == 'Enemy':
      raise ValueError('Enemy ships can only be Frigates or Destroyers')
    if self.shipClass == 'Carrier' and self.armed == True:
      raise ValueError('Carriers cannot be armed')
    return self