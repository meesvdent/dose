# dose
Chemical focus


This script integrates a set of differential equations forward in time using scipy.integrate
that together describe the pharmacokinetic properties of a drug as follows:


    kabs            k1           kon  
  I  --->   Iblood  ----> Itissue ---->  EI  
            |       <----         <----  
            | kout   k2           koff  
           \/


   where kout is the sum of the rates of elimination and metabolism.
 All rates are in units of 1/s, except for kon, which is in 1/(M s).
 Concentrations are in mol/L, and time is in seconds.

 All species are described in the system vector X:
   X = [Iblood, Itissue, f]

 All rates are described in the rate vector R:
   R = [kabs, kout, k1, k2, kon, koff]

   where [E] = (1-f)Etot and [EI] = f*Etot
     and Etot is the total concentration of target protein

 Alex Dickson  
 Michigan State University, 2016