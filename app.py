import streamlit as st
import ffmpeg
import os
from PIL import Image
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Function to extract frames from video
def extract_frames(video_path, num_frames, output_folder):
    os.makedirs(output_folder, exist_ok=True)  # Ensure output directory exists

    # Get video duration using FFmpeg
    probe = ffmpeg.probe(video_path)
    duration = float(probe['format']['duration'])  # Extract duration in seconds

    # Calculate time interval for frame extraction
    interval = duration / num_frames

    # FFmpeg command to extract frames at specific timestamps
    try:
        (
            ffmpeg
            .input(video_path)
            .output(f'{output_folder}/frame_%04d.png', vf=f"select='not(mod(t,{interval}))'", vsync="vfr")
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
        message = f"Frames extracted every {interval:.2f} seconds."
        print(message)  # Log to console
        return message  # Return message to display in UI
    except ffmpeg.Error as e:
        error_msg = f"FFmpeg error: {e.stderr.decode()}"
        print(error_msg)
        return error_msg



# Function to generate description for an image using Janus-Pro-7B
def generate_description(image_path, model, tokenizer):
    image = Image.open(image_path)
    # Preprocess the image and generate description
    # This is a placeholder; actual implementation depends on Janus-Pro-7B's requirements
    inputs = tokenizer("Describe the image:", return_tensors="pt")
    outputs = model.generate(**inputs)
    description = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return description

def main():
    st.title("Video Image Understanding App")

    # File uploader for video
    video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])
    num_frames = st.number_input("Number of frames to sample", min_value=1, value=10)

    if video_file is not None:
        # Save uploaded video to a temporary file
        video_path = f"temp_{video_file.name}"
        with open(video_path, "wb") as f:
            f.write(video_file.read())

        # Create a directory to save frames
        output_folder = "frames"
        os.makedirs(output_folder, exist_ok=True)

        # Extract frames and get extraction message
        extraction_message = extract_frames(video_path, num_frames, output_folder)

        # Display frame extraction interval in UI
        st.success(extraction_message)

        # Load Janus-Pro-7B model and tokenizer
        model_name = "deepseek-ai/Janus-Pro-7B"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        model.eval()

        # Generate descriptions for each frame
        descriptions = []
        for frame_file in sorted(os.listdir(output_folder)):
            frame_path = os.path.join(output_folder, frame_file)
            description = generate_description(frame_path, model, tokenizer)
            descriptions.append(f"{frame_file}: {description}")

        # Display descriptions
        st.header("Generated Descriptions")
        for desc in descriptions:
            st.write(desc)

        # Clean up temporary files
        os.remove(video_path)
        for frame_file in os.listdir(output_folder):
            os.remove(os.path.join(output_folder, frame_file))
        os.rmdir(output_folder)


if __name__ == "__main__":
    main()
