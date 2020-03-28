# deeparc2undistort
convert image that capture from deeparc into colmap undistrot model

## installation guide
```shell
# install colmap
sudo apt install colmap
# install colmap2deeparc 
pip install git+https://github.com/pureexe/colmap2deeparc
# download our sfm
wget https://github.com/pureexe/deeparc2undistort/releases/download/v0.0.1/sfm.deb
# install our sfm
sudo dpkg -i sfm.deb
# install deeparc2undistort
pip install git+https://github.com/pureexe/deeparc2undistort
```

## usage
```
deeparc2undistort -i <input images directory> -r <reference camera model> -o <output colmap undistorted directory>
```

If you have more than 1 object to image just put every object into sub directory of `<input directory>` and specify `-b`
