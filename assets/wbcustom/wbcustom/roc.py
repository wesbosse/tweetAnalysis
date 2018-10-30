import matplotlib.pyplot as plt
import numpy as np

def plot(probas, true, step=0.01):
    """
    probas should be a numpy array of predict_probas
    true is a pandas series of true labels
    step is the step size for checking thresholds
    """

    probas = probas[:,
             1]  # The output of predict_proba() is an array of the probabilities for every class, but we only want the probabilities for class 1
    true = true.values  # We need to convert the class labels from a Pandas Series to a numpy array. We do this using the .values attribute
    assert (len(probas) == len(
        true))  # We're making sure that our probabilities vector is the same length as our true class labesl vector

    TPRs = []  # Setting up empty list of True Positive Rate
    FPRs = []  # Setting up empty list of False Positive Rate

    for i in np.arange(0.0, 1.0, step):  # np.arange allows us to use step sizes that are decimals
        preds_class = probas > i  # Numpy arrays have a feature called 'broadcasting.' Check the documentation: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html to see what this does.
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for index in range(len(preds_class)):  # We're comparing each prediction with each true value here

            if preds_class[index] == 1 and true[index] == 1:
                TP += 1
            elif preds_class[index] == 1 and true[index] == 0:
                FP += 1
            elif preds_class[index] == 0 and true[index] == 0:
                TN += 1
            elif preds_class[index] == 0 and true[index] == 1:
                FN += 1

        TPR = TP / (TP + FN)  # Calculating TPR and FPR and appending to our lists
        FPR = FP / (FP + TN)

        TPRs.append(TPR)
        FPRs.append(FPR)

    plt.rcParams['font.size'] = 14
    plt.plot(FPRs, TPRs, color="orange")
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.title('Receiver Operating Characteristic')
    plt.xlabel("False Positive Rate (1 - Specificity)")
    plt.ylabel("True Positive Rate (Sensitivity)")
    plt.show();
