from ImageHandler import ImageHandler
import config

handler = ImageHandler(config.source_dir, config.destination_dir)
handler.process_images()
