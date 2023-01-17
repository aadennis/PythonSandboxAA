import io
from google.cloud import speech

speech_file = "d:\\temp\\phone.wav"

client = speech.SpeechClient()

with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

# storage_uri = 'gs://YOUR_BUCKET_ID/path/to/your/file.wav'
# audio = speech.RecognitionAudio(uri=storage_uri)

# SpeechContext: to configure your speech_context see:
# https://cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#speechcontext
# Full list of supported phrases (class tokens) here:
# https://cloud.google.com/speech-to-text/docs/class-tokens
#speech_context = speech.SpeechContext(phrases=["$TIME"])
# speech_context = speech.SpeechContext(phrases=["$OOV_CLASS_ALPHANUMERIC_SEQUENCE"])
speech_context = speech.SpeechContext(phrases=["$OOV_CLASS_DIGIT_SEQUENCE"]) # ,"$OOV_CLASS_ALPHA_SEQUENCE"])
speech_context = speech.SpeechContext(phrases=["$FULLPHONENUM"]) # ,"$OOV_CLASS_ALPHA_SEQUENCE"])





# RecognitionConfig: to configure your encoding and sample_rate_hertz, see:
# https://cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#recognitionconfig
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code="en-GB",
    speech_contexts=[speech_context],
)

response = client.recognize(config=config, audio=audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("-" * 20)
    print("First alternative of result {}".format(i))
    print("Transcript: {}".format(alternative.transcript))

