import geopandas as gpd
import pandas as pd
import numpy as np

# Read raw data (_icpms)
gpd.options.io_engine = "pyogrio" #by default it will be applied to read_file
markgeokemi_icpms = gpd.read_file(
    "C:/Projects/markgeokemi/raw_data/markgeokemi_regional.gpkg",
    layer = "moran_0063mm_hno3_icpms",
    use_arrow = True
).dropna(subset=["unikt_id", "ns", "ew", "geometry"]
).set_crs("EPSG:3006", allow_override=True) #remove NaN
markgeokemi_icpms_clean = markgeokemi_icpms.copy()
markgeokemi_icpms.to_file(
     "C:/Projects/markgeokemi/cleaned_data/markgeokemi_icpms_clean.gpkg",
    driver= "GPKG",
    use_arrow = True) #save cleaned raw_data
u_icpms = markgeokemi_icpms_clean[
    markgeokemi_icpms_clean["u_ppm"] > 0
][["unikt_id", "ns", "ew", "u_ppm", "geometry"]] #filter rows, condition: values in column u_ppm >0
#summary stats
u_icpms_stat = u_icpms["u_ppm"].describe()
median_u_icpms = u_icpms["u_ppm"].median()
skew_u_icpms = u_icpms["u_ppm"].skew()
print(f" summary:")
print(u_icpms_stat.round(2))
print(f" Median {median_u_icpms:.2f}")
print(f"Skewness {skew_u_icpms:.2f}")
u_95_thresh = u_icpms["u_ppm"].quantile(0.95)
u_75_thresh = u_icpms["u_ppm"].quantile(0.75)
u_50_thresh = u_icpms["u_ppm"].quantile(0.50)
u_25_thresh = u_icpms["u_ppm"].quantile(0.25)