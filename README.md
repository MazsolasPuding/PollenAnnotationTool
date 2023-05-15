# User interface for subjective quality assessment KEVA-7026

## Passwords:

1.  Gmail, Clever Cloud:

    pollen.proj@gmail.com
    Pollen5319ß

2.  Clever Cloud PostgreSQL:

    POSTGRESQL_ADDON_HOST=bql3duq2x8p5l7r5ahz0-postgresql.services.clever-cloud.com
    POSTGRESQL_ADDON_DB=bql3duq2x8p5l7r5ahz0
    POSTGRESQL_ADDON_USER=ucsuarf2fko8ds4k3443
    POSTGRESQL_ADDON_PORT=5432
    POSTGRESQL_ADDON_PASSWORD=W2JF95zE1czTx9ngxrZyX2nHxi3Drm
    POSTGRESQL_ADDON_URI=postgresql://ucsuarf2fko8ds4k3443:W2JF95zE1czTx9ngxrZyX2nHxi3Drm@bql3duq2x8p5l7r5ahz0-postgresql.services.clever-cloud.com:5432/bql3duq2x8p5l7r5ahz0

This is a general documentation and guide for setting up and using the user interface for subjective quality assessment of

## Python environment setup

**IMPORTANT NOTE:** these instructions have ony been tested on VZ-imaged Macbook Pros and Dell Linux laptops with python 3.8

1.  Install Anaconda

    https://docs.anaconda.com/anaconda/install/mac-os/

2.  create conda environment

    In a terminal navigate to the main directory of the program and run the following command:

    conda create --name sas python=3.8

3.  activate your environment

    conda activate sas

    **NOTE**: You can see if it is activated when the environment name shows up in parentheses in the terminal before your user name.

4.  install the following packages.

        pip install PyQt5
        pip install python-vlc
        pip install GitPython

5.  videos folder setup

    The final step is to place two folders to be compared. (Recommended path for the videos: VIDEOS folder in the program's directory.)

    **NOTE**: The two folders must contain an equal number of videos, with the same filenames!

## Usage and Instructions for the User Interface

1.  In order to run the program you need to navigate to the main directory of the program in a terminal and run the following command (after you have activated the conda environment):

        python3 src/main.py -fd "<first folder for comparison>" -sd "<second folder for comparison>"

        e.g.:   python3 src/main.py -fd "./videos/original_encoded" -sd "./videos/vi4bj_algo_72063a5fixlighting"

        More non mandatory parameters:
        --res sets the screen resolution to the given size
            values : 4K/FHD/MAC
        --video_count <int> sets the maximum playable videos. default 30

        --replay_count <int> sets the maximum replays for one video. default 1

        --language sets the language in which the GUI is displayed
            values : HUN/ENG

        --paramfile <paramfile.json>
            A json format paramfile can be specified where all of the command line prameters can be given.
            The usage of the paramfile can be combined with the command line arguments, in this case the command line
            parameters will be accepted.
            example :
            {
            "firstdir": "videos/original_ivf" ,
            "seconddir" : "videos/vi4bj_algo_2b680de6fixlighting_1",
            "resolution": "MAC",
            "replay_count" : 2 ,
            "video_count" : 20,
            "language" : "HUN"
            }

    **NOTE**: You will find folders to be compered in the 'videos' folder.

2.  Once the program has started, you have to type in your VZID in the top left corner and click on the SUBMIT button.
    Your VZID will then appear on top of the SUBMIT button with a green checkmark, and the first video will start playing.

    **NOTE**: If the video does not play automatically, click on the NEXT button in the lower right corner.

3.  Filling out the forms:

    Two videos will be played side by side, please keep close attention to the details and the differences between them.
    After the videos has stopped, complete the form below them:

    - You have to compare the video on the RIGHT to the video on the LEFT.
    - Grab all the sliders to the appropriate answers to the questions. e.g.: If the video on the left looks better grab the slider left.
    - If you'd like to watch the videos again before moving to the next one, you can click on the REPLAY button (below the videos) and watch them again one more time.
    - After you've answered all there questions, you can leave an additional comment below them.
    - Once you've completed the form, please click on the NEXT button and the assessment of a new video starts.
    - After completing all the forms in the assessment, a FINISH button will appear in the place of the NEXT button. After clicking it, you have completed the assessment, and a message box will appear with a SAVE button. Click Save and a new assessment will begin.

    ## Version generation

    Before using or releasing the Subjective Assessment Tool an Internal/version.json file must be generated. This can be done with src/version.py script.
    This will generate the version.json containing the git hash, the branch name, and dirty state of the source files. This last one indicates whether the current source files have uncommited changes or not.
