import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
import matplotlib.pyplot as plt


def get_data_loader(training=True):
    custom_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    if training:
        train_set = datasets.FashionMNIST('./data', train=True, download=True, transform=custom_transform)
        return torch.utils.data.DataLoader(train_set, batch_size=64)
    else:
        test_set = datasets.FashionMNIST('./data', train=False, transform=custom_transform)
        return torch.utils.data.DataLoader(test_set, shuffle=False, batch_size=64)


def build_model():
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(784, 300),
        nn.Sigmoid(),
        nn.Linear(300, 10)
    )
    return model


def evaluate_nn(model, test_loader, criterion):
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0

        for batch, (data, labels) in enumerate(test_loader):
            outputs = model(data)
            loss = criterion(outputs, labels)

            batch_size = labels.size(0)

            _, predicted = outputs.max(1)
            total += batch_size
            correct += predicted.eq(labels).sum().item()

    print(1 - (correct / total))
    return correct / total


def train_and_eval_nn(model, train_loader, test_loader, criterion, T):
    train_plot, test_plot = [], []
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    for epoch in range(0, T):
        model.train()
        correct = 0
        total = 0

        for batch, (data, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(data)

            loss = criterion(outputs, labels)
            loss.backward()

            optimizer.step()

            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

        train_plot.append(correct / total)
        test_plot.append(evaluate_nn(model, test_loader, criterion))

    return train_plot, test_plot


if __name__ == '__main__':
    epochs = 50
    criterion = nn.CrossEntropyLoss()
    train_loader = get_data_loader()
    test_loader = get_data_loader(False)
    model = build_model()

    train_plot, test_plot = train_and_eval_nn(model, train_loader, test_loader, criterion, epochs)
    epochs_list = []
    for i in range(epochs):
        epochs_list.append(i+1)

    plt.figure()
    plt.plot(epochs_list, train_plot, label="Training accuracy")
    plt.plot(epochs_list, test_plot, label="Test accuracy")
    plt.title("PyTorch Implementation")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.show()
