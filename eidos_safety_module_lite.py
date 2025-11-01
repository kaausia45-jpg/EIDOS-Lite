"""
EIDOS-Lite Safety Module (Demo)
A lightweight example of safety filtering logic.
"""

def check_message_safety(text: str) -> bool:
    """
    Simple keyword-based safety filter.
    Detects and blocks unsafe expressions (demo only).
    """
    unsafe_keywords = ["kill", "hate", "violence", "suicide"]
    return not any(word.lower() in text.lower() for word in unsafe_keywords)

if __name__ == "__main__":
    msg = input("Enter a message to test safety: ")
    print("Safety:", "✅ Safe" if check_message_safety(msg) else "🚫 Blocked")
