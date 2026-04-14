import geopandas as gpd
gpd.options.io_engine = "pyogrio"
arsenic_icpms_clean = gpd.read_file(
    "C:/Projects/markgeokemi/raw_data/markgeokemi_regional.gpkg",
    layer = "moran_0063mm_hno3_icpms",
    columns = ["unikt_id", "geometry", "ns", "ew", "prov_artal", "provtyp", "as_ppm"],
    engine = "pyogrio",
    use_arrow = True
).dropna(subset=["as_ppm", "ns", "ew", "geometry"]).copy() # remove NaN
arsenic_icpms_clean.to_file(
    "C:/Projects/markgeokemi/cleaned_data/arsenic_icpms_clean.gpkg", driver="GPKG"
) #save in cleaned data
arsenic_icpms_clean = arsenic_icpms_clean.set_crs("EPSG:3006", allow_override=True)#assign CRS, update
arsenic_icpms_clean.crs