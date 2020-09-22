import fastai.vision.core as fvc


def parent_label_list(label):
    return [fvc.parent_label(label)]
