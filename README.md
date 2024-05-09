# Pollen Annotation Tool

## Version: 1.0.0

## About the App:

    This app was designed for annotating Pollens.
    The project has a Gmail account 'pollen.proj@gmail.com', and in it's Google Drive is the latest version of the application,
    and the app's database is hosted on 'clever cloud'. Access to all of these are listed under the 'Accounts and Passwords' section.
    **NOTE**: For the review function to be working properly, the pictures MUST stay in the same location as they were during annotation.

## Usage:

    ### Creating an account and Logging in:

        In the folder of the project you will find a `Pollen.exe` file. Run this executable and the program will start and a Welcome screen will open.

        In the welcome screen you will have the option for'Logging in' or 'creating an account'.
        To create an account click on the appropriate button and fill out the form.
        The 'experience level' drop down list is for specifying that you are senior or more of a beginner annotator.

        **IMPORTANT NOTE**: The password you provide should be unique and not used elsewhere.
                    While it is stored encrypted, it should NOT be a key to any of your other accounts for safety reasons.
                    Retrieving a forgotten password can be achieved through directly accessing the database and decrypting the password,
                    so while it is possible, you should keep a copy of it somewhere, in case you forget it.
                    If you do forget it, you can contact me, my contact is down below.

        After creating an account you can log in, and the main window of the app will show up.

    ### Basic Annotation:

        For using the tool, you first need to load a directory using the 'Open Dir' button in the toolbar.
        If the folder contains pictures, they will show up in the thumbnails view dock, and first image appears in the middle of the screen.
        If you decided which type of Pollen is on the picture:
            - Select a Pollen Type from the list
            - Input your confidence in your choice using the slider
            - Add a comment if needed
            - And click on the Save button (The save Button will only be enabled if you choose a pollen type.)
            - Click on next and repeat the process for the remaining pictures in the folder

        After labelling all the pictures in a folder a pop up message will appear.

    ### Annotation Review:

        For Senior Accounts the 'Review Tab' is enabled (above the top left corner of the picture), click on it and the review page will open.
        First you will need to load previous annotations from the database, using the filters on the right. In the filter you can set the date
        range and select users. (The 'include Senior annotations' checkbox is only for selecting 'All users' from the dropdown list, and for
        further specifying the selection).
        After setting the filter, click on the load button.

        If your filter contains annotations the first picture will be loaded, and the counter will show how many annotations are loaded.
        The Data panel shows the previous annotations details. After evaluating it do the following:
            - Give the annotation a Score (0-100)
            - Give it a Review comment if needed
            ---* After this, do the Basic Annotations workflow ---
            - Select a Pollen Type from the list
            - Input your confidence in your choice using the slider
            - Add a comment if needed
            - And click on the Save button (The save Button will only be enabled if you choose a pollen type.)
            - Click on next and repeat the process for the remaining pictures in the folder

        *: While Reviewing and, providing feedback, your annotation will be saved as a separate record as-well.

        **IMPORTANT NOTE**: For the review function to be working, the location of the pictures MUST be the same as it was
                    during the annotation, otherwise the pictures will not load.

    ### Singing out:

        If you've want to switch accounts you can use the 'Sign Out' button or just by closing the window.
        Closing the app is by closing the main window and the the welcome screen.

## Accounts and Passwords:

...


## License

    Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

    If you have any further questions or issues feel free to contact me:

    Horváth Dávid - horvath.david35@gmail.com
