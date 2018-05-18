import numpy as np

#garbage_data = np.loadtxt('ALESS_data_improved.txt', usecols = [0, 46, 47, 53, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 114, 115, 116, 117, 118, 119], skiprows = 1) 
# 0 id , 53 z_phot, 60 VIMOS starts, first all fluxes, then errors, except 46, 47  # 60-78 Fluxes # errors 79-98 # 99-104 are SPIRE BANDS, again flux, error, .... etc.
# 114-119 MIPS and PACS BANDS, flux, error, .... etc.

garbage_data = np.loadtxt('ALESS_data_improved.txt', usecols = [0, 56], skiprows = 1) 

print garbage_data
