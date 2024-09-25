import tkinter as tk

def calculate():
    try:
        # Get user input values
        bitrate_kbps = float(bitrate_entry.get())
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
        number_of_segments = int(segments_entry.get())

        # Convert bitrate to bits per second (bps)
        bitrate_bps = bitrate_kbps * 1000

        # Convert duration to total seconds
        video_duration_seconds = (hours * 3600) + (minutes * 60) + seconds

        # Calculate total video size in bytes
        total_video_size_bytes = (bitrate_bps / 8) * video_duration_seconds

        # Convert total video size to megabytes (MB)
        total_video_size_MB = total_video_size_bytes / (1024 * 1024)

        # Calculate required download speeds for different percentages
        percentages = [50, 60, 70, 75]
        results = []

        for percent in percentages:
            desired_download_time_seconds = (percent / 100) * video_duration_seconds
            required_speed_MBps = total_video_size_MB / desired_download_time_seconds
            results.append((percent, required_speed_MBps))

        # Update the results in the GUI
        result_text = f"Total Video Size: {total_video_size_MB:.2f} MB\n\n"
        for percent, speed in results:
            result_text += f"To download video in its {percent}% of runtime: {speed:.2f} MBps (MegaBytes Per Second)\n"

        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Please enter valid numbers in all fields.")

# Create the main window
root = tk.Tk()
root.title("Video Download Speed Calculator")

# Create and place labels and entry fields
tk.Label(root, text="Video Bitrate:").grid(row=0, column=0, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Bitrate (kbps):").grid(row=1, column=0, padx=10, pady=10)
bitrate_entry = tk.Entry(root)
bitrate_entry.grid(row=1, column=1, padx=10, pady=10)

# Heading for video duration
tk.Label(root, text="Video Duration:").grid(row=2, column=0, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Hours:").grid(row=3, column=0, padx=10, pady=10)
hours_entry = tk.Entry(root)
hours_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Minutes:").grid(row=4, column=0, padx=10, pady=10)
minutes_entry = tk.Entry(root)
minutes_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Seconds:").grid(row=5, column=0, padx=10, pady=10)
seconds_entry = tk.Entry(root)
seconds_entry.grid(row=5, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Segments:").grid(row=6, column=0, padx=10, pady=10)
segments_entry = tk.Entry(root)
segments_entry.grid(row=6, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
