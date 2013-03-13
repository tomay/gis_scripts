# From regular dos cmd window
# c:\Python26\ArcGIS10.0\python.exe mean.py
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:\\atom\\GCMs\\clipped\\b2a\\all_mean"
arcpy.CheckOutExtension("Spatial")

# get basic list of bio1, bio2, ... bio19
#biolist = arcpy.ListRasters("*", "tif")
biolist = ["bio1","bio2","bio3","bio4","bio5","bio6","bio7","bio8","bio9","bio10","bio11","bio12","bio13","bio14","bio15","bio16","bio17","bio18","bio19"]

# Process: Cell Statistics...
outputdir = "C:\\atom\\GCMs\\clipped\\b2a\\all_mean\\"
for biorast in biolist:
  g1 = "C:\\atom\\GCMs\\clipped\\b2a\\cccma\\" + biorast + ".tif"
  g2 = "C:\\atom\\GCMs\\clipped\\b2a\\csiro\\" + biorast + ".tif"
  g3 = "C:\\atom\\GCMs\\clipped\\b2a\\hccpr\\" + biorast + ".tif"
  g4 = "C:\\atom\\GCMs\\clipped\\b2a\\nies99\\" + biorast + ".tif"
  print g1
  print g2
  print g3
  print g4
  outmean = CellStatistics([g1,g2,g3,g4], "MEAN")
  outmean.save(outputdir + biorast + ".tif")
  arcpy.RasterToASCII_conversion(outmean, outputdir + biorast + ".asc")  
