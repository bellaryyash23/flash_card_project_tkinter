# 📸Flash Card App using Tkinter of Python

🌟A GUI based app which helps you learn new things like learning a new language, new vocabulary, etc.

🌟Here, we have built an app which helps you learn new French words. The app first displays a French Word and within 3 seconds it flashes
the English translation of the word. The user can then tick right if they got the correct answer and press wrong if they want to attempt the word again.

🌟Thus, by flashing the question and answer, the user can verify wheather if they have learnt the word and if not then they can always retry.
This proves to be a very effective way to self-learn new topics.

👉The UI setup of the app is done using the tkinter classes like Label, Button, Tk, Entry, PhotoImage and Canvas.

👉The Canvas class is used to design the background image of the app.

👉The objects are placed and packed on the window using the .grid(..) method of the tkinter class which divides the whole window into rows and columns. 
The attribute columnspan is used for effective design and placement of labels and buttons.

![UI of the App](https://github.com/bellaryyash23/flash_card_project_tkinter/blob/master/samples/ui.JPG?raw=true)

👆UI Design of App👆

📸Random word Generation

👉In the 'main.py' file, first the data containing the French words and its English translation is imported from the 'french_words.csv' file using pandas.
The data is properly formated and converted into a dictionary using the 'orient' attribute set to 'records'.

👉Now, from this dictionary a random choice is made and it is confgured to replace the 'Language' and 'Word' objects respectively of the app.

👉The method of tkinter class called .after(...) is used to program a timer for the random cards English counterpart to be displayed after 3 seconds.
This is done in the 'random_word' function which is tied to the 'right-btn' object and called on each press.

👉During the first run function call and timer method is setup explicitly. After that during each button press the method is updated.

![Front French of the App](https://github.com/bellaryyash23/flash_card_project_tkinter/blob/master/samples/front.JPG?raw=true)

👆French Word👆

📸English Translated Word to display

👉The current selected record is stored and updated as global variable. This recored is used to display the English translation. Once the timer completes 3 seconds
the function 'show_english_translation' is triggered and it will configure and update the app with English translated counterpart of the French Word.

![Back English Word](https://github.com/bellaryyash23/flash_card_project_tkinter/blob/master/samples/back.JPG?raw=true)

👆English Word👆

📸Evaluation Mechanism:

👉Once the English word is displayed, the user can check if he knew the answer and press the respective buttons. If the user pressed the 'wrong-btn' then, the record
is pushed back into the file for user to reattempt it. The initial data is as follows:

![Initial Data file](https://github.com/bellaryyash23/flash_card_project_tkinter/blob/master/samples/initial_data.JPG?raw=true)

👆Initial Loaded data file👆

👉If the user pressed the right button it means the user knew the answer and hence, the record of that word is removed from the dictionary of words. After that a new 
'words_to_learn.csv' file is generated which contains the words which the did not get right and excludes the correct ticked data.

![Words to learn](https://github.com/bellaryyash23/flash_card_project_tkinter/blob/master/samples/learn_data.JPG?raw=true)

👆Words to Learn data file👆

👉In this way, using the user feedback the Flash cards data is updated and kept relevant to users needs. Thus, all these components combined create the smooth working
of the app.
