#!/usr/bin/env python
# coding: utf-8

# ## Dog Breeds Classifier

# -----------------------------
# Make everything deterministic
import numpy as np
np.random.seed(2)

import torch
torch.manual_seed(2)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
# -----------------------------
#get_ipython().run_line_magic('matplotlib', 'notebook')

import fastai

from fastai.vision import *
from fastai.metrics import error_rate
from fastai import __version__

import torchvision
from torchvision import models

from fastai.callbacks import *
from fastai.utils.mem import *

torch.cuda.ipc_collect()
torch.cuda.empty_cache()
gc.collect()


debug = False

get_ipython().system('nvidia-smi')


from subprocess import check_output
nvidia_smi_ = [0, 0]

def nvidia_smi(nvidia_smi_):
    old_nvidia_smi_ = nvidia_smi_[1]
    nvidia_smi_now  = int(check_output(['nvidia-smi', '--query-gpu=memory.used', '--format=csv,nounits,noheader']))
    nvidia_smi_[0]  = nvidia_smi_now
    nvidia_smi_[1]  = nvidia_smi_now - old_nvidia_smi_
    return nvidia_smi_ 

print('nvidia-smi memory usage/increment:', nvidia_smi(nvidia_smi_))

torch.cuda.empty_cache()


import pathlib
import hashlib

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()


print(f'Dog breed classifier v4.0')
print(f'Fast.ai version: {fastai.__version__}')

if len(sys.argv) > 1:
	target_dir = sys.argv[1]
	target_dir = Path(target_dir)
	if target_dir.is_dir():
		print(f'Running on target directory: {target_dir}')
		file_list = list(target_dir.glob('**/*.jpg'))
		#print(file_list)

		download_url = 'https://imaticloud.ge.imati.cnr.it/index.php/s/2IBskdQofQoawxF/download'
		model_fname  = 'resnet50-epoch1-unfreeze-299-2019-10-17_13.04.08_1-90perc-acc.pkl'
		model_dir    = '/tmp'
		model_md5sum = '0ba2b01b2e63a337f09f85186e750205'

		model_file   = Path(model_dir) / model_fname


		if not model_file.exists():
			print(f'Model file doesn\'t exist. Downloading...')
			get_ipython().system('wget --no-check-certificate {download_url} --output-document={model_dir}/{model_fname}')
		elif md5(model_file) != model_md5sum:
			print(f'Model MD5 digest doesn\'t match: {md5(model_file)} != {model_md5sum}. Re-downloading...')
			get_ipython().system('wget --no-check-certificate {download_url} --output-document={model_dir}/{model_fname}')
		else:
			print(f'Model MD5 digest matches: {md5(model_file)}')

		print(f'Loading model: {model_dir}/{model_fname}')
		learn = load_learner(model_dir, model_fname)

		classes = learn.data.classes

		classes_dict = {}

		file_counter = 0
		for fname in file_list:
			img = open_image(fname)
			prediction, classid, raw_pred = learn.predict(img)
			sorted_raw_pred = raw_pred.sort()

			pred_str = ''
			for i in range(-1, -5, -1):
				this_class = str(classes[sorted_raw_pred[1][i]])
				this_prob  = float(sorted_raw_pred[0][i])
				#print(classes_dict[this_class])

				class_acc = classes_dict.get(this_class)
				if class_acc:
					if debug:
						print(f'cumulative class probability for {this_class}: {class_acc}')
					class_acc += this_prob
				else:
					if debug:
						print(f'cumulative class probability for {this_class}: 0.0')
					class_acc = this_prob
				classes_dict[this_class] = class_acc

				if this_prob > 0.49 or i == -1:
					pred_str += this_class + ' -> ' + str(round(this_prob, 2)) + '\t'

			print(f'{fname.name} -> {prediction} - {pred_str}')
			file_counter += 1
		print(f'This image directory has the following class probabilities.')
		print(sorted(classes_dict.items(), key=lambda x: x[1], reverse=True))
	else:
		print(f'Supplied parameter {target_dir} is not a directory. Exiting...')
		sys.exit(0)
else:
	print('Please provide target directory with images to classifiy. Exiting...')
	sys.exit(0)

