# Geologiska arsenikhotspots i fokus 


## Data
## Information on how the work done
Downloade markgeokemi data from SGU. One file "markgeokemi_regional.gpkg" is was large, so was not pushed to the Git rep.
Created Git repository markgeokemi and cloned into my local folder.
### markgeokemi_regional.gpkg File not tracked yet

## Data selection
 
**Core dataset**: 
- moran_0063mm_hno3_icpms HNO<sub>3</sub>-extractable as (_ppm), for environmental risk screening
- moran_0063mm_totalhalt_xrf as the total (_ppm) as in the soil matrix
- moran_0063mm_ph, pH data
- fe_ppm → arsenic host mineral association

## location id
unikt_id
ns
ew
prov_artal
provtyp
geometry


## Information on how the work done
Downloade markgeokemi data from SGU. One file "markgeokemi_regional.gpkg" is was large, so was not pushed to the Git rep.
Created Git repository markgeokemi and cloned into my local folder.
### markgeokemi_regional.gpkg File not tracked yet

## Now extracted uranium and pH data from **moran_0063mm_ph**

Data cleaned. uranium, there were missing values, removed

Find matching common sample points using **unikt_id**, unikt id kombinerar idnr och idkod 


# Uranium

![Geological uranium vs pH](Uranium_pH.png) 
Elevated concrentration of uranium have been measured in the drinking water from private well.
Main concern, radioactivity and mainly toxicity, e.g. kidney.
In the dataset merged with pH values, the measured total uranium concentration in the geological materials ranges between **0.1** and **75.6** ppm.

![Uranium total concentration as a function of pH in privated wll](Uranium_in_private_well_pH.png)
Within the pH range 6.7-7.8, uranium occurs dominantly in the form of neutrally charged complexes.   
Such U form is common in private drilled well. Possibily Ca<sub>2</sub>UO<sub>2</sub>(CO<sub>3</sub>)<sub>3</sub><sup>0</sup> but as the pH becomes more alkaline, this the CaUO<sub>2</sub>(CO<sub>3</sub>)<sub>3</sub><sup>2−</sup> forms.


![Geological uranium vs Ca](Uranium_Calcium.png)
Calcium concentration is a key factor in determining the neutral uranium  Ca<sub>2</sub>UO<sub>2</sub> complexes
The figure below shows relationship between Ca and U on log-log-scale. The relationship is non linear.
- at low to moderate Ca concentrations, around 10<sup>2</sup>-10<sup>4</sup>, U shows wider ranges and highest observed values.
- At high Ca concentrations, above 10<sup>4</sup>-10<sup>5</sup>, U tends to be lower and less variable.
This suggest that at high Ca levels leads to U immobilization or dicrease in dissolved U concetrations. Geochemically, this may indicate:

high Ca favors formation of Ca-uranyl-carbonate complexes,
or high-Ca environments correspond to lithologies/waters with lower uranium mobility or source availability. However, at low Ca ranges, other factors such as pH, organic matter are likely more important.





 ### Arsenic concentration as a function of pH

 ![Geological arsenic vs pH](Uranium_pH.png)    

and 

 ![Geological arsenic vs pH](correlation_Arsenic_vs_pH.png)   
