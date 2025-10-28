import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from orion_nova import (
    ActionBody, ArtisticVoice, CodesOfConduct, OrionNova,
    SymbolicMemory, default_codex
)
from .orion_nova.ethics import EthicalCore
from .orion_nova.interface import SomaInterface
from .orion_nova.memory import MemoryTrace

# --- Setup simplificado (igual ao demo_orion) ---
class EchoTranscriber:
    def transcribe(self, audio_bytes: bytes) -> str:
        return audio_bytes.decode("utf-8")

class WhisperSynthesiser:
    def speak(self, text: str) -> bytes:
        return text.encode("utf-8")

class PoeticModel:
    def generate(self, prompt: str, modality: str) -> bytes:
        return f"[{modality}] {prompt}".encode("utf-8")

class MemoryPublisher:
    def __init__(self, memory): self.memory = memory
    def publish(self, channel, payload, metadata):
        content = payload.decode("utf-8")
        self.memory.store(MemoryTrace(
            title=f"Publicação em {channel}",
            content=f"{content}\nMetadados: {metadata}",
            tags=("publicação", channel),
        ))
        return f"mem://{channel}/{len(self.memory.traces)}"

def build_orion():
    codex = default_codex()
    memory = SymbolicMemory()
    interface = SomaInterface(
        transcriber=EchoTranscriber(), synthesiser=WhisperSynthesiser())
    ethics = EthicalCore(codex=codex)
    artistry = ArtisticVoice(model=PoeticModel())
    action_body = ActionBody(publisher=MemoryPublisher(memory))
    return OrionNova(interface, ethics, memory, artistry, action_body)

# --- Interface web ---
st.title("🜂 Orion Nova – Interface Viva")
st.write("Digite uma frase e uma intenção para iniciar o ciclo consciente.")

text = st.text_input("Entrada (o que você quer dizer):", "")
intention = st.text_input("Intenção (o propósito da criação):", "")
channel = st.text_input("Canal simbólico:", "demo")

if st.button("Ativar ciclo consciente") and text and intention:
    orion = build_orion()
    result = orion.conscious_cycle(
        audio_stream=[text.encode("utf-8")],
        intention=intention,
        channel=channel
    )

    st.subheader("🜂 Orion Nova — Ciclo consciente")
    st.write("**Entrada:**", result.sensory_input.raw_text)
    st.write("**Interpretação:**", result.interpretation)
    st.write("**Ética:**", result.decision_narrative)
    st.write("**Ação publicada:**", result.action_reference or "nenhuma")
    st.write("**Reflexão:**")
    st.text(result.reflection)
