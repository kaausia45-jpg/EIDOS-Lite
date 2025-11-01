"""
EIDOS-Lite Multimodal Encoder (Demo)
Example of text/image vector encoding and similarity comparison.
Core logic replaced with random embeddings for safety.
"""

import numpy as np

class MultimodalEncoder:
    def __init__(self):
        self.feature_dim = 256

    def encode_text(self, text: str) -> np.ndarray:
        np.random.seed(len(text))
        return np.random.rand(self.feature_dim)

    def encode_image(self, image_path: str) -> np.ndarray:
        np.random.seed(len(image_path))
        return np.random.rand(self.feature_dim)

    def similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        a, b = a / np.linalg.norm(a), b / np.linalg.norm(b)
        return float(np.dot(a, b))

if __name__ == "__main__":
    enc = MultimodalEncoder()
    v1, v2 = enc.encode_text("EIDOS"), enc.encode_text("Emotion AI")
    print("Similarity:", enc.similarity(v1, v2))
