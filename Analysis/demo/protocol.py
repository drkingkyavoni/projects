from dataclasses import dataclass
from typing import Protocol


@dataclass
class Model(Protocol):
    name: str = ""
    size: int

    def __str__(self) -> None:
        print("{} {}".format(self.name, self.size))


@dataclass
class ChildModel(Model):
    text: str

    def __str__(self) -> None:
        print("child class: {} {} {}".format(self.name, self.size, self.text))


if __name__ == "__main__":
    model = ChildModel()
    print(model)
