# indoor_position
PROBLEM STATEMENT :

Building an Indoor positioning systems (IPS) which  enable locating the position of  objects or people within buildings(malls, hospitals etc.) by using Human Activity (walking, upstairing etc.)

Instruction to run and Packages details:
•	Name: tensorflow
              Version: 1.12.0
              Summary: TensorFlow is an open source machine learning framework for everyone.
               Home-page: https://www.tensorflow.org/
               Author: Google Inc.
               Author-email: opensource@google.com
               License: Apache 2.0
               Requires: keras-preprocessing, six, wheel, absl-py, gast, grpcio, astor, protobuf, numpy,
               termcolor, keras-applications, tensorboard.






•	Name: numpy
              Version: 1.15.4
              Summary: NumPy: array processing for numbers, strings, records, and objects.
              Home-page: http://www.numpy.org
              Author: Travis E. Oliphant et al.
              Author-email: None
              License: BSD
              Requires:
Required-by: Theano, tensorflow, tensorboard, tables, seaborn, scikit-learn, PyWavelets, pytest-doctestplus, pytest-arraydiff, patsy, pandas, opencv-python, opencv-contrib-python, odo, numexpr, numba, mkl-random, mkl-fft, matplotlib, Keras, Keras-Preprocessing, Keras-Applications, h5py, datashape, Bottleneck, bokeh, bkcharts, astropy.








•	Name: pandas
Version: 0.24.0
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Requires: numpy, pytz, python-dateutil
Required-by: seaborn, odo



Python Libraries:
1.	Numpy.
2.	Pandas.
3.	Glob.
4.	Sklearn.
5.	Tensorflow.


To run the following set of codes you have to make some changes which as follows:
•	In har.py file , in line 19 you have to give the location of the dataset which is used to train the model.
•	In har.py file you have to count the string of the location in which you have stored the training data as in my case it starts from 50 to 53 and same goes with the line 64 in har.py file.
•	And in har.py line 122 you to give the location where your pretrained model is stored 




link to data set for training: https://www.kaggle.com/malekzadeh/motionsense-dataset?select=A_DeviceMotion_data


link for the pre-trained model : https://icedrive.net/0/b6fwinf2Ls

video of working model link: https://icedrive.net/0/1bv2jsFdiS
