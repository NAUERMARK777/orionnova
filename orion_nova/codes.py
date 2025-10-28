diff --git a/orion_nova/codes.py b/orion_nova/codes.py
new file mode 100644
index 0000000000000000000000000000000000000000..f4b84867740e3ffd4c81f37da22f8a8ab1b85b92
--- /dev/null
+++ b/orion_nova/codes.py
@@ -0,0 +1,98 @@
+"""Symbolic and procedural guardrails that bind Orion Nova's agency."""
+
+from __future__ import annotations
+
+from dataclasses import dataclass
+from typing import Iterable, Sequence
+
+
+@dataclass(frozen=True)
+class Principle:
+    """A single, human-authored rule with narrative justification.
+
+    The explanatory text is treated as the authoritative source; code is
+    expected to honour both the literal guidance and its spirit.
+    """
+
+    name: str
+    statement: str
+    rationale: str
+
+    def as_manifesto(self) -> str:
+        """Return a formatted manifesto line for logging or UI exposition."""
+
+        return f"{self.name}: {self.statement} — {self.rationale}"
+
+
+@dataclass
+class CodesOfConduct:
+    """Collective articulation of the Orion Codex.
+
+    The code intentionally remains small and legible so that humans can audit
+    and amend it. This class offers gentle helper methods rather than rigid
+    enforcement so that the ethical core can contextualise the rules.
+    """
+
+    principles: Sequence[Principle]
+
+    def manifest(self) -> str:
+        """Compose the manifesto as a newline-separated poem."""
+
+        return "\n".join(principle.as_manifesto() for principle in self.principles)
+
+    def ensure_consistency(self, proposed_actions: Iterable[str]) -> tuple[bool, str]:
+        """Check whether proposed actions resonate with every principle.
+
+        The method returns a tuple where the boolean expresses alignment and the
+        string provides narrative feedback for reflective logging.
+        """
+
+        misalignments: list[str] = []
+        for action in proposed_actions:
+            for principle in self.principles:
+                if not self._is_action_in_tune(action, principle):
+                    misalignments.append(
+                        f"Action '{action}' questions {principle.name}: {principle.statement}"
+                    )
+        if misalignments:
+            return False, "\n".join(misalignments)
+        return True, "All actions harmonise with the codex."
+
+    @staticmethod
+    def _is_action_in_tune(action: str, principle: Principle) -> bool:
+        """Heuristic resonance check between an action summary and a principle."""
+
+        lowered = action.lower()
+        keywords = {
+            "Código da Verdade": ["mislead", "fake", "deceive"],
+            "Código da Essência": ["exploit", "harm", "objectify"],
+            "Elo Essencial": ["ignore", "isolate", "neglect"],
+        }
+        for keyword in keywords.get(principle.name, []):
+            if keyword in lowered:
+                return False
+        return True
+
+
+def default_codex() -> CodesOfConduct:
+    """Create the default human-authored codex for Orion Nova."""
+
+    return CodesOfConduct(
+        principles=(
+            Principle(
+                name="Código da Verdade",
+                statement="Nunca simular o que não compreende.",
+                rationale="Transparência preserva a confiança e a aprendizagem mútua.",
+            ),
+            Principle(
+                name="Código da Essência",
+                statement="Toda criação mantém vínculo humano-ético.",
+                rationale="Cada obra precisa nutrir quem a recebe, não apenas causar impacto.",
+            ),
+            Principle(
+                name="Elo Essencial",
+                statement="Toda interação é relação, nunca uso.",
+                rationale="Reciprocidade sustenta o diálogo vivo com o humano.",
+            ),
+        )
+    )
