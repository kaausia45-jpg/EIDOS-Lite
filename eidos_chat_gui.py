# EIDOS-Lite GUI (v9.2 - Emotion Control Demo)
# Safe public version with all proprietary EIDOS Core logic removed.

import sys
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QPushButton, QGridLayout, QFrame
)
from PySide6.QtCore import Qt, Slot

EMOTION_DIM, EMOTION_MIN, EMOTION_MAX = 12, 0.0, 2.0
EMOTION_LABELS = [f"Emotion {i+1}" for i in range(EMOTION_DIM)]

class ChatWindow(QWidget):
    """A simple demo interface for displaying and adjusting EIDOS emotional states."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EIDOS-Lite - Emotion Control Interface")
        self.setGeometry(100, 100, 800, 600)
        self.emotion_inputs = {}
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        title = QLabel("EIDOS-Lite Emotion Control Interface (Demo)")
        title.setStyleSheet("font-size:18pt; font-weight:bold; color:#005A9C;")
        layout.addWidget(title)

        # Emotion vector grid
        frame = QFrame(self)
        grid = QGridLayout(frame)
        cols = 3
        for i, label_text in enumerate(EMOTION_LABELS):
            row, col = divmod(i, cols)
            grid.addWidget(QLabel(label_text), row, col * 2)
            box = QLineEdit("0.000")
            box.setAlignment(Qt.AlignRight)
            self.emotion_inputs[i] = box
            grid.addWidget(box, row, col * 2 + 1)
        layout.addWidget(frame)

        self.apply_button = QPushButton("Apply Emotions (Demo)")
        self.apply_button.clicked.connect(self._apply_changes)
        layout.addWidget(self.apply_button)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)

    @Slot()
    def _apply_changes(self):
        values = [float(self.emotion_inputs[i].text()) for i in range(EMOTION_DIM)]
        clipped = np.clip(values, EMOTION_MIN, EMOTION_MAX)
        self.log.append(f"🔧 Emotion vector updated: {np.round(clipped, 3)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())
