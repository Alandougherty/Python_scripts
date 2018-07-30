import numpy as np

def degreetorad(degree):
    return (degree * (np.pi / 180))


def params(angles):
    theta_degree = np.min(angles) - np.max(angles)
    theta = np.array([degreetorad(theta_degree), 0, 0])
    return theta


def affineTranslate(input):
    translationMatrix = np.array([[1, 0, 0, input[0]], [0, 1, 0, input[1]], [0, 0, 1, input[2]], [0, 0, 0, 1]])
    return translationMatrix


def affineSheer(input):
    input = np.array(input)
    sheerMatrix = np.array(
        [[np.cos(input[1]), np.sin(input[0]), 0, 0], [np.sin(input[1]), np.cos(input[0]), 0, 0], [0, 0, 1, 0],
         [0, 0, 0, 1]])
    return sheerMatrix


def affineScale(input):
    # input = input / np.max(input)
    scaleMatrix = np.array([[input[0], 0, 0, 0], [0, input[1], 0, 0], [0, 0, input[2], 0], [0, 0, 0, 1]])
    return scaleMatrix


def affinerotatex(input):
    input = input / np.max(input)
    rotateMatrix = np.array(
        [[1, 0, 0, 0], [0, np.cos(input[0]), -np.sin(input[0]), 0], [0, np.sin(input[0]), np.cos(input[0]), 0],
         [0, 0, 0, 1]])
    return rotateMatrix


def affinerotatez(input):
    rotateMatrix = np.array(
        [[np.cos(input[2]), -np.sin(input[2]), 0, 0], [np.sin(input[2]), np.cos(input[2]), 0, 0], [0, 0, 1, 0],
         [0, 0, 0, 1]])
    return rotateMatrix



def affineTransform(input, theta, size):
    augmenter = np.ones((input.shape[0], 1))

    # Adust the translate to recenter after the shear
    newOrigin = np.array([0, 0, 0])
    # transform as usual
    # input = np.concatenate((input, augmenter), axis=1)
    transformMat = np.matmul(affineScale(size), affineTranslate(newOrigin))
    transformMat = np.matmul(transformMat, affineSheer(theta))
    transformed = np.matmul(transformMat, input.transpose())


    return transformed[0:-1].transpose()

