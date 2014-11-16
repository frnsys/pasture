## Visualization setup
To get the visualization output from `process_tweets.py` working, you have to do a lot
of work (these instructions are for OSX 10.9):

    brew install qt
    brew install graphviz
    pip install -U pyside
    pip install pygraphviz
    git clone https://github.com/PySide/pyside-setup.git
    cd pyside-setup
    pyside_postinstall.py -install

For Ubuntu:

    sudo apt-get install graphviz libgraphviz-dev
    sudo apt-get build-dep python-matplotlib
    pip install matplotlib
    sudo apt-get install cmake qt-sdk
    pip install -U pyside
    pip install pygraphviz