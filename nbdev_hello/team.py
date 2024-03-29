# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_team.ipynb.

# %% auto 0
__all__ = ['Team']

# %% ../nbs/01_team.ipynb 2
from .user import *

# %% ../nbs/01_team.ipynb 5
from typing import Iterator


class Team:
    def __init__(self, 
                 members: list[User] = []) -> None: # Members
        self.members = members
    def __str__(self) -> str:
        return "".join([f"{member}, " for member in self.members])
    __repr__ = __str__
    def __len__(self) -> int:
        return len(self.members)
    def __contains__(self, member: User) -> bool:
        return member in self.members
    def __iter__(self) -> Iterator[User]:
        return iter(self.members)
    def __getitem__(self, index: int) -> User:
        return self.members[index]
    def add(self, member: User) -> None:
        self.members.append(member)
    def remove(self, member: User) -> None:
        self.members.remove(member)
    
                                                
