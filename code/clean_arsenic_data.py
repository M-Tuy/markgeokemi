import geopandas as gpd
markgeokemi_regional= gpd.read_file (
    "C:/Projects/markgeokemi/raw_data/markgeokemi_regional.gpkg", 
    layer= "moran_0063mm_hno3_icpms"
)
arsenic_icpms= markgeokemi_regional[
    ["unikt_id", "geometry","ns", "ew", "prov_artal","provtyp", "as_ppm"]
].copy()
arsenic_icpms_clean= arsenic_icpms.dropna(
    subset=["as_ppm", "ns", "ew", "geometry"]
).copy() # remove NaN
arsenic_icpms_clean.to_file(
    "C:/Projects/markgeokemi/cleaned_data/arsenic_icpms_clean.gpkg", driver="GPKG"
) #save in cleaned data