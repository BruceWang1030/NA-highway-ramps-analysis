from UliEngineering.Utils.Files import *
from UliEngineering.Utils.ZIP import *
import shapefile
# List files inside ZIP
zipcontents = list(list_zip("./lrnf00r18a_e/lrnf00r18a_e.zip"))
# Find one filename that is present with ".shp", ".dbf" and ".prj" extensions
dataset_filenames = list(find_datasets_by_extension(
    zipcontents, (".shp", ".dbf", ".prj")))
# Read the files (copy to memory)
dataset = read_from_zip(
    "./lrnf00r18a_e/lrnf00r18a_e.zip", dataset_filenames[0])
# Read shapefile format
sf = shapefile.Reader(shp=dataset[0], dbf=dataset[1], prj=dataset[2])
# Do something useful with the reader

print(len(sf))
