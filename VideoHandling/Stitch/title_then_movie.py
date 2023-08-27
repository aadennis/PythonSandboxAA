from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips

JPG_PATH = 'c:/tempx/piano.jpg' # save as test image
MP4_PATH = 'c:/tempx/output.mp4'
MP4_PATH2 = 'c:/tempx/shorty.mp4'

OUTPUT_PATH = 'c:/tempx/output_videox3.mp4'
CLIP_OUTPUT = 'c:/tempx/clip_output.mp4'
IMAGE_DURATION=3
CODEC = 'libx264'

jpg_image = ImageClip(JPG_PATH, duration=IMAGE_DURATION)
jpg_image.write_videofile(CLIP_OUTPUT, codec=CODEC, fps=30)

# Load the MP4 video
image_clip = VideoFileClip(CLIP_OUTPUT)
video_clip = VideoFileClip(MP4_PATH)
video_clip2 = VideoFileClip(MP4_PATH2)

# The next lines amount to this:
# If 2 video clips are cat'ed, fine.
# If a video clip and an image clip are cat'ed, then whatever
# comes second, scrolls like mad. argh. Check it in anyway, as it's
# learning of a sort.
# Docs at https://zulko.github.io/moviepy/ref/ref.html say that ImageClip
# is "just" a still version of a VideoClip... but tests suggest not quite.
final = concatenate_videoclips([video_clip2, video_clip])
#final = concatenate_videoclips([image_clip, video_clip])
#final = concatenate_videoclips([video_clip2, jpg_image])

final.write_videofile(OUTPUT_PATH,codec='libx264',fps=30)

print(f"Image-as-video is saved at [{OUTPUT_PATH}]")

