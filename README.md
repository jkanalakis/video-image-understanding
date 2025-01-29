# video-image-understanding
Builds a video description from scenes within the video by sampling video frames evenly from scenes and using an AI model to describe each frame append to a text file. A Streamlit app that extracts evenly sampled frames from a video and generates AI-generated descriptions for each frame using Janus-Pro-7B.

---

## **Features**
- Upload a video file (`.mp4`, `.mov`, `.avi`)  
- Set the **number of frames** to sample  
- Extract frames **at equal time intervals**  
- Generate AI-powered **descriptions** for each frame  
- Display descriptions in the **Streamlit UI**  

---

## Installation
**Clone the repository**  
```bash
git clone https://github.com/YOUR_USERNAME/video-image-understanding.git
cd video-image-understanding
```

**Create a virtual environment
```bash
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
# or
myenv\Scripts\activate  # Windows
```

**Install dependencies**  
```bash
pip install -r requirements.txt
```

**Run the app**  
```bash
streamlit run app.py
```

---

## Usage
1. **Upload a video**  
2. **Choose how many frames to extract**  
3. **See AI-generated descriptions**  
4. **Analyze the video’s content!**

---

## Technologies Used
- [Streamlit](https://streamlit.io/) – UI framework  
- [FFmpeg](https://ffmpeg.org/) – Frame extraction  
- [Transformers](https://huggingface.co/docs/transformers/) – AI model  
- [Pillow](https://pillow.readthedocs.io/) – Image processing  
- [PyTorch](https://pytorch.org/) – Model execution  

---

## Troubleshooting
### **NumPy Version Conflict**
If you see an error related to NumPy 2.x:
```bash
pip install "numpy<2"
```

### FFmpeg Not Found
If `ffmpeg` is missing, install it:  
**MacOS (Homebrew):**  
```bash
brew install ffmpeg
```
**Ubuntu:**  
```bash
sudo apt install ffmpeg
```

---

## License

MIT License – Free to use and modify.  

---

## Contributions

🔹 Feel free to fork and submit pull requests!  
🔹 Found a bug? [Open an issue](https://github.com/YOUR_USERNAME/video-image-understanding/issues).  

---

### Like this project? Give it a star on GitHub!

---

### Next Steps
- Improve AI descriptions  
- Enhance UI with better visualization  
- Add sentiment analysis for video understanding  


