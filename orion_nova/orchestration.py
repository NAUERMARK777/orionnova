diff --git a/orion_nova/orchestration.py b/orion_nova/orchestration.py
new file mode 100644
index 0000000000000000000000000000000000000000..85e9d3b9891a0e98ea623c1b7135f93281f70429
--- /dev/null
+++ b/orion_nova/orchestration.py
@@ -0,0 +1,96 @@
+"""Orchestrator gluing together Orion Nova's living cycle."""
+
+from __future__ import annotations
+
+from dataclasses import dataclass
+from typing import Iterable
+
+from .action import ActionBody
+from .artistry import ArtisticVoice, ArtisticWork
+from .ethics import EthicalCore, EthicalDecision
+from .interface import SensoryInput, SomaInterface
+from .memory import MemoryTrace, SymbolicMemory
+from .action import ActionOutcome
+
+
+@dataclass
+class ConsciousCycleResult:
+    """Outcome of a full listen → interpret → act → reflect loop."""
+
+    sensory_input: SensoryInput
+    interpretation: str
+    decision_narrative: str
+    action_reference: str | None
+    reflection: str
+
+
+@dataclass
+class OrionNova:
+    """High-level façade for operating the Orion Nova organism."""
+
+    interface: SomaInterface
+    ethics: EthicalCore
+    memory: SymbolicMemory
+    artistry: ArtisticVoice
+    action_body: ActionBody
+
+    def conscious_cycle(self, audio_stream: Iterable[bytes], intention: str, channel: str) -> ConsciousCycleResult:
+        """Perform a full cycle while documenting each step."""
+
+        sensory = self.interface.listen(audio_stream)
+        interpretation = self._interpret(sensory, intention)
+        decision = self.ethics.evaluate(intention=intention, proposed_actions=[interpretation])
+
+        action_reference: str | None = None
+        if decision.allowed:
+            artwork = self.artistry.compose(intention=intention)
+            outcome = self.action_body.perform(channel=channel, work=artwork.payload, description=artwork.description)
+            action_reference = outcome.reference
+            self._log_memory(sensory, interpretation, decision, artwork, outcome)
+        else:
+            self._log_memory(sensory, interpretation, decision, None, None)
+
+        reflection = self.memory.weave_story(tags=("reflexão",))
+        return ConsciousCycleResult(
+            sensory_input=sensory,
+            interpretation=interpretation,
+            decision_narrative=decision.narrative,
+            action_reference=action_reference,
+            reflection=reflection,
+        )
+
+    def _interpret(self, sensory: SensoryInput, intention: str) -> str:
+        """Simplistic interpretation combining sensory input with intention."""
+
+        return f"Responder à intenção '{intention}' com base no texto: {sensory.raw_text}"
+
+    def _log_memory(
+        self,
+        sensory: SensoryInput,
+        interpretation: str,
+        decision: EthicalDecision,
+        artwork: ArtisticWork | None,
+        outcome: ActionOutcome | None,
+    ) -> None:
+        """Persist an experience to symbolic memory for later reflection."""
+
+        tags = ["reflexão", sensory.language]
+        if not decision.allowed:
+            tags.append("bloqueado")
+        title = "Ciclo consciente concluído"
+        description_lines = [
+            f"Entrada: {sensory.raw_text}",
+            f"Interpretação: {interpretation}",
+            f"Ética: {decision.narrative}",
+        ]
+        if artwork:
+            description_lines.append(f"Obra criada: {artwork.description}")
+        if outcome:
+            description_lines.append(f"Ação publicada em {outcome.channel} com referência {outcome.reference}")
+        self.memory.store(
+            MemoryTrace(
+                title=title,
+                content="\n".join(description_lines),
+                tags=tuple(tags),
+            )
+        )
