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

#### Download Colmap

Go to [Colmap's Github Release page](https://github.com/colmap/colmap/releases) Click on assets and then click on [COLMAP-dev-windows.zip](https://github.com/colmap/colmap/releases/download/3.6-dev.3/COLMAP-dev-windows.zip) then extract file.

#### Set colmap to environment path

Add Colmap to Environment Variable name PATH

[Youtube video](https://www.youtube.com/watch?v=Kj3FSWoKYfo)  show how to edit evironment variable in windows.

#### Enable WSL (Windows Linux subsystem)

[Microsoft docs](https://docs.microsoft.com/en-us/windows/wsl/install-win10) show how to enable WSL

#### Install our sfm to WSL

```shell
# download our sfm
wget https://github.com/pureexe/deeparc2undistort/releases/download/v0.0.1/sfm.deb
# install our sfm
sudo dpkg -i sfm.deb
# install share library 
sudo apt install libceres-dev libfmt-dev

```

### Install Python

[https://www.youtube.com/watch?v=dX2-V2BocqQ](Youtube Video) show how to install python on windows
 
#### Install Python Script to Windows Host (Not WSL)
```shell
# install colmap2deeparc 
pip install git+https://github.com/pureexe/colmap2deeparc
# install deeparc2undistort
pip install git+https://github.com/pureexe/deeparc2undistort
```

## Usage
```
deeparc2undistort -i <input images directory> -r <reference camera model> -o <output colmap undistorted directory>
```

If you have more than 1 object to image just put every object into sub directory of `<input directory>` and specify `-b`
