# 🧠 EIDOS-Lite GUI (v9.2)
**Emotion-Control Interface for the EIDOS Framework**

> A public demo of the EIDOS cognitive architecture’s emotion visualization system.  
> Designed for safe, visual, and educational exploration of AI–emotion interaction.

---

## 🌐 Overview

**EIDOS-Lite** is a simplified, publicly available interface derived from the full **EIDOS Framework**.  
It demonstrates **emotion-aware dialogue** and **multimodal encoding** in a sandboxed environment.  
All reasoning, self-reflection, and autonomous-goal subsystems have been removed for safety.

---

## 📂 File Structure

| File | Description |
|------|--------------|
| `eidos_chat_gui.py` | PySide6-based GUI for real-time emotion state visualization and chat simulation |
| `eidos_safety_module_lite.py` | Lightweight safety filter for text moderation |
| `eidos_multimodal_encoder.py` | Randomized text/image encoder for multimodal demonstration |
| `character.png` | EIDOS avatar image (placeholder) |
| `LICENSE` | Custom open-source license (non-commercial research use only) |

---

## ⚙️ Run the Demo

```bash
pip install PySide6 numpy
python eidos_chat_gui.py


When executed, the GUI displays:

Real-time emotion vectors (valence, arousal, dominance)

Character avatar reacting to user input

Safety-filtered dialogue window (Lite mode)

🧩 Features
Feature	Description
Emotion-Aware Chat	Each user message updates the visible emotion graph
Multimodal Encoder	Converts text/image inputs into normalized embedding vectors
Safety Layer	Blocks unsafe or AGI-level interactions automatically
Lightweight GUI	Standalone PySide6 interface without any backend dependencies
⚠️ Important Notes

This demo does not include the real EIDOS Core (reasoning, self-reflection, emotion dynamics, or goal system).

It is intended solely for educational and research visualization.

Integration into commercial products or AGI systems requires explicit written permission from the author.

Any attempt to reconstruct or reverse-engineer EIDOS Core logic is strictly prohibited.

📜 License

This repository is licensed under a Custom Research License:

✅ Free for academic, educational, and non-commercial use

❌ Commercial use, redistribution, or model integration without consent is prohibited

© 2025 Seungjun Baek. All rights reserved.
Unauthorized use of EIDOS Core or derivative logic is strictly prohibited.

💬 Contact

Author: Seungjun Baek (백승준)

Email: <your-email>@gmail.com

Website: eidos-lab.kr
 (coming soon)

Project Tagline: Externalized Intelligence through Emotion and Interaction
