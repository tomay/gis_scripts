# To run from regular cmd prompt
# c:\Python26\ArcGIS10.0\python.exe c:\atom\GCMs\python\scale_worldclim.py
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:\\atom\\GCMs\\1950_2000\\clipped\\"
inputdir = "C:\\atom\\GCMs\\1950_2000\\clipped\\"
outputdir = "C:\\atom\\GCMs\\1950_2000\\scaled\\"
arcpy.CheckOutExtension("Spatial")

# get basic list of bio1, bio2, ... bio19
biolist = ["bio1","bio2","bio3","bio4","bio5","bio6","bio7","bio8","bio9","bio10","bio11","bio12","bio13","bio14","bio15","bio16","bio17","bio18","bio19"]
# Test set: biolist = ["bio1","bio2","bio3"]

# Process: Spatial analysis...
for biorast in biolist:
  #Get the geoprocessing result object
  araster = inputdir + biorast + ".tif"
  print("current: " + araster)
  rmin = arcpy.GetRasterProperties_management(araster, "MINIMUM")
  rmax = arcpy.GetRasterProperties_management(araster, "MAXIMUM")
  maxRaster = CreateConstantRaster(rmax,"FLOAT",arcpy.Describe(araster).MeanCellHeight,arcpy.Describe(araster).extent)
  minRaster = CreateConstantRaster(rmin,"FLOAT",arcpy.Describe(araster).MeanCellHeight,arcpy.Describe(araster).extent)
  rscale = ((araster - minRaster) / (maxRaster - minRaster)) * 255
  #Get the elevation standard deviation value from geoprocessing result object
  #rout = rscale.getOutput(0) 
  rscale.save(outputdir + biorast + ".tif")
  arcpy.RasterToASCII_conversion(rscale, outputdir + biorast + ".asc")  
