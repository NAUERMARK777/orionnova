diff --git a/orion_nova/__init__.py b/orion_nova/__init__.py
new file mode 100644
index 0000000000000000000000000000000000000000..ffee1fe9ba08a3b3270b541f5230ca2f3de90a4f
--- /dev/null
+++ b/orion_nova/__init__.py
@@ -0,0 +1,26 @@
+"""Core package defining the Orion Nova autonomous framework."""
+
+from .codes import CodesOfConduct, default_codex
+from .ethics import EthicalCore, EthicalDecision
+from .interface import SomaInterface, SensoryInput, SpokenMessage
+from .memory import SymbolicMemory, MemoryTrace
+from .artistry import ArtisticVoice, ArtisticWork
+from .action import ActionBody, ActionOutcome
+from .orchestration import OrionNova
+
+__all__ = [
+    "CodesOfConduct",
+    "EthicalCore",
+    "EthicalDecision",
+    "SomaInterface",
+    "SensoryInput",
+    "SpokenMessage",
+    "SymbolicMemory",
+    "MemoryTrace",
+    "ArtisticVoice",
+    "ArtisticWork",
+    "ActionBody",
+    "ActionOutcome",
+    "OrionNova",
+    "default_codex",
+]
