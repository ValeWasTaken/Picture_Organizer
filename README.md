# Picture_Organizer
GUI picture viewer and organizer. One-click solution to separating images into different folders.

<h3>How to use:</h3>
The default setup looks like the following:
<img src="http://i.imgur.com/5GgmJZM.jpg"></img>
Here is how to use it:

1. Create a folder and place the images you want to sort and Python_Organizer.py inside of it.

2. Rename the path (line 12) to your folder. If you named the folder "Test" and placed it on your desktop it would be this on a Windows computer: 'C:\\Users\\YOUR_USERNAME_HERE\\Desktop\\Test\\'

3. Click run and maximize the screen.

4. Enjoy!

If you want to customize the program to filter to generate and sort to different folders, say for example you wanted to sort wallpapers into "Abstract", "Cities", "Nature", and "Other" then you would simply only have to replace all the current options "Yes/Maybe/Skipped/Delete" with your new words. To change the program to those examples we would change the following:

Line 17: **excludes = ['Yes', 'Maybe', 'Skipped', 'Delete']** -> **['Abstract', 'Cities', 'Nature', 'Other']**

Line 46-62: **move_file(path + 'Yes\\\')** -> **move_file(path + 'Abstract\\\')**

Line 78-81: **button_yes = Button(top_frame, text="Yes", command=yes)** -> **button_yes = Button(top_frame, text="Abstract", command=yes)**
