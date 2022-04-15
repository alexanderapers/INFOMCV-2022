import load_data
import os
import matplotlib.pyplot as plt
import tensorflow as tf
from models import stanford40_model
from keras.utils.np_utils import to_categorical
import plotting

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main():
    # get the actual list of files for train, validation and test from stanford dataset from the file names
    s40_train, s40_val, s40_test, s40_classes = load_data.load_stanford()
    #
    # model = stanford40_model.get_model()
    # history = model.fit(s40_train,
    #     validation_data=s40_val, batch_size=32, epochs=10)
    #
    # plotting.plot_history_metric(history, "Stanford 40", "accuracy")
    # plotting.plot_history_metric(history, "Stanford 40", "loss")

    load_data.load_tvhi()

    # load_data.load_tvhi(TVHI_train[0], TVHI_validation[0], TVHI_test[0])

    

if __name__ == "__main__":
    main()
