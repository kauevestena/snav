import os
from processing_functions import misc as msc


OPJ = os.path.join
OE = os.environ


pathsWithCheckpoints = [
    msc.joinToHome("/data/checkpoints/deeplab_plus"),
]

gtImages = msc.joinToHome("/Dropbox/data/gt/originals")
gtMasksVersions = msc.joinToHome("/Dropbox/data/gt/versions")