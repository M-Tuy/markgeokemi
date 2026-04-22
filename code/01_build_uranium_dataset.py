import geopandas as gpd
from pyproj import Transformer
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

gpd.options.io_engine = "pyogrio" #faster engine
markgeokemi_icpms = gpd.read_file(
    "C:/Projects/markgeokemi/raw_data/markgeokemi_regional.gpkg",
    layer = "moran_0063mm_hno3_icpms",
    use_arrow = True
)
#Drop rows with missing ID/coordinates, ensure SWEREF system 
markgeokemi_icpms_clean = markgeokemi_icpms.dropna(   
    subset=[
        "unikt_id", "ns", "ew", "geometry"
    ]).set_crs("EPSG:3006", allow_override=True) 
# save cleaned data to GeoPackage
markgeokemi_icpms_clean.to_file(
     "C:/Projects/markgeokemi/cleaned_data/markgeokemi_icpms_clean.gpkg",
    driver= "GPKG",
    use_arrow = True
)

#geographic bbox in WGS84; convert to SWEREF 99 TM
min_lat, max_lat = 59.20, 59.95
min_lon, max_lon = 17.30, 18.30
trans = Transformer.from_crs(
    "EPSG:4326",
    "EPSG:3006",
    always_xy = True
)
# convert bbox corners
min_ew, min_ns = trans.transform(min_lon, min_lat)  
max_ew, max_ns = trans.transform(max_lon, max_lat)

# keep valid (measured, >0) uranium values within defined bbox
#0 → removes 0 (not analyzed
as_stoch_upp = markgeokemi_icpms_clean[
    (markgeokemi_icpms_clean["u_ppm"].notna()) & #removes missing values
    (markgeokemi_icpms_clean["u_ppm"] > 0) & # > 0 removes not analysed & below detection
    (markgeokemi_icpms_clean["ew"].between(min_ew, max_ew)) &
    (markgeokemi_icpms_clean["ns"].between(min_ns, max_ns))
][["unikt_id", "ns", "ew", "as_ppm", "geometry"]
].copy()

#summary stats for defined bbox
u_stoch_upp_stat = u_stoch_upp["u_ppm"].describe()
median_u_stoch_upp = u_stoch_upp["u_ppm"].median()
skew_as_stoch_upp = as_stoch_upp["u_ppm"].skew()

# define 95th percentile threshold; select top 5% (hotspots)
thresh_95 = u_stoch_upp["u_ppm"].quantile(0.95)
u_stoch_upp_hotspots = u_stoch_upp[
    u_stoch_upp["u_ppm"] >= thresh_95
].copy()
#report summary stats and hotspot metrics
print(f" report summary stats and hotspot metrics:")
print(u_stoch_upp_stat.round(2))
print(f" median {median_u_stoch_upp:.2f}")
print(f"skewness {skew_u_stoch_upp:.2f}")
print(f"Hotspot threshold (95th percentile): {thresh_95:.2f} ppm")
print(f"Number of hotspot samples: {len(u_stoch_upp_hotspots)}")

fig, ax = plt.subplots(figsize=(7, 7))
u_stoch_upp.plot(
    ax=ax,
    color="lightgrey",
    markersize=10,
    alpha=0.7
)
u_stoch_upp_hotspots.plot(
    column="as_ppm",
    legend=True,
    ax=ax,
    markersize=45
)
ax.set_title("uranium Hotspots, Stockholm–Uppsala Region")
plt.savefig(
    "C:/Projects/markgeokemi/results/uranium_stockholm_Uppsala_map.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

#Fe data 
fe_stoch_upp = markgeokemi_icpms_clean[
    (markgeokemi_icpms_clean["fe_ppm"].notna()) & #removes missing values
    (markgeokemi_icpms_clean["fe_ppm"] > 0) & # > 0 removes not analysed & below detection
    (markgeokemi_icpms_clean["ew"].between(min_ew, max_ew)) &
    (markgeokemi_icpms_clean["ns"].between(min_ns, max_ns))
][["unikt_id", "ns", "ew", "fe_ppm", "geometry"]
].copy()
print(fe_stoch_upp.shape)

valid = (fe_stoch_upp["fe_ppm"] > 0) & (u_stoch_upp["u_ppm"] > 0)

fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(
    np.log10(fe_stoch_upp.loc[valid, "fe_ppm"]),
    np.log10(u_stoch_upp.loc[valid, "u_ppm"]),
    s=25,
    alpha=0.5
)
ax.set_xlabel("log10(Fe_ppm)")
ax.set_ylabel("log10(As_ppm)")
ax.set_title("Arsenic vs Iron")
plt.savefig(
    "C:/Projects/markgeokemi/results/as_fe_stockholm_Uppsala.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()