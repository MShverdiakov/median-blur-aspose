import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage
from aspose.imaging.imagefilters.filteroptions import MedianFilterOptions
import os



image_folder = r".\images"

delete_output = False #'SAVE_OUTPUT' not in os.environ
data_dir = image_folder

with Image.load(os.path.join(data_dir, "image.jpg")) as image:
	if aspycore.is_assignable(image, RasterImage):
		raster_image = aspycore.as_of(image, RasterImage)

		options = MedianFilterOptions(8)
		raster_image.filter(image.bounds, options)
		image.save(os.path.join(data_dir, "result.jpg"))

if delete_output:
	os.remove(os.path.join(data_dir, "result.jpg"))