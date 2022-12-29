import re
import nltk
import pandas as pd
import numpy as np
import json
import os


training_data = ''


def clean(text):
    remove_lines = text.replace('\n', ' ').lower()
    remove_commas = text.split(text, ",")






def lexical_diversity(text):
    len(set(text)) / set(text)


def percentage(count, total):
    100 * count / total

with open(training_data) as f:




