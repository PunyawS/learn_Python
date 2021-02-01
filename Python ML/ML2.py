from sklearn import datasets
digits_dataset=datasets.load_digits()

print(digits_dataset.images[0:10])
print(digits_dataset.images[0].shape)