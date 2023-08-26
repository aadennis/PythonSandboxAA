from moviepy.editor import VideoFileClip, concatenate_videoclips

src_root = "C:/Users/Dennis/Videos/"
dest_root = "c:/tempx/"
avi_files = [src_root + 'MOVI0000.mp4',src_root + 'MOVI0002.mp4' ]

# List of AVI file paths
#avi_files = ['file1.avi', 'file2.avi', 'file3.avi']

# Convert AVI files to temporary MP4 files
temp_mp4_files = []
for avi_file in avi_files:
    temp_mp4_file = avi_file.replace('.avi', '_temp.mp4')
    clip = VideoFileClip(avi_file)
    clip.write_videofile(temp_mp4_file, codec='libx264')
    temp_mp4_files.append(temp_mp4_file)

# Load each temporary MP4 video clip
video_clips = [VideoFileClip(file) for file in temp_mp4_files]

# Concatenate the video clips
final_clip = concatenate_videoclips(video_clips)

# Write the final concatenated video to an MP4 file
final_clip.write_videofile('output.mp4', codec='libx264')


