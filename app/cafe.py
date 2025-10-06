from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError(f"{visitor["name"]} must be vaccinated"
                                     f" to enter the cafe.")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor["name"]} has an expired "
                                       f"vaccine.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor["name"]} must wear a mask "
                                      f"to enter the cafe.")
        return f"Welcome to {self.name}"
