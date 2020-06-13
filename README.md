# Covid-19-Drug-Discovery

🕵️ Introduction
The objective is to prepare a machine learning model that can be used to propose potential novel effective drugs to fight SARS-CoV-2, the virus responsible for COVID-19.

You are provided with a dataset containing drug molecules (encoded as SMILES) and their binding affinities. The task is to use this dataset to make a regression model for binding affinity prediction. You will be evaluated on Root Mean Squared Error (RMSE).

💾 Dataset
SARS-CoV-2 virus contains proteins responsible for action and replication of the virus. The protein functions can be stopped by introducing drug molecules that are capable of blocking the protein. In other words, preparation of a drug involves finding molecules that can effectively bind to the protein i.e have a high binding affinity.
In this task, you are provided with a dataset of drug molecules and their binding affinity towards SARS-CoronaVirus Main Proteaese(Mpro), one of the proteins in the target virus.
The data has been generated using Protein-Ligand docking.

SMILES REPRESENTATION OF MOLECULES -
SMILES are character strings to represent drug molecules. For example, a carbon atom can be represented as “C”, an oxygen atom can be represented as “O”, double bond by “=”. The molecule Carbon dioxide is represented as “C(=O)=O”. Read more about SMILES here

The max length of the string is 25.

SAMPLE DATA FORMAT
SMILES sequence, Binding Affinity
O=Cc1ccc(O)c(OC)c1COCc, -17.41
CN=C=O, -21.3 . . .
