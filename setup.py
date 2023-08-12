from setuptools import setup

setup(
    name='taskHandler',
    version='0.1.0',    
    description='taskHandker pakage will distribute all file present in give directory',
    url='https://github.com/vardhannegi/taskHandler.git',
    author='vardhan negi',
    author_email='vardhan.negi@gmail.com',
    license='MIT ',
    packages=['taskHandler'],
    install_requires=['os','pwd'],

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux'
    ],
    python_requires='>=3.5'
)
