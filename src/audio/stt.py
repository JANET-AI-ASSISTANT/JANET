import whisper

def transcribe(file):
    model = whisper.load_model("tiny")
    result = model.transcribe(file)
    return result["text"]

if __name__ == "__main__":
    print(transcribe("output.wav"))