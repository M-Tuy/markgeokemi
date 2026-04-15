import geopandas as gpd

# Read raw data (_icpms) and save cleaned data
gpd.options.io_engine = "pyogrio" #by default pyogrio will be applied to read_file
markgeokemi_icpms = gpd.read_file(
    "C:/Projects/markgeokemi/raw_data/markgeokemi_regional.gpkg",
    layer = "moran_0063mm_hno3_icpms",
    use_arrow = True
).dropna(subset=["unikt_id", "ns", "ew", "geometry"]
).set_crs("EPSG:3006", allow_override=True) #remove NaN
markgeokemi_icpms.head()
markgeokemi_icpms.to_file(
     "C:/Projects/markgeokemi/cleaned_data/markgeokemi_icpms_clean.gpkg",
    driver= "GPKG",
    use_arrow = True) #save in cleaned raw_data
