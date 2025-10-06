from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError(visitor.get("name") + " must be "
                                     "vaccinated to enter the cafe.")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(visitor.get("name") + " has an"
                                       " expired vaccine.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor.get("name") + " must wear"
                                      " a mask to enter the cafe.")
        return f"Welcome to {self.name}"
