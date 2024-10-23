import tkinter as tk
from tkinter import filedialog, messagebox

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        label_image_input.config(text="Image Selected: " + file_path)

def upload_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        label_audio_input.config(text="Audio Selected: " + file_path)

def upload_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
    if file_path:
        label_video_input.config(text="Video Selected: " + file_path)

def process_inputs():
    result = "Fake"
    label_result.config(text="Detection Result: " + result)

# Create main window
window = tk.Tk()
window.title("Multimodal Deepfake Detection")

# Image input
label_image_input = tk.Label(window, text="No Image Selected")
label_image_input.pack(pady=10)
btn_upload_image = tk.Button(window, text="Upload Image", command=upload_image)
btn_upload_image.pack()

# Audio input
label_audio_input = tk.Label(window, text="No Audio Selected")
label_audio_input.pack(pady=10)
btn_upload_audio = tk.Button(window, text="Upload Audio", command=upload_audio)
btn_upload_audio.pack()

# Video input
label_video_input = tk.Label(window, text="No Video Selected")
label_video_input.pack(pady=10)
btn_upload_video = tk.Button(window, text="Upload Video", command=upload_video)
btn_upload_video.pack()

# Process button
btn_process = tk.Button(window, text="Process Inputs", command=process_inputs)
btn_process.pack(pady=20)

# Output label
label_result = tk.Label(window, text="Detection Result: ")
label_result.pack(pady=20)

# Start the main loop
window.mainloop()
