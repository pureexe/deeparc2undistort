# deeparc2undistort
convert image that capture from deeparc into colmap undistrot model

## Installation guide

### Linux (compatible with Windows Linux Subsystem )

```shell
# install colmap
sudo apt install colmap
# install colmap2deeparc 
pip install git+https://github.com/pureexe/colmap2deeparc
# download our sfm
wget https://github.com/pureexe/deeparc2undistort/releases/download/v0.0.1/sfm.deb
# install our sfm
sudo dpkg -i sfm.deb
# install share library 
sudo apt install libceres-dev libfmt-dev
# install deeparc2undistort
pip install git+https://github.com/pureexe/deeparc2undistort
```

### Windows 

#### Download Colamp

#### Set colmap to environment path

#### Enable WSL (Windows Linux subsystem)

#### Install our sfm to WSL

```shell
# download our sfm
wget https://github.com/pureexe/deeparc2undistort/releases/download/v0.0.1/sfm.deb
# install our sfm
sudo dpkg -i sfm.deb
# install share library 
sudo apt install libceres-dev libfmt-dev

```

#### Install Python Script
```shell
# install colmap2deeparc 
pip install git+https://github.com/pureexe/colmap2deeparc
# install deeparc2undistort
pip install git+https://github.com/pureexe/deeparc2undistort
```

## usage
```
deeparc2undistort -i <input images directory> -r <reference camera model> -o <output colmap undistorted directory>
```

If you have more than 1 object to image just put every object into sub directory of `<input directory>` and specify `-b`
