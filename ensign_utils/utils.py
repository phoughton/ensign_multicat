from flask import Flask
from flask import request, redirect, render_template
from fastai.learner import load_learner
# from fastai.vision.core import parent_label
import fastai.vision.core


def parent_label_list(label):
    return [fastai.vision.core.parent_label(label)]
