from abc import ABC, abstractmethod

from pdata import file_name_set


class BasicState(ABC):
    states:dict
    @abstractmethod
    def print_state(self) -> None:
        pass

class GameState(BasicState):
    def __init__(self, server_idx: int = 1, file_name_set_idx: int = 0):
        self._server_idx = server_idx
        self._file_name_set_idx = file_name_set_idx

    @property
    def channel_idx(self) -> int:
        return self._server_idx

    @channel_idx.setter
    def channel_idx(self, idx: int):
        self._server_idx = idx

    @property
    def file_name_set_idx(self) -> int:
        return self._file_name_set_idx

    @file_name_set_idx.setter
    def file_name_set_idx(self, idx: int):
        if idx in file_name_set:
            self._file_name_set_idx = idx
        else:
            raise ValueError(f"invalid file_name_set index: {idx}")


    def print_state(self) -> None:
        print(self.states)