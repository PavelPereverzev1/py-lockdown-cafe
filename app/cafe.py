from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f'{visitor["name"]} is not a vaccine.')
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f'{visitor["name"]} vaccine is outdated.'
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f'{visitor["name"]} is not wearing mask.'
            )
        return f"Welcome to {self.name}"
