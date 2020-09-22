from fastai.vision.core import parent_label


def parent_label_list(label):
    return [parent_label(label)]
