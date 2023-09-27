from get_frames_from_video_inmem import get_frames 

def test_get_frames():
    input_file = r'D:\Sandbox\git\aadennis\PythonSandboxAA\VideoHandling\Stitch\test\assets\sup_asset.mp4'
    expected_duration = 55.55 # duration of source file
    start = 1
    stop = start + 5
    interval = 0.091
    output_file = "c:/temp/mavideox.mp4"

    ans = get_frames(input_file, start, stop, interval)
    assert ans.duration == expected_duration # token test of content being read OK
    #ans.write_videofile(output_file, codec = 'libx264',fps=24)
    print(ans)