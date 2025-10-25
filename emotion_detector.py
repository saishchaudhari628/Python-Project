import text2emotion as te
import time
import sys

# Function to print welcome banner
def welcome():
    print("="*60)
    print("🎭 Welcome to Text-based Emotion Detector 🎭")
    print("Type 'exit' anytime to quit.")
    print("="*60)

# Function to detect emotions
def detect_emotion(text):
    emotions = te.get_emotion(text)
    dominant = max(emotions, key=emotions.get)
    return emotions, dominant

# Function to return a message based on dominant emotion
def emotion_message(dominant):
    messages = {
        "Happy": "😊 Keep smiling! Happiness looks great on you.",
        "Angry": "😡 Take a deep breath. Anger fades away.",
        "Surprise": "😲 Wow! That must be unexpected.",
        "Sad": "😢 It's okay to feel sad. Take care of yourself.",
        "Fear": "😱 Be brave! Face your fears step by step."
    }
    return messages.get(dominant, "🤔 Feeling something unique today?")

# Function to log emotions
def log_emotion(text, emotions, dominant):
    with open("emotion_log.txt", "a") as f:
        f.write(f"Text: {text}\n")
        f.write(f"Emotions: {emotions}\n")
        f.write(f"Dominant: {dominant}\n")
        f.write("-"*50 + "\n")

# Function to print emotions neatly
def print_emotions(emotions):
    print("\nDetected Emotions:")
    for e, v in emotions.items():
        print(f"{e}: {v:.2f}")

# Main program
def main():
    welcome()
    while True:
        text = input("\nEnter your sentence: ")
        if text.lower() == "exit":
            print("\n👋 Goodbye! See you soon!")
            break

        emotions, dominant = detect_emotion(text)
        print_emotions(emotions)
        print(f"\n👉 Dominant Emotion: {dominant}")
        print(emotion_message(dominant))

        log_emotion(text, emotions, dominant)
        time.sleep(1)

if __name__ == "__main__":
    main()
