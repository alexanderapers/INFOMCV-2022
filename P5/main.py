from load_data import load_stanford, load_tvhi
import os
import matplotlib.pyplot as plt
import tensorflow as tf
from models import stanford40_model, tv_hi_model
from keras.utils.np_utils import to_categorical
import plotting
from learning_rate_scheduler import halving_scheduler

# Suppress those pesky GPU logs.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main():
    # get the actual list of files for train, validation and test from stanford dataset from the file names
    # s40_train, s40_val, s40_test, s40_classes = load_stanford()

    # checkpoint_path = "training/stanford40-epoch{epoch:04d}"
    # save_callback = tf.keras.callbacks.ModelCheckpoint(
    #     checkpoint_path,
    #     monitor="val_loss",
    #     verbose=0,
    #     save_weights_only=True,
    #     save_freq="epoch",
    # )
    lr_callback = tf.keras.callbacks.LearningRateScheduler(halving_scheduler)

    # model = stanford40_model.get_model()
    # history = model.fit(s40_train,
    #     validation_data=s40_val, batch_size=8, epochs=15,
    #     callbacks=[lr_callback, save_callback])

    # plotting.plot_history_metric(history, "Stanford 40", "accuracy")
    # plotting.plot_history_metric(history, "Stanford 40", "loss")
    # load_data.load_tvhi()

    # load_data.load_tvhi(TVHI_train[0], TVHI_validation[0], TVHI_test[0])

    (tvhi_frames_train, tvhi_flows_train), (tvhi_frames_val, tvhi_flows_val), (tvhi_frames_test, tvhi_flows_test) = load_tvhi()
    model = tv_hi_model.get_model()
    history = model.fit(tvhi_frames_train,
        validation_data=tvhi_frames_val, batch_size=8, epochs=15,
        callbacks=[lr_callback])


if __name__ == "__main__":
    main()
