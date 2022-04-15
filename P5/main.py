import load_data
import os
import matplotlib.pyplot as plt
import tensorflow as tf
from models import stanford40_model
from keras.utils.np_utils import to_categorical

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main():
    # gathers the two datasets file names and class labels
    # they are already split into train, validation and test using stratification
    # train, validation and test variables are tuples of lists (file_names, label_names)
    # classes are the unique names of the classes that are used
    # TVHI_train, TVHI_validation, TVHI_test, TVHI_classes = files.__process_TVHI()

    # get the actual list of files for train, validation and test from stanford dataset from the file names
    s40_train_files, s40_val_files, s40_test_files = load_data.load_stanford()

    for batch in s40_train_files:
        # X shape is (batch_size, img_height, img_width, channels)
        # y is a list of labels (integers) shape (batch_size)
        X, y = batch
        plt.imshow(tf.cast(X[1,:,:,:], dtype=tf.int32))
        plt.show()
        print(y[1])
        break
    #    print(x, y)
    # s40_num_classes = len(s40_classes)
    # s40_train_y = to_categorical(s40_train_y, num_classes=s40_num_classes)
    # s40_val_y = to_categorical(s40_val_y, num_classes=s40_num_classes)
    # s40_test_y = to_categorical(s40_test_y, num_classes=s40_num_classes)

    # model = stanford40_model.get_model()
    # model.fit(s40_train_files, s40_train_y,
    #     validation_data=(s40_val_files, s40_val_y))

    # load_data.load_tvhi(TVHI_train[0], TVHI_validation[0], TVHI_test[0])

    

if __name__ == "__main__":
    main()
