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
```
sudo pip install PIL
```

### All OS
In addition to the above, execute the following: (on Windows leave out `sudo`)
```
sudo pip install ipython
```

Try if you can open 
```
ipython notebook
```
on the command line. Otherwise try to install:
```
sudo pip install jupyter
```

Then download or clone the Tutorials from this GIT repository:

```
git clone https://github.com/tuwien-musicir/DL_Tutorial.git
```
or download https://github.com/tuwien-musicir/DL_Tutorial/archive/master.zip <br/>
unzip it and rename the folder to `DL_Tutorial`.

Install the remaining Python libraries needed:
```
cd DL_Tutorial
sudo pip install -r requirements.txt
```

### Windows

As we use Theano as the Deep Learning computation backend, but Keras is configured to use TensorFlow as the default on Windows, you have to change this in the `keras.json` configuration file which is in the `.keras` folder of the user's HOME directory:

Change these 2 lines to the following:
```
{
    "image_dim_ordering": "th",
    "backend": "theano"
}
```

See https://keras.io/backend/ for details or http://ankivil.com/installing-keras-theano-and-dependencies-on-windows-10/ for a step by step guide.

### Optional for GPU computation

If you want to train your neural networks on your GPU, also install the following (not needed for the tutorials):

* [NVidia drivers](http://www.nvidia.com/Download/index.aspx?lang=en-us)
* [CUDA](https://developer.nvidia.com/cuda-downloads)
* [cuDNN](https://developer.nvidia.com/cudnn) (optional, for further speedup)

To permanently configure Keras/Theano to use the GPU place a file `.theanorc` in your home directory with the following content:

```
[global]
device = gpu
floatX = float32
mode=FAST_RUN
```

### Check if installed correctly

To check whether Python, Keras and Theano were installed correctly, do:

`
python test_keras.py
`

If everything is installed correctly, it should print `Using Theano backend.`<br/>
If the GPU is configured correctly, it should also print `Using gpu device 0: GeForce GTX 980 Ti` or similar.


# Tutorials

For the tutorials, we use iPython / Jupyter notebook, which allows to program and execute Python code interactively in the browser.

To run the tutorials go into the `DL_Tutorial` folder and start from the command line:

`ipython notebook`

Your web browser will open showing a list of files. Start the tutorials one after another by clicking on the following:

1. <b>Car_recognition.ipynb</b><br/>
   This tutorial shows how images are loaded into Python and classified binary into "cars" and "not cars" using
   a) a Fully Connected neural network and b) a Convolutional Neural Network.

(more tutorials to follow)



# Source Credits

## Python libraries

The following helper Python libraries are used in these tutorials:

image_preprocessing.py: by Thomas Lidy and Alexander Schindler
audiofile_read.py and rp_extract.py: by Thomas Lidy and Alexander Schindler, taken from the [RP_extract](https://github.com/tuwien-musicir/rp_extract) git repository
wavio.py: by Warren Weckesser

## Data Sources

The data sets we use in the tutorials are from the following sources: (a copy is included in this repository, so no need to download them)

Car Data Set:
Images of side views of cars for use in evaluating object detection algorithms. The images were collected at UIUC. Contains 1050 training images (550 car and 500 non-car images) and 170 single-scale test images, containing 200 cars at roughly the same scale as in the training images.
http://cogcomp.cs.illinois.edu/Data/Car/

Music Speech Data Set:
by George Tzanetakis
Collected for the purposes of music/speech discrimination. Consists of 128 tracks, each 30 seconds long. Each class (music/speech) has 64 examples in 22050Hz Mono 16-bit WAV audio format.
http://marsyasweb.appspot.com/download/data_sets/

NOT USED YET:

Fashion Data Set:
Fashion 10000: An Enriched Social Image Dataset forFashion and Clothing
Loni et. al, Proceedings of the 5th ACM Multimedia Systems Conference, 2014
https://www.researchgate.net/publication/262254329_Fashion_10000_An_enriched_social_image_dataset_for_fashion_and_clothing