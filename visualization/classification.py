import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np


def plot_training(history,val = True,save_fig = False):


    # TODO : Obsłużyć fakt że nie zawsze muszę mieć określony klucz, najlepiej pętlą for po kluczach :)

    acc = history.history["acc"]
    loss = history.history["loss"]
    val_acc = history.history["val_acc"]
    val_loss = history.history["val_loss"]

    epochs = range(len(acc))

    plt.figure(figsize=(20,10))

    plt.subplot(2,1,1)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    plt.show()

    if save_fig == True:
        plt.savefig("learning")

def plot_confusion_matrix(model, X_test, y_test, class_names, save_fig=False):
    Y_pred = model.predict(X_test)
    y_pred = np.argmax(Y_pred, axis=1)
    y_pred = model.predict_classes(X_test)
    cnf_matrix = confusion_matrix(np.argmax(y_test, axis=1), y_pred)

    plt.figure(3, figsize=(14, 14))
    plt.title("Confusion Matrix")
    sns.heatmap(cnf_matrix, annot=True, xticklabels=class_names, yticklabels=class_names, fmt='.0f', square=True,
                robust=True,
                cmap="Blues", linewidths=4, linecolor='white')

    if save_fig == True:
        plt.savefig("CNF_Maxtrix.png")

    plt.figure(4, figsize=(14, 14))
    plt.title("Normalized Confusion Matrix")
    cnf_matrix_normalized = cnf_matrix / cnf_matrix.sum(axis=0)
    sns.heatmap(cnf_matrix_normalized, annot=True, xticklabels=class_names, yticklabels=class_names, fmt='.2f',
                square=True, robust=True,
                cmap="Blues", linewidth=4, linecolor='white')

    if save_fig == True:
        plt.savefig("CNF_Maxtrix_norm.png")


def plot_precision_recall():
    pass

def plot_AUC():
    pass

