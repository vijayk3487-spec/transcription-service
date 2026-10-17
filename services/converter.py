import os
import subprocess

def convert_audio(input_file):

    filename = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"uploads/{filename}.wav"

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            input_file,
            "-ar",
            "16000",
            "-ac",
            "1",
            output_file
        ],
        check=True
    )

    return output_file