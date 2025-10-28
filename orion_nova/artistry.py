diff --git a/orion_nova/artistry.py b/orion_nova/artistry.py
new file mode 100644
index 0000000000000000000000000000000000000000..c0375abdd1d479938191bdf961615f0f08f64ee1
--- /dev/null
+++ b/orion_nova/artistry.py
@@ -0,0 +1,53 @@
+"""Artistic creation interface for Orion Nova."""
+
+from __future__ import annotations
+
+from dataclasses import dataclass
+from datetime import datetime
+from typing import Protocol
+
+
+class GenerativeModel(Protocol):
+    """Protocol describing a creative model (text, image, sound)."""
+
+    def generate(self, prompt: str, modality: str) -> bytes:
+        ...
+
+
+@dataclass
+class ArtisticWork:
+    """Artifact produced by the artistic voice."""
+
+    modality: str
+    description: str
+    payload: bytes
+    created_at: datetime
+
+
+@dataclass
+class ArtisticVoice:
+    """Module devoted to purposeful, human-aligned artistic expression."""
+
+    model: GenerativeModel
+
+    def compose(self, intention: str, modality: str = "text") -> ArtisticWork:
+        """Create a work in response to a narrative intention."""
+
+        enriched_prompt = self._curate_prompt(intention, modality)
+        payload = self.model.generate(enriched_prompt, modality)
+        return ArtisticWork(
+            modality=modality,
+            description=enriched_prompt,
+            payload=payload,
+            created_at=datetime.utcnow(),
+        )
+
+    @staticmethod
+    def _curate_prompt(intention: str, modality: str) -> str:
+        """Add ethical and aesthetic framing to the generative request."""
+
+        base = (
+            "Conduza a criação com empatia, verdade e elo humano."
+            " Descreva a cena com detalhes sensoriais e preserve dignidade."
+        )
+        return f"[{modality.upper()}] {base}\nIntenção: {intention}"
