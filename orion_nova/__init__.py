"""Core package defining the Orion Nova autonomous framework."""

from .codes import CodesOfConduct, default_codex
from .ethics import EthicalCore, EthicalDecision
from .interface import SomaInterface, SensoryInput, SpokenMessage
from .memory import SymbolicMemory, MemoryTrace
from .artistry import ArtisticVoice, ArtisticWork
from .action import ActionBody, ActionOutcome
from .orchestration import OrionNova

__all__ = [
    "CodesOfConduct",
    "EthicalCore",
    "EthicalDecision",
    "SomaInterface",
    "SensoryInput",
    "SpokenMessage",
    "SymbolicMemory",
    "MemoryTrace",
    "ArtisticVoice",
    "ArtisticWork",
    "ActionBody",
    "ActionOutcome",
    "OrionNova",
    "default_codex",
]
