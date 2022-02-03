#myTDFcalc python program 
#TDFcalc calculates whether any number fraction needs to be added to present treatment course if a patient has discontinued the treatment and restarts the treatment after a gap due to any reason
#TDFstands_time_dose_fraction
######################################################################
#tdf_tot is total tdf of the treatment regime
#n1 is the total number of fractions inthe treatment course
#d is the total dose per fraction

def tdf_tot(n1,d):
  tdf_t=n1*(d)**1.538*(7/5)**(-0.169)*10**-3
  return tdf_t
 
 
n1=input('Total number of fractions ')
d=input('Please enter dose per fraction in cGy ')

n1=int(n1)
d=int(d)

tdf_t=tdf_tot(n1,d)
print(f"Total TDF for treatment {tdf_t}")

######################################################
#tdf_del is the total tdf delivered before the patient discontinued the treatment in between the course
#d is dose per fraction in cGy
#n2 is the number of fractions delivered before the before the patient discontinued the treatment in between the course

def tdf_del(d,n2):
 tdf_d=n2*(d)**1.538*(7/5)**(-0.169)*10**-3
 return tdf_d 
 
n2=input('Number of fractions already delivered before gap ')

n2=int(n2)

tdf_d=tdf_del(d,n2)
print(f"TDF delivered in the treatment by now,before the gap is {tdf_d}")

#################################################################
#gap_factor is the gap correction factor accounts for gap of discontinuty in the treatment course
#t is the total number of calender days before the gap
#g is the gap days in the treatment course
#r is the sum of the total days and gap days
def gap_factor(t,g):
 r=t+g
 gap=(t/r)**0.11
 return gap
 
t=input('Total number of calender days ')
g=input('Gap days ')

t=int(t)
g=int(g)

gap=gap_factor(t,g)
print(f"Gap correction factor is {gap}")

####################################################################
#tdf_corr is the corrected  tdf of the course
tdf_corr=(gap)*(tdf_d)
print(f"Corrected TDF for the treatment is {tdf_corr}")
#tdf_rem is the remaining tdf to be delivered after gap 
tdf_rem=(tdf_t)-(tdf_corr)
print(f"Remaining TDF for the treatment is {tdf_rem}")
#num_frac is the number of fraction of remaining tdf
p=(d)**1.538*(7/5)**(-0.169)*10**-3
num_frac=(tdf_rem)/(p)
print(num_frac) 
print(f"Number of fractions for the treatment course from the time of restart of treatment are {num_frac}")