#BioEECoins

This is a PyQt program used in BioEE lab, Columbia University, for colony inspection.

## Installation Guide for Ubuntu 14.04.3 LTS

Before installing and executing this code, you will first need several program installed in you computer. This guide is tested under Ubuntu 14.04.3 environment only. But it should work for other Linux distributions in a similar way.

* Qt installation
Go to the official website of QT and have QT5 downloaded (under LGPL licence)

* PyQt installation
After installing Qt, you will need SIP and PyQt.
	* The version of SIP provided by the Ubuntu community official repository is a little bit out dated. So you will probably need to download it and compile from source. The source code can be found at: [SIP 4.17] (http://www.riverbankcomputing.com/software/sip/download). Download the code, then run:
				```bash
				python configure.py ;
				make ;
				make install
				```
				That should provide a successful installation of SIP

	* If you are running python3, then it is probably good to just get PyQt5 from the official repository. This can be done by running `sudo apt-get install python3-pyqt5`
				However, I never get python3 running with Opal Kelly's official library.
				So I stick to python 2.7.4
				In this case, you will need, as well, compile the code from the source.
				The code for PyQt5 can be downloaded from [PyQt5] (http://www.riverbankcomputing.com/software/pyqt/download5).
				After this, all you need to do is again:
				```
				python configure.py -qmake=ABSOLUTE_PATH_TO_THE_BINARY ;
				make ;
				make install ;
				```
				And this should fix the thing.

	* The ploting functionality is implemented using pyqtgraph integration, this can be installed by using: `sudo apt-get install python[3]-pyqtgraph`

	However the above 
