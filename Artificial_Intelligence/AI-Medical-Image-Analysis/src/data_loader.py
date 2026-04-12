import tensorflow as tf

def load_data(path):
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        rotation_range=15,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )

    train = datagen.flow_from_directory(
        path,
        target_size=(160,160),
        batch_size=16,
        class_mode='binary',
        subset='training'
    )

    val = datagen.flow_from_directory(
        path,
        target_size=(160,160),
        batch_size=16,
        class_mode='binary',
        subset='validation'
    )

    return train, val