from moviepy.editor import VideoFileClip, concatenate_videoclips

INPUT_VIDEO = "c:/VideoStaging/mp4Joined.mp4"
OUTPUT_VIDEO = "c:/VideoStaging/shorty.mp4" 

video_clip_set = []
video_clip_set.append(VideoFileClip(INPUT_VIDEO).subclip(50,50+10))
video_clip_set.append(VideoFileClip(INPUT_VIDEO).subclip(60+50,60+50+10))
video_clip_set.append(VideoFileClip(INPUT_VIDEO).subclip(60+60+50,60+60+50+10))

final_clip = concatenate_videoclips(video_clip_set, method="compose")
final_clip.write_videofile(OUTPUT_VIDEO, codec='libx264')
