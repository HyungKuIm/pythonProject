import ffmpeg
# path = 'C:/Users/daman/PycharmProjects/pythonProject/starwars.mp4'
# video_info = ffmpeg.probe(path)
# print(video_info)

stream = ffmpeg.input('starwars.mp4')
audio_stream = stream.audio
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, audio_stream, 'output.mp4')
ffmpeg.run(stream)

# stream = ffmpeg.input('starwars.mp4').hflip().output('output.mp4')
# ffmpeg.run(stream)