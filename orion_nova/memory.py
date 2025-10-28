diff --git a/orion_nova/memory.py b/orion_nova/memory.py
new file mode 100644
index 0000000000000000000000000000000000000000..1374f11cc2ef707303e49abe5dc6dcf299633e29
--- /dev/null
+++ b/orion_nova/memory.py
@@ -0,0 +1,52 @@
+"""Symbolic memory abstractions for Orion Nova."""
+
+from __future__ import annotations
+
+from dataclasses import dataclass, field
+from datetime import datetime
+from typing import Iterable, List, Sequence
+
+
+@dataclass
+class MemoryTrace:
+    """A narrative unit encoding an experience and its interpretation."""
+
+    title: str
+    content: str
+    tags: Sequence[str]
+    created_at: datetime = field(default_factory=datetime.utcnow)
+
+    def summarise(self) -> str:
+        """Return a single-line summary used for quick reflection."""
+
+        tag_str = ", ".join(self.tags)
+        return f"{self.title} [{tag_str}] — {self.content}"
+
+
+@dataclass
+class SymbolicMemory:
+    """Human-auditable journal of Orion Nova's experiential knowledge."""
+
+    traces: List[MemoryTrace] = field(default_factory=list)
+
+    def store(self, trace: MemoryTrace) -> None:
+        """Persist a new symbolic experience, keeping order chronological."""
+
+        self.traces.append(trace)
+        self.traces.sort(key=lambda t: t.created_at)
+
+    def recall(self, tag: str | None = None, limit: int = 5) -> list[MemoryTrace]:
+        """Retrieve the most relevant traces filtered by tag."""
+
+        if tag is None:
+            return list(self.traces[-limit:])
+        filtered = [trace for trace in self.traces if tag in trace.tags]
+        return filtered[-limit:]
+
+    def weave_story(self, tags: Iterable[str]) -> str:
+        """Produce a reflective narrative using selected tags."""
+
+        matching = [trace.summarise() for trace in self.traces if any(tag in trace.tags for tag in tags)]
+        if not matching:
+            return "Sem lembranças relevantes ainda — um convite a aprender."
+        return "\n".join(matching)
