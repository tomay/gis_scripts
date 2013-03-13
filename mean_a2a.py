# c:\Python26\ArcGIS10.0\python.exe mean.py
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:\\atom\\GCMs\\clipped\\a2a\\cccma"
arcpy.CheckOutExtension("Spatial")

# get basic list of bio1, bio2, ... bio19
#biolist = arcpy.ListRasters("*", "tif")
biolist = ["bio1","bio2","bio3","bio4","bio5","bio6","bio7","bio8","bio9","bio10","bio11","bio12","bio13","bio14","bio15","bio16","bio17","bio18","bio19"]
# biolist = ["bio1","bio2","bio3"]

# Process: Cell Statistics...
outputdir = "C:\\atom\\GCMs\\clipped\\a2a\\mean\\"
for biorast in biolist:
  #the_grids = "'C:\\atom\\GCMs\\clipped\\a2a\\cccma\\ + biorast + ".tif";'C:\\atom\\GCMs\\clipped\\a2a\\csiro\\ + biorast + ".tif"';'C:\\atom\\GCMs\\clipped\\a2a\\hccpr\\' + biorast + ".tif"';'C:\\atom\\GCMs\\clipped\\a2a\\nies99' + biorast'"
  g1 = "C:\\atom\\GCMs\\clipped\\a2a\\cccma\\" + biorast + ".tif"
  g2 = "C:\\atom\\GCMs\\clipped\\a2a\\csiro\\" + biorast + ".tif"
  g3 = "C:\\atom\\GCMs\\clipped\\a2a\\hccpr\\" + biorast + ".tif"
  g4 = "C:\\atom\\GCMs\\clipped\\a2a\\nies99\\" + biorast + ".tif"
  print g1
  print g2
  print g3
  print g4
  outmean = CellStatistics([g1,g2,g3,g4], "MEAN")
  outmean.save("C:\\atom\GCMs\\clipped\\a2a\\_mean\\" + biorast + ".tif")
  arcpy.RasterToASCII_conversion(outmean, "C:\\atom\GCMs\\clipped\\a2a\\_mean\\" + biorast + ".asc")   
