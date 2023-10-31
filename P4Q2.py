import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


def get_data_loader(training=True):
    custom_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    if training:
        train_set = datasets.FashionMNIST('./data', train=True, download=True, transform=custom_transform)
        return DataLoader(train_set, batch_size=64)
    else:
        test_set = datasets.FashionMNIST('./data', train=False, transform=custom_transform)
        return DataLoader(test_set, shuffle=False, batch_size=64)


def softmax(z):
    e_z = np.exp(z - np.max(z, axis=0, keepdims=True))
    return e_z / np.sum(e_z, axis=0, keepdims=True)


def cross_entropy_loss(label, pred):
    return -np.sum(label * np.log(pred))


def forward_pass(x, W1, W2):
    z1 = np.dot(W1, x.T)
    a1 = 1 / (1 + np.exp(-z1))

    z2 = np.dot(W2, a1)
    pred = softmax(z2)

    return a1, pred


def backward_pass(x, y, a1, pred, W1, W2, learning_rate):
    dL_dz2 = pred - y
    grad_W2 = np.dot(dL_dz2, a1.T)

    W2 -= learning_rate * grad_W2

    dL_dz1 = np.dot(W2.T, dL_dz2) * a1 * (1 - a1)
    grad_W1 = np.dot(dL_dz1, x)

    W1 -= learning_rate * grad_W1

    return W1, W2


def compute_accuracy(predictions, labels):
    return np.mean(np.argmax(predictions, axis=0) == labels)


def train_nn(train_loader, test_loader, W1, W2, learning_rate, epochs):
    train_plot = []
    test_plot = []
    for epoch in range(epochs):
        total_correct = 0
        total_samples = 0

        for inputs, labels in train_loader:
            inputs = inputs.view(inputs.size(0), -1).numpy()  # Convert input to a NumPy array
            one_hot_labels = np.zeros((10, len(labels)))
            one_hot_labels[labels, np.arange(len(labels))] = 1

            a1, pred = forward_pass(inputs, W1, W2)

            W1, W2 = backward_pass(inputs, one_hot_labels, a1, pred, W1, W2, learning_rate)

            total_correct += np.sum(np.argmax(pred, axis=0) == labels.numpy())
            total_samples += len(labels)

        train_plot.append(total_correct / total_samples)

        test_total_correct = 0
        test_total_samples = 0

        for test_inputs, test_labels in test_loader:
            test_inputs = test_inputs.view(test_inputs.size(0), -1).numpy()
            test_a1, test_pred = forward_pass(test_inputs, W1, W2)
            test_total_correct += np.sum(np.argmax(test_pred, axis=0) == test_labels.numpy())
            test_total_samples += len(test_labels)

        test_plot.append(test_total_correct / test_total_samples)
        print(1 - test_total_correct / test_total_samples)
    return train_plot, test_plot


if __name__ == '__main__':
    W1 = np.random.randn(300, 784)
    W2 = np.random.randn(10, 300)
    learning_rate = 0.001
    epochs = 50

    train_loader = get_data_loader()
    test_loader = get_data_loader(False)
    train_plot, test_plot = train_nn(train_loader, test_loader, W1, W2, learning_rate, epochs)

    epochs_list = []
    for i in range(epochs):
        epochs_list.append(i + 1)

    plt.figure()
    plt.plot(epochs_list, train_plot, label="Training accuracy")
    plt.plot(epochs_list, test_plot, label="Test accuracy")
    plt.title("PyTorch Implementation")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.show()
