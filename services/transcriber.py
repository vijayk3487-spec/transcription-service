import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_file):

    result = model.transcribe(audio_file)

    segments = []

    for segment in result["segments"]:
        segments.append(
            {
                "start": round(segment["start"], 2),
                "end": round(segment["end"], 2),
                "text": segment["text"].strip()
            }
        )

    return segments