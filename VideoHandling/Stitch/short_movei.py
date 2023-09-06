input_video = "E:\\Den\\VideoDump\\VideoAssets\\13second_test_vid.mp4"
output_video = "E:\\Den\\VideoDump\\VideoAssets\\tiny_video2.mp4"

from moviepy.editor import VideoFileClip, ImageSequenceClip

# Load the original video
clip = VideoFileClip(input_video)

print(clip.duration)

# Select the frames you want (frame 4, 7, and 10 in this case)
frame_numbers = [1,3,5,82]

# Extract the selected frames
# new_frames = []
# for i in frame_numbers:
#     a = clip.get_frame(i)

new_frames = [clip.get_frame(i) for i in frame_numbers]

frame_duration = 2 # in seconds

# Create a new video from the selected frames
new_clip = ImageSequenceClip(new_frames, fps=clip.fps) # , durations=frame_duration)

# Write the new video to 'new.mp4'
new_clip.write_videofile(output_video, codec="libx264")

