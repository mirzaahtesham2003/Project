# import os
# import moviepy.editor
# from tkinter import Tk, filedialog, simpledialog, messagebox

# # Ensure 'input' and 'output' directories exist
# if not os.path.exists("input"):
#     os.makedirs("input")
# if not os.path.exists("output"):
#     os.makedirs("output")

# def extract_audio_from_video(video_path, audio_path):
#     try:
#         video = moviepy.editor.VideoFileClip(video_path)
#         audio = video.audio
#         audio.write_audiofile(audio_path)
#         return True
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return False

# def main():
#     root = Tk()
#     root.withdraw()  # Hide the main window
    
#     video_path = filedialog.askopenfilename(title="Select the video file", filetypes=[("Video Files", "*.mp4;*.avi;*.mkv;*.flv;*.mov")])
#     if not video_path:
#         return

#     # Save the selected video file to the 'input' directory
#     dest_path = os.path.join("input", os.path.basename(video_path))
#     with open(video_path, "rb") as fsrc:
#         with open(dest_path, "wb") as fdst:
#             fdst.write(fsrc.read())

#     audio_format = simpledialog.askstring("Output Format", "Enter desired audio format (e.g. mp3, wav):", initialvalue="mp3")

#     # Set the audio path in the 'output' directory with the same filename as the video (but different extension)
#     output_filename = os.path.splitext(os.path.basename(dest_path))[0] + f".{audio_format}"
#     audio_path = os.path.join("output", output_filename)
    
#     success = extract_audio_from_video(dest_path, audio_path)

#     if success:
#         messagebox.showinfo("Success", f"Audio saved successfully at: {audio_path}")
#     else:
#         messagebox.showerror("Error", "Failed to extract audio. Please check the video file.")

# if __name__ == "__main__":
#     main()
import os
import moviepy.editor
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk

# Ensure 'input' and 'output' directories exist
if not os.path.exists("input"):
    os.makedirs("input")
if not os.path.exists("output"):
    os.makedirs("output")

def extract_audio_from_video(video_path, audio_path):
    try:
        video = moviepy.editor.VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Set theme and styles
    style = ttk.Style(root)
    style.theme_use('clam')  # Options: 'clam', 'alt', 'default', 'classic'

    # Set overall styles for the application
    style.configure('TButton', font=('Helvetica', 12), padding=10)
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TEntry', font=('Helvetica', 12))
    style.configure('TFrame', background='#f0f0f0')

    # Add an icon (ensure you have an icon file named 'your_icon.ico')
    # root.iconbitmap('your_icon.ico')

    # Show the file dialog to select a video file
    video_path = filedialog.askopenfilename(title="Select the video file", filetypes=[("Video Files", "*.mp4;*.avi;*.mkv;*.flv;*.mov")])
    if not video_path:
        return

    # Save the selected video file to the 'input' directory
    dest_path = os.path.join("input", os.path.basename(video_path))
    with open(video_path, "rb") as fsrc:
        with open(dest_path, "wb") as fdst:
            fdst.write(fsrc.read())

    audio_format = simpledialog.askstring("Output Format", "Enter desired audio format (e.g. mp3, wav):", initialvalue="mp3")

    # Set the audio path in the 'output' directory with the same filename as the video (but different extension)
    output_filename = os.path.splitext(os.path.basename(dest_path))[0] + f".{audio_format}"
    audio_path = os.path.join("output", output_filename)
    
    success = extract_audio_from_video(dest_path, audio_path)

    if success:
        messagebox.showinfo("Success", f"Audio saved successfully at: {audio_path}")
    else:
        messagebox.showerror("Error", "Failed to extract audio. Please check the video file.")

if __name__ == "__main__":
    main()
