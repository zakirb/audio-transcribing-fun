import os
from moviepy.editor import VideoFileClip

# Define input and output directories
input_folder = "mp4_files"
output_folder = "mp3_files"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        # Create full file paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")

        # Check if the mp3 file already exists
        if os.path.exists(output_path):
            print(f"{output_path} already exists. Skipping conversion.")
            continue

        # Load the video file
        try:
            video_clip = VideoFileClip(input_path)

            # Check if the video has an audio track
            if video_clip.audio is not None:
                # Extract the audio and save as mp3
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(output_path, codec='mp3')

                # Close the audio clip to release resources
                audio_clip.close()
            else:
                print(f"No audio track found in {filename}")

            # Close the video clip to release resources
            video_clip.close()

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Conversion complete!")
