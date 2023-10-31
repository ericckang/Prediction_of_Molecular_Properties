from rdkit.Chem import Descriptors
import numpy as np

def calculate_descriptors(mol):
    """
    Calculate descriptors for a single molecule.
    """
    return [Descriptors.MolWt(mol), Descriptors.MolLogP(mol)]

def prepare_features(data):
    """
    Calculate descriptors for a dataset.
    """
    data['Descriptors'] = data['Mol'].apply(calculate_descriptors)
    features = np.stack(data['Descriptors'].values)
    return features

# Add more feature engineering functions as needed
