from PIL import Image, ImageSequence, ImageChops

def merge_gif_frames(gif_path, output_path):
    gif = Image.open(gif_path)
    frames = [frame.convert("1") for frame in ImageSequence.Iterator(gif)]

    # Create an output image with the same size as the frames, filled with white
    output_image = Image.new("1", frames[0].size, 1)

    # Use ImageChops.darker to keep the darker (black) pixels in the final image
    for frame in frames:
        output_image = ImageChops.darker(output_image, frame)

    output_image.save(output_path)

# Usage
merge_gif_frames('flag_1.gif', 'flag_1.png')
merge_gif_frames('flag_2.gif', 'flag_2.png')
