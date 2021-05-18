

import pandas as pd

#Read files
ContinuationsTransformations = pd.read_csv('ContinuationsTransformations.csv')
DomaineValeur = pd.read_csv('DomaineValeur.csv')
Entreprise = pd.read_csv('Entreprise.csv')
Etablissements = pd.read_csv('Etablissements.csv')
FusionScissions = pd.read_csv('FusionScissions.csv')
Nom = pd.read_csv('Nom.csv')


#Groups
grp1 = [2591,2592,2593,2599]
grp2 = [161,162,163,164,169]

#Consider this as base as it contains the grp codes
Entreprise = Entreprise[(Entreprise['COD_ACT_ECON_CAE'].isin(grp1+grp2)) | (Entreprise['COD_ACT_ECON_CAE2'].isin(grp1+grp2))]

unique_NEQ = Entreprise['NEQ'].unique()

#Select only NEQ from Entreprise
ContinuationsTransformations = ContinuationsTransformations[ContinuationsTransformations['NEQ'].isin(unique_NEQ)].drop_duplicates()
Etablissements = Etablissements[Etablissements['NEQ'].isin(unique_NEQ)].drop_duplicates()
FusionScissions = FusionScissions[FusionScissions['NEQ'].isin(unique_NEQ)].drop_duplicates()
Nom = Nom[Nom['NEQ'].isin(unique_NEQ)].drop_duplicates()

print("No of records in Entreprise- "+str(len(Entreprise)))
print("No of records in ContinuationsTransformations- "+str(len(ContinuationsTransformations)))
print("No of records in Etablissements- "+str(len(Etablissements)))
print("No of records in FusionScissions- "+str(len(FusionScissions)))
print("No of records in Nom- "+str(len(Nom)))

#Merge with other tables using NEQ
df = Entreprise.merge(ContinuationsTransformations,on='NEQ',how='left')

df = df.merge(Etablissements,on='NEQ',how='left')
df = df.merge(FusionScissions,on='NEQ',how='left')
df = df.merge(Nom,on='NEQ',how='left')

#Separate the tables
df_grp1 = df.copy()
df_grp1 = df_grp1[(df_grp1['COD_ACT_ECON_CAE'].isin(grp1)) | (df_grp1['COD_ACT_ECON_CAE2'].isin(grp1))]

df_grp2 = df.copy()
df_grp2 = df_grp2[(df_grp2['COD_ACT_ECON_CAE'].isin(grp2)) | (df_grp2['COD_ACT_ECON_CAE2'].isin(grp2))]

df_grp1.to_csv('df_grp1.csv',index=False)
df_grp2.to_csv('df_grp2.csv',index=False)
