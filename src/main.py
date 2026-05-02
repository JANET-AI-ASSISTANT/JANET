from audio.audio import record_audio
from audio.stt import transcribe
from intent.intent import decide_action
from utils.utils import tell_time, end_timer, set_timer

while True:
    file = record_audio()
    query = transcribe(file)
    print(query)
    action = decide_action(query)
    print(action)