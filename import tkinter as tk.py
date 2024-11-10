import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

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

def update_background(event):
    new_width = event.width
    new_height = event.height
    resized_bg = original_bg_image.resize((new_width, new_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(resized_bg)
    bg_label.config(image=bg_photo)
    bg_label.image = bg_photo

# Create the main window
window = tk.Tk()
window.title("Multimodal Deepfake Detection")
window.attributes('-fullscreen', True)

# Load the background image (replace with your image path)
original_bg_image = Image.open("E:\Misc\Wallpapers\One Piece Episode 968 - AniMixPlay - Google Chrome 7_28_2021 6_37_28 PM.png")  # Replace with your image path

# Set up the background label
bg_photo = ImageTk.PhotoImage(original_bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Bind window resize event
window.bind("<Configure>", update_background)

# Frame for input sections (centered)
frame_inputs = ttk.Frame(window, style="TFrame")
frame_inputs.grid(row=0, column=0, sticky="nsew")

# Load and display icons (replace with your icon paths)
image_icon = ImageTk.PhotoImage(Image.open(r"D:\UI\image.png").resize((32, 32)))
audio_icon = ImageTk.PhotoImage(Image.open(r"D:\UI\sound.png").resize((32, 32)))
video_icon = ImageTk.PhotoImage(Image.open(r"D:\UI\video.jpg").resize((32, 32)))

# Image input section (centered)
frame_image = tk.LabelFrame(frame_inputs, text="Image Input", bg="#333", fg="white", relief="solid", bd=1)
frame_image.grid(row=0, column=0, sticky="nsew")
label_image_input = ttk.Label(frame_image, text="No Image Selected", style="TLabel")
label_image_input.pack(pady=5)
btn_upload_image = ttk.Button(frame_image, text="Upload Image", image=image_icon, compound="left", command=upload_image)
btn_upload_image.pack()

# Audio input section (centered)
frame_audio = tk.LabelFrame(frame_inputs, text="Audio Input", bg="#333", fg="white", relief="solid", bd=1)
frame_audio.grid(row=0, column=1, sticky="nsew")
label_audio_input = ttk.Label(frame_audio, text="No Audio Selected", style="TLabel")
label_audio_input.pack(pady=5)
btn_upload_audio = ttk.Button(frame_audio, text="Upload Audio", image=audio_icon, compound="left", command=upload_audio)
btn_upload_audio.pack()

# Video input section (centered)
frame_video = tk.LabelFrame(frame_inputs, text="Video Input", bg="#333", fg="white", relief="solid", bd=1)
frame_video.grid(row=0, column=2, sticky="nsew")
label_video_input = ttk.Label(frame_video, text="No Video Selected", style="TLabel")
label_video_input.pack(pady=5)
btn_upload_video = ttk.Button(frame_video, text="Upload Video", image=video_icon, compound="left", command=upload_video)
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
status_frame = tk.Frame(window, bg="black")
status_frame.grid(row=4, column=0, sticky="we")
status_label = ttk.Label(status_frame, text="Waiting for input...", relief="sunken", anchor="w", style="TLabel")
status_label.pack(fill="x")

# Start the main loop
window.mainloop()