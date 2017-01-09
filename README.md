# Deep Learning Tutorial
# Coding Deep Learning Algorithms in Python with Keras

This is a set of tutorials with the purpose of getting into hands-on programming of Deep learning algorithms for
various tasks.

It uses Python 2.7 as the programming language with the popular Keras and Theano Deep Learning libraries underneath.

https://keras.io/


# Installation of Pre-requisites

Install Python 2.7: https://www.python.org/download/releases/2.7/
Note: On most Mac and Linux systems python is already pre-installed.
Check with `python --version` on the command line.

Install Python libraries:

## All OS:


## Mac 
(may be needed before):
xcode-select --install
easy_install pip 

sudo pip install pillow

## Linux

sudo pip install PIL

## Windows

As we use Theano as the Deep Learning computation backend, but Keras is configured to use TensorFlow as default on Windows, you have to change this in the keras.json configuration file which is in the .keras folder of the user's HOME directory:

Change these 2 lines to the following:
{
    "image_dim_ordering": "th",
    "backend": "theano"
}

See https://keras.io/backend/ for details or http://ankivil.com/installing-keras-theano-and-dependencies-on-windows-10/ for a step by step guide.



# Tutorials

To run the tutorials go into the `DL_Tutorial` folder and start from the command line:

`ipython notebook`

Your web browser will open and you can code and execute Python interactively in the browser.




# Sources

Car Data Set: http://cogcomp.cs.illinois.edu/Data/Car/
Fashion Data Set: 
Fashion 10000: An Enriched Social Image Dataset forFashion and Clothing
Loni et. al, Proceedings of the 5th ACM Multimedia Systems Conference, 2014
https://www.researchgate.net/publication/262254329_Fashion_10000_An_enriched_social_image_dataset_for_fashion_and_clothing