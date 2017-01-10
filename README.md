# Deep Learning Tutorial
## Coding Deep Learning Algorithms in Python with Keras

(c) 2017 by Thomas Lidy, TU Wien - http://ifs.tuwien.ac.at/~lidy

This is a set of tutorials with the purpose of getting into hands-on programming of Deep learning algorithms for
various tasks.

It uses Python 2.7 as the programming language with the popular [Keras] (https://keras.io/) and [Theano](http://deeplearning.net/software/theano/) Deep Learning libraries underneath.

# Installation of Pre-requisites

## Install Python 2.7

Note: On most Mac and Linux systems Python is already pre-installed. Check with `python --version` on the command line whether you have Python 2.7.x installed.

Otherwise install Python 2.7 from https://www.python.org/download/releases/2.7/

## Install Python libraries:

### Mac 

On the terminal:

```
# Note: the first two are not needed if you have done this previously:
xcode-select --install
easy_install pip 

sudo pip install pillow
```

### Linux + Windows
`
sudo pip install PIL
`

### All OS
In addition to the above, execute the following: (on Windows leave out `sudo`)
`
sudo pip install ipython
`

Try if you can open 
`
ipython notebook
`
on the command line. Otherwise try to install:
`
sudo pip install jupyter
`

Then install the remaining Python libraries neede:
```
cd DL_Tutorial
sudo pip install -r requirements.txt
```

### Windows

As we use Theano as the Deep Learning computation backend, but Keras is configured to use TensorFlow as default on Windows, you have to change this in the keras.json configuration file which is in the .keras folder of the user's HOME directory:

Change these 2 lines to the following:
`{
    "image_dim_ordering": "th",
    "backend": "theano"
}`

See https://keras.io/backend/ for details or http://ankivil.com/installing-keras-theano-and-dependencies-on-windows-10/ for a step by step guide.

### Optional for GPU computation

If you want to train your neural networks on GPU, also install the following:

* [NVidia drivers](http://www.nvidia.com/Download/index.aspx?lang=en-us)
* [CUDA](https://developer.nvidia.com/cuda-downloads)
* [cuDNN](https://developer.nvidia.com/cudnn) (optional, for further speedup)

To permanently configure Keras/Theano to use the GPU place a file `.theanorc` in your home directory with the following content:

`
[global]
device = gpu
floatX = float32
mode=FAST_RUN
`

### Check if installed correctly

To check if Python, Keras and Theano were installed correctly, do:

`
python test_keras.py
`

If everything is installed correctly, it should print `Using Theano backend.`.<br/>
If the GPU is configured correctly, it should also print `Using gpu device 0: GeForce GTX 980 Ti`.


# Tutorials

For the tutorials, we use iPython / Jupyter notebook, which allows to program and execute Python code interactively in the browser.

To run the tutorials go into the `DL_Tutorial` folder and start from the command line:

`ipython notebook`

Your web browser will open showing a list of files. Start the tutorials one after another by clicking on the following:

1. <Car_recognition.ipynb>Car_recognition.ipynb
   This tutorial shows how images are loaded into Python and classified binary into "cars" and "not cars" using
   a) a Fully Connected neural network and b) a Convolutional Neural Network.

(more tutorials to follow)


# Data Sources

The data sets we use in the tutorials are from the following sources:

Car Data Set:
http://cogcomp.cs.illinois.edu/Data/Car/

Fashion Data Set:
Fashion 10000: An Enriched Social Image Dataset forFashion and Clothing
Loni et. al, Proceedings of the 5th ACM Multimedia Systems Conference, 2014
https://www.researchgate.net/publication/262254329_Fashion_10000_An_enriched_social_image_dataset_for_fashion_and_clothing