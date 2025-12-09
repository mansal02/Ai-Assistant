import speech_recognition as sr
import pyttsx3
import sys

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

class InputHandler:
    def __init__(self):
        self.mode = "voice" # Default to voice
        self.recognizer = sr.Recognizer()
        
        # Check if microphone is actually available
        try:
            with sr.Microphone() as source:
                pass
            print("[System] Microphone detected. Voice mode enabled.")
        except OSError:
            print("[System] No microphone found. Switching to TEXT mode.")
            self.mode = "text"
        except Exception as e:
            print(f"[System] Mic Error ({e}). Switching to TEXT mode.")
            self.mode = "text"

    def get_input(self):
        """
        Smart function that decides whether to listen or ask for text.
        """
        if self.mode == "text":
            return self._get_text_input()
        else:
            return self._get_voice_input()

    def _get_text_input(self):
        try:
            # Simple chatbox style input
            text = input("\n[YOU]: ")
            return text.lower()
        except EOFError:
            return None

    def _get_voice_input(self):
        with sr.Microphone() as source:
            print("\n[Listening...] (Press Ctrl+C to switch to Text Mode)")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                # Listen for 1 second
                audio = self.recognizer.listen(source, timeout=1)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"[Heard]: {text}")
                return text
            
            except sr.WaitTimeoutError:
                print("[System] Didn't hear anything.")
                # Option: Fallback to text if silence?
                choice = input(">> I couldn't hear you. Type instead? (y/n): ")
                if choice.lower() == 'y':
                    return self._get_text_input()
                return None
            
            except sr.UnknownValueError:
                print("[System] Couldn't understand audio.")
                return None
            
            except sr.RequestError:
                print("[System] Internet error. Switching to text mode.")
                self.mode = "text"
                return self._get_text_input()
            
            except KeyboardInterrupt:
                # Allows you to force text mode by pressing Ctrl+C while listening
                print("\n[System] Switching to Text Mode...")
                self.mode = "text"
                return self._get_text_input()

def speak_response(text):
    print(f"[AI]: {text}")
    engine.say(text)
    engine.runAndWait()