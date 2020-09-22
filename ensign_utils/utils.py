import fastai.vision.core


def parent_label_list(label):
    return [fastai.vision.core.parent_label(label)]
