from pathlib import Path
from utils4plans.io import write_json
from pydantic import BaseModel, RootModel
from utils4plans.geom import Coord, CoordsType, tuple_list_from_list_of_coords


class DomainModel(BaseModel):
    name: str
    coords: list[Coord]

    # needs read and write method -> layout does..


class LayoutModel(RootModel):
    root: dict[str, CoordsType]

    def read_from_path(self):
        pass  # NOTE: for specific use case, will be read by polyfix

    def write_to_path(self, path: Path):
        write_json(self.model_dump(), path, OVERWRITE=True)

    @classmethod
    def from_domains(cls, domains: list[DomainModel]):
        return cls({i.name: tuple_list_from_list_of_coords(i.coords) for i in domains})
