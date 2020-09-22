from flask import Flask
from flask import request, redirect, render_template
from fastai.learner import load_learner
from fastai.vision.core import parent_label


def parent_label_list(label):
    return [parent_label(label)]
