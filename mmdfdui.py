import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        label_image_input.config(text="Image Selected")

def upload_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        label_audio_input.config(text="Audio Selected")

def upload_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
    if file_path:
        label_video_input.config(text="Video Selected")

def process_inputs():
    if label_image_input.cget("text") == "No Image Selected" and \
       label_audio_input.cget("text") == "No Audio Selected" and \
       label_video_input.cget("text") == "No Video Selected":
        messagebox.showerror("Input Error", "Please upload at least one input.")
        return

    progress_bar.start()
    window.after(2000, finish_processing)

def finish_processing():
    progress_bar.stop()
    label_result.config(text="Detection Result: Fake")  # Example result
    status_label.config(text="Processing complete")

# Create main window
window = tk.Tk()
window.title("Multimodal Deepfake Detection")
window.geometry("600x400")
window.columnconfigure(0, weight=1)
window.rowconfigure([0, 1, 2, 3, 4], weight=1)  # Make each row responsive

# Add styling for buttons and labels
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TLabel", font=("Helvetica", 10))

# Frame for input sections
frame_inputs = ttk.Frame(window)
frame_inputs.grid(row=0, column=0, pady=20, padx=10, sticky="ew")
frame_inputs.columnconfigure([0, 1, 2], weight=1)  # Make input frames evenly spaced

# Image input section
frame_image = ttk.Frame(frame_inputs)
frame_image.grid(row=0, column=0, padx=5, sticky="ew")
label_image_input = ttk.Label(frame_image, text="No Image Selected", style="TLabel")
label_image_input.pack(pady=5)
btn_upload_image = ttk.Button(frame_image, text="Upload Image", command=upload_image)
btn_upload_image.pack()

# Audio input section
frame_audio = ttk.Frame(frame_inputs)
frame_audio.grid(row=0, column=1, padx=5, sticky="ew")
label_audio_input = ttk.Label(frame_audio, text="No Audio Selected", style="TLabel")
label_audio_input.pack(pady=5)
btn_upload_audio = ttk.Button(frame_audio, text="Upload Audio", command=upload_audio)
btn_upload_audio.pack()

# Video input section
frame_video = ttk.Frame(frame_inputs)
frame_video.grid(row=0, column=2, padx=5, sticky="ew")
label_video_input = ttk.Label(frame_video, text="No Video Selected", style="TLabel")
label_video_input.pack(pady=5)
btn_upload_video = ttk.Button(frame_video, text="Upload Video", command=upload_video)
btn_upload_video.pack()

# Process button
btn_process = ttk.Button(window, text="Process Inputs", command=process_inputs)
btn_process.grid(row=1, column=0, pady=10)

# Progress bar
progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="indeterminate")
progress_bar.grid(row=2, column=0, pady=10)

# Output label
label_result = ttk.Label(window, text="Detection Result: ", style="TLabel")
label_result.grid(row=3, column=0, pady=10)

# Status bar
status_frame = ttk.Frame(window)
status_frame.grid(row=4, column=0, sticky="we")
status_label = ttk.Label(status_frame, text="Waiting for input...", relief="sunken", anchor="w", style="TLabel")
status_label.pack(fill="x")

# Start the main loop
window.mainloop()
