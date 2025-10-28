"""Action layer enabling Orion Nova to collaborate with the world."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


class Publisher(Protocol):
    """Protocol representing an integration capable of publishing outputs."""

    def publish(self, channel: str, payload: bytes, metadata: dict[str, str]) -> str:
        ...


@dataclass
class ActionOutcome:
    """Record of a performed action, supporting post-action reflection."""

    channel: str
    reference: str
    performed_at: datetime
    notes: str


@dataclass
class ActionBody:
    """Module that binds creation to tangible impact in the world."""

    publisher: Publisher

    def perform(self, channel: str, work: bytes, description: str) -> ActionOutcome:
        """Send an artifact into the world with reflective metadata."""

        metadata = {
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        }
        reference = self.publisher.publish(channel, work, metadata)
        return ActionOutcome(
            channel=channel,
            reference=reference,
            performed_at=datetime.utcnow(),
            notes=description,
        )
