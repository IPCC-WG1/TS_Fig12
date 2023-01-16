# TS_Fig12
Figure TS.12 shows land-related changes relative to the 1850-1900 as a function of global warming levels. 
![Figure TS.12](IPCC_AR6_WGI_TS_Figure_12.png?raw=true)

Figure subpanels

The figure has six panels, with input data provided for all panels in subdirectories named Extremes,  ModelSnow/sncbin and WaterCyclePanels.

List of data provided
This dataset contains:
- Relative frequency and intensity changes of 1-in-10- and 1-in-50-year extreme daily heat (TXx) in CMIP6 models (ScenarioMIP) with respect to 1850-1900. Medians and 5, 17, 83, 95 percentiles.
- Relative frequency and intensity changes of 1-in-10- and 1-in-50-year extreme daily precipitation rates (Rx1day) in CMIP6 models (ScenarioMIP) with respect to 1850-1900. Medians and 5, 17, 83, 95 percentiles.
- Relative frequency and intensity changes of 1-in-10-year drought events in CMIP6 models (ScenarioMIP) with respect to 1850-1900. Medians and 5, 17, 83, 95 percentiles.
- Monthly NH snow cover extent changes (in %), dependent on the GWL (with respect to 1850-1900), for CMIP6 models (historical + ScenarioMIP), with respect to snow cover extent at 0°C GWL (1850-1900)
- Average precipitable water (annual mean), precipitation rate (annual mean + interannual variability), and runoff (annual mean + interannual variability) over tropical land (|latitude|<30°), in the CMIP6 models that reach +5°C GWL in SSP5-8.5.
- Average precipitable water (annual mean), precipitation rate (annual mean + interannual variability), and runoff (annual mean + interannual variability) over tropical land (|latitude|>30°), in the CMIP6 models that reach +5°C GWL in SSP5-8.5.

Data provided in relation to figure

Panel a:
- Data file: Extremes/TXx_freq_change_10_year_event.csv; relates to the orange clock symbols and small orange 3-pronged symbols above and below.
- Data file: Extremes/TXx_intens_change_10_year_event.csv; relates to the orange thermometer symbols and small orange 3-pronged symbols above and below.
- Data file: Extremes/TXx_freq_change_50_year_event.csv; relates to the brown clock symbols and small orange 3-pronged symbols above and below.
- Data file: Extremes/TXx_intens_change_50_year_event.csv; relates to the brown thermometer symbols and small orange 3-pronged symbols above and below.

Panel b:
- Data file: Extremes/Rx1day _freq_change_10_year_event.csv; relates to the orange clock symbols and small orange 3-pronged symbols above and below.
- Data file: Extremes/Rx1day _intens_change_10_year_event.csv; relates to the orange rain cloud symbols and small orange 3-pronged symbols above and below.
- Data file: Extremes/Rx1day _freq_change_50_year_event.csv; relates to the brown clock symbols and small orange 3-pronged symbols above and below.
- Data file: Extremes/Rx1day _intens_change_50_year_event.csv; relates to the brown rain cloud symbols and small orange 3-pronged symbols above and below.

Panel c:
- Data file: Extremes/drought _freq_change_10_year_event.csv; relates to the orange clock symbols and small orange 3-pronged symbols above and below.
- Data file: Extremes/drought _intens_change_10_year_event.csv; relates to the orange drop symbols and small orange 3-pronged symbols above and below.

Panel d:
Data files: sncbin/sncbin_{model}_historical+ssp{xyy}.nc. For each model and scenario, these files contain a table that gives the snow cover extent changes for each month of the year and for 0.2°C-wide temperature bins. The colours represent the 5 scenarios (see legend, standard IPCC scenario colour code). Each dot represents one GWL (0.2°C bins) for one model and one scenario. The linear multi-model regression lines are coloured dependent on the scenario they represent.

Panel e:
- Data files: WaterCyclePanels/Hydro_vars_change_20210201_derived_tropic.json. Multi-model mean precipitable water, precipitation, and runoff (annual mean and interannual variability (standard deviation)).

Left part of the panel:

* Black full line: Precipitable water, annual mean, multi-model mean

* Brown full line: Runoff, annual mean, multi-model mean

* Brown dashed line: Runoff, interannual variability, multi-model mean

* Blue full line: Precipitation, annual mean, multi-model mean

* Blue dashed line: Precipitation, interannual variability, multi-model mean

Right part of the panel: 17-83% inter-model ranges for the +5°C GWL.
Notes on reproducing the figure from the provided data.

Panel a:
The Python script Extremes/TS2-Land-Extremes-202110.py reads the csv data sheets and plots the panel.

Panel b:
The Python script Extremes/TS2-Land-Extremes-202110.py reads the csv data sheets and plots the panel.

Panel c:
The Python script Extremes/TS2-Land-Extremes-202110.py reads the csv data sheets and plots the panel.

Panel d:
The Python script ModelSnow/AR6TS2-Snow.py reads the csv data sheets and plots the panel.

Panel e:
The Python script WaterCyclePanels/TS12-WaterCycle.py reads the json data sheets and plots the panel.

All the cvs data above are available in the CEDA catalogue here:  
