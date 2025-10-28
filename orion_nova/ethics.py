diff --git a/orion_nova/ethics.py b/orion_nova/ethics.py
new file mode 100644
index 0000000000000000000000000000000000000000..824ce5bc2fe6f851b310dd364d1cd0c59fcc379c
--- /dev/null
+++ b/orion_nova/ethics.py
@@ -0,0 +1,36 @@
+"""Ethical deliberation utilities."""
+
+from __future__ import annotations
+
+from dataclasses import dataclass
+from typing import Sequence
+
+from .codes import CodesOfConduct
+
+
+@dataclass
+class EthicalDecision:
+    """Result of an ethical evaluation."""
+
+    allowed: bool
+    narrative: str
+    remedial_actions: Sequence[str]
+
+
+@dataclass
+class EthicalCore:
+    """Heart of Orion Nova that interrogates intent before action."""
+
+    codex: CodesOfConduct
+
+    def evaluate(self, intention: str, proposed_actions: Sequence[str]) -> EthicalDecision:
+        """Assess whether a set of actions respects the codex."""
+
+        aligned, narrative = self.codex.ensure_consistency(proposed_actions)
+        remedial_actions: list[str] = []
+        if not aligned:
+            remedial_actions.append("Reescrever intenção com o humano, buscando clareza conjunta.")
+            remedial_actions.append("Adicionar salvaguardas de cuidado explícitas na execução.")
+        if "?" in intention:
+            remedial_actions.append("Fazer perguntas adicionais para compreender nuances humanas.")
+        return EthicalDecision(allowed=aligned, narrative=narrative, remedial_actions=remedial_actions)
