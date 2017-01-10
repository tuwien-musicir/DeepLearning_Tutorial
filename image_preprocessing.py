from PIL import Image
from sklearn import preprocessing

# adapted from https://github.com/fchollet/keras/blob/master/keras/applications/imagenet_utils.py
# (skipping 0 mean as we do this separately)

def reorder_RGB(data, dim_ordering='default'):
    if dim_ordering == 'default':
        dim_ordering = 'th' #K.image_dim_ordering()
    assert dim_ordering in {'tf', 'th'}

    # reorder 'RGB'->'BGR' according to Theano or Tensorflow order
    if dim_ordering == 'th':
        data = data[:, ::-1, :, :]
    else:
        data = data[:, :, :, ::-1]
    return data


def resize_and_crop(img,target_width=224,target_height=224):
    width, height = img.size

    img_ratio = width / float(height)
    target_ratio = target_width / float(target_height)

    # 1) compare ratios and resize the larger side proportional to the target of the smaller side
    new_width, new_height = (target_width, target_height)

    if target_ratio > img_ratio:
        new_height = int(round(height * (target_width / float(width))))
    else:
        new_width = int(round(width * (target_height / float(height))))

    img_new = img.resize((new_width, new_height), Image.ANTIALIAS)
    # The filter argument can be one of NEAREST (use nearest neighbour), BILINEAR (linear interpolation in a
    # 2x2 environment), BICUBIC (cubic spline interpolation in a 4x4 environment), or ANTIALIAS (a high-quality downsampling filter).
    # If omitted, or if the image has mode "1" or “P”, it is set to NEAREST.
    # Note that the bilinear and bicubic filters in the current version of PIL are not well-suited for large downsampling
    # ratios (e.g. when creating thumbnails). You should use ANTIALIAS unless speed is much more important than quality.

    # 2) crop to target size
    # offset to half of the remaining padding (one of them is 0)
    width_offset  = (new_width - target_width) / 2
    height_offset = (new_height - target_height) / 2

    # crop with offsets
    img_new = img_new.crop((width_offset, height_offset, width_offset+target_width, height_offset+target_height))
    #  The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate.
    return img_new



# STANDARDIZE DATA

def standardize(data, return_scaler = True, copy=True):
    '''standardize the data with zero mean unit variance (feature attribute-wise)

    data: numpy array to be transformed
    return_scaler: if True, a tuple of (data, scaler) will be returned with the scaler object containing all necessary parameters to scale other data again
    copy = False means try to avoid a copy and do inplace scaling instead.
    '''

    if return_scaler:
        # STANDARDIZATION (0 mean, unit var)
        scaler = preprocessing.StandardScaler(copy)
        # alternative: NORMALIZATION (min - max Normalization to (0,1))
        #scaler = preprocessing.MinMaxScaler()
        data = scaler.fit_transform(data)
        return (data, scaler)
    else:
        return preprocessing.scale(data,axis=0,copy=copy)
        # axis=0 means independently standardize each feature, otherwise (if 1) standardize each sample

    # how to get scaler parameters:
    #print scaler.mean_
    #print scaler.scale_


def standardize_flat(data):
    from scipy.stats.mstats import zscore
    return zscore(data,axis=None)
    # the manual version:
    #m = np.mean(a)
    #s = np.std(a)
    #(a - m) / s
