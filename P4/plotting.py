import matplotlib.pyplot as plt
import numpy as np

def plot_mean_metric(training_metrics, validation_metrics, model_label, metric_label): 
    epochs = range(0,len(training_metrics['mean']))

    training_mean = training_metrics['mean']
    training_std = training_metrics['std']
    validation_mean = validation_metrics['mean']
    validation_std = validation_metrics['std']

    plt.errorbar(epochs, training_mean, training_std, capsize=4)

    plt.errorbar(epochs, validation_mean, validation_std, capsize=4)

    # plt.plot(training_mean)
    
    # plt.plot(validation_mean)
    plt.title(f'{model_label} {metric_label}')
    plt.ylabel(metric_label)
    plt.xlabel('epoch')
    plt.xticks(epochs, labels=[f'{i + 1}' for i in epochs])
    plt.legend(['train', 'validation'], loc='upper left')
    plt.savefig(f"metrics/{model_label}_{metric_label}")
    plt.show()

