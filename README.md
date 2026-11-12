# Inverse modelling of mineral reactions in groundwater using PHRERQC

**Author:** Marius Tuyishime. **Course: Geochemicalmodelling2026, exercise 5** 

---

**1. Introduction**

The chemistry of surface water and groundwater results from many interacting factors. These include atmospheric input, climate, topography, the mineral composition of the catchment, which in turn depend on water temperature, flow rate, the presence of a gas phase, and redox conditions. The process starts with the weathering of primary minerals. Over time, rocks and minerals at the Earth’s surface react with the atmosphere, water and living organisms. In most natural systems, the main source of protons (H⁺) is carbonic acid (H₂CO₃). It forms when soil CO₂ dissolves in water. Soil CO₂ is produced by the decomposition of organic matter and by root respiration. Its partial pressure in soil is higher than in the atmosphere. Protons attack mineral surfaces and release ions into solution. Secondary minerals, such as clays, then form by precipitation. Ion exchange, adsorption and desorption also control the dissolved ion content. Two examples are:

Albite weathers to kaolinite:
$2NaAlSi_3O_8 + 2CO_2 + 11H_2O \rightarrow Al_2Si_2O_5(OH)_4 + 2Na^+ + 2HCO_3^- + 4H_4SiO_4$

Calcite dissolves in carbonic acid:
$CO_2 + H_2O \rightleftharpoons H_2CO_3$
$CaCO_3 + H_2CO_3 \rightarrow Ca^{2+} + 2HCO_3^-$

Organic acids and ligands are other proton sources. They bind to mineral surfaces and speed up dissolution. Sulfuric acid forms where sulfide minerals, such as pyrite, oxidise.

1.2 Geochemical modelling

Differences in water chemistry result from water reacting with the surrounding rock. Other processes also act, such as plant uptake of carbon, gas exchange, and input of nutrients and metals. Geochemical modelling describes these interactions at the water-rock interface.

Inverse modelling explains the water chemistry by mineral reactions and gas exchange. It determines the mole transfers of phases that account for the change between an initial and a final water. It can show which primary minerals dissolve and which secondary minerals form. It can also show how much of a change comes from mixing and how much from reactions. It uses mass balance only, so it gives no reaction rates.

This exercise repeats the study of Garrels and Mackenzie (1967) on two groundwater springs in the Sierra Nevada. The ephemeral spring (solution 1) feeds the perennial spring (solution 2), which has reacted longer with the granitic bedrock. The aim is to find, with PHREEQC, the mineral and gas mole transfers that turn solution 1 into solution 2, and to judge which model is most reasonable.

## 2. Data and Method

This exercise repeats the study of Garrels and Mackenzie (1967) on two groundwater springs in the Sierra Nevada. The ephemeral spring (solution 1) feeds the perennial spring (solution 2), which has reacted longer with the granitic bedrock. The aim is to find, with PHREEQC, the mineral and gas mole transfers that turn solution 1 into solution 2, and to judge which model is most reasonable.

**Table 1 concentrations of some chemical species in the Sierra nevada springs** 
|Species|Sol. 1: Ephemeral|Sol.2: Perennial|
|---:|---:|---:|
|pH|6.2|6.8|
|$SiO_2$|0.273|0.410|
|$Ca^2^+$|0.078|0.260|
|$Mg^2$|0.029|0.071|
|$Na^1$|0.134|0.259|
|$K^1$|0.028|0.040|
|$HCO_3^1$|0.328|0.895|
|$SO_4^2^-$|0.010|0.025|
|$Cl^-$|0.014|0.030|

Data source: Garrels and Mackenzie (1967). concentration are expressed in mM.


**Site description and  and Hydrogeological description**



***Geology and Water-bearing formations and aquifer types***
- The methods used in this study include, a light litterature review data analysis using various software packages

**Geochemical modelling**

- Product: [markgeokemi-regional](https://www.sgu.se/produkter-och-tjanster/geologiska-data/geokemi--geologiska-data/markgeokemi/)


## 3. Results

Results and discussion

models differences
3.1 Physical and chemical characteristics of surface water

- temp, pH, el conductivity
- Processes controlling major solute distributions in surface water
- Saturation index (SI) is a factor that indicates mineral saturation due to water chemistry.
- The study of the Ca/Mg ratio of water samples can be used to indicate dissolution of calcite or dolomite
- Geochemical modelling




As hotspots (top 5%, red) among all cleaned sample points (Fig. 1).

![Arsenic screening map](results/arsenic_screening_map.png)

Table model 1:

| Minerals | Moles | Minimum | Maximum | Formula | SI in sol 1, 2 |
|---|---:|---:|---:|---|---|
| Halite | 1.600e-05 | 1.490e-05 | 1.710e-05 | NaCl | (-10.32, -9.72) |
| Gypsum | 1.500e-05 | 1.413e-05 | 1.588e-05 | CaSO4:2H2O | (-4.62, -3.77) |
| Kaolinite | -1.282e-04 | -1.403e-04 | -1.159e-04 | Al2Si2O5(OH)4 | - |
| CO2(g) | 3.143e-04 | 2.493e-04 | 3.798e-04 | CO2 | (-1.87, -2.05) |
| Calcite | 1.028e-04 | 8.680e-05 | 1.182e-04 | CaCO3 | (-3.30, -1.77) |
| Chalcedony | -1.084e-04 | -1.473e-04 | -6.906e-05 | SiO2 | (-0.01, 0.16) |
| Biotite | 1.370e-05 | 1.317e-05 | 1.370e-05 | KMg3AlSi3O10(OH)2 | - |
| Plagioclase | 1.758e-04 | 1.582e-04 | 1.935e-04 | Na0.62Ca0.38Al1.38Si2.62O8 | - |


Table: model 2

| Minerals | Moles | Minimum | Maximum | Formula | SI in sol 1, 2 |
|---|---:|---:|---:|---|---|
| Halite | 1.600e-05 | 1.490e-05 | 1.710e-05 | NaCl | (-10.32, -9.72) |
| Gypsum | 1.500e-05 | 1.413e-05 | 1.588e-05 | CaSO4:2H2O | (-4.62, -3.77)  |
| Kaolinite | -3.392e-05 | -5.587e-05 | -1.224e-05 | Al2Si2O5(OH)4 | - |
| Ca-Montmorillon | -8.090e-05 | -1.100e-04 | -5.154e-05 | Ca0.165Al2.33Si3.67O10(OH)2 | - |
| CO2(g) | 3.009e-04 | 2.365e-04 | 3.659e-04 | CO2 | (-1.87, -2.05) |
| Calcite | 1.161e-04 | 1.007e-04 | 1.309e-04 | CaCO3 | (-3.30, -1.77) |
| Biotite | 1.370e-05 | 1.317e-05 | 1.370e-05 | KMg3AlSi3O10(OH)2 | - |
| Plagioclase | 1.758e-04 | 1.582e-04 | 1.935e-04 | Na0.62Ca0.38Al1.38Si2.62O8 | - |








## 4. Discussion

## 5. Limitations

## 8. References

1. Stumm, W. and Morgan, J.J. (1981). (Sweden)Aquatic Chemistry: An Introduction Emphasizing 
Chemical Equilibria in Natural Waters.  2nd Edition, John Wiley & Sons Ltd., New York.
