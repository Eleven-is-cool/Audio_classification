import shutil
import os


def clean():
    shutil.rmtree('highMass')
    os.mkdir('highMass')
    shutil.rmtree('temp')
    os.mkdir('temp')