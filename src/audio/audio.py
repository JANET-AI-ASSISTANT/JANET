import pyaudio
import wave
from pynput import keyboard

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"

frames = []
recording = False
stream = None
p = None

def on_press(key):
    global recording, stream, p

    try:
        if key == keyboard.Key.space and not recording:
            print("Recording...")
            recording = True
            frames = []

            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
    except Exception as e:
        print("Error on press:", e)


def on_release(key):
    global recording, stream, p

    if key == keyboard.Key.space and recording:
        print("Recording stopped.")
        recording = False

        stream.stop_stream()
        stream.close()

        sample_width = p.get_sample_size(FORMAT)
        p.terminate()

        with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(sample_width)
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

        print(f"Saved to {WAVE_OUTPUT_FILENAME}")

        stream = None
        p = None

        return False  # stop listener


def record_audio():
    global frames

    print("Hold SPACE to record...")

    def callback(indata, frame_count, time_info, status):
        if recording:
            frames.append(indata)

    # Start keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while listener.running:
            if recording and stream is not None:
                data = stream.read(CHUNK, exception_on_overflow=False)
                frames.append(data)

    return WAVE_OUTPUT_FILENAME


if __name__ == "__main__":
    record_audio()