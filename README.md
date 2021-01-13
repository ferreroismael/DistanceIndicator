# DistanceIndicator
This code allows to estimate the stellar mass of a galaxy by providing its  surface brightness and effective radii. See Ferrero et al. 2021 for more details.

There are two assumptions that must to be done:
1) A relation between stellar mass and halo mass 
2) A contracction model for the halo

-----Options-----
1) For the relation between galaxy stellar and halo mass there are 4 options:
  a) EAGLE simulation,      imput: 'EAGLE'
  b) TNG   simulation,      imput: 'TNG'
  c) Behroozi et al. 2019,  imput: 'B+19'
  d) Moster et al. 2018,    imput: 'M+18'
  
2) For the modeling of the halo contracction
  a) Gnedin,           imput: 'gnedin'
  b) Adiabatic,        imput: 'adiabatic'
  c) No contracction,  imput: 'nocontracction'
  
  
-----Imputs-----
Surface brightness, [Mo / kpc^2], in log
Effective radii, [kpc], in log

  
Examples:

- Asuming stellar to halo mass relation from EAGLE and no contraction 
Sigmae = [8]
Re = [2.4]
Dist_indicator(Sigmae,Re,'EAGLE','nocontracction')


- Asuming stellar to halo mass relation from Moster et al. 2018 and Gnedin contraction 
Sigmae = [8]
Re = [2.4]
Dist_indicator(Sigmae,Re,'B+18','gnedin')

