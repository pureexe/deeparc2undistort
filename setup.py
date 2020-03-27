import setuptools

setuptools.setup(
    name="deeparc2undistort",
    version="0.0.1",
    author="Pakkapon Phongthawee",
    author_email="pakkapon.p_s19@vistec.ac.th",
    description="convert images from deeparc into colmap undistorted",
    url="https://github.com/pureexe/colmap2deeparc",
    packages=setuptools.find_packages(),
    py_modules=['deeparc2undistort'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux 64 Bit",
    ],
    entry_points={
     'console_scripts': ['deeparc2undistort=deeparc2undistort:entry_point'],
    },
    package_data={'deeparc2undistort': ['window5x5_matching_no_duplicate.txt']},
    python_requires='>=3.6'
)