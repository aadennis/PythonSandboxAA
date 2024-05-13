from ImageHandler import ImageHandler

source_dir = 'ImageHandling/tests/TestImageFiles/'
destination_dir = 'TestOutput'
handler = ImageHandler(source_dir, destination_dir)
handler.process_images()
