# Code Jam 4 Qualifier - The Rocketship Control Panel!
In order to qualify for this code jam, you'll be building a rocketship control panel
based on the code in the file `qualifier.py`.

First, you need to do some prep:
- `git clone` this repository into a directory on your computer.
- Run the module. The code will crash. Looks like there are bugs in our qualifier code!
- Fix the bugs.
- Run the module after fixing the bugs. Nothing will show up.
- Figure out why nothing shows up, and fix that too. This may involve adding a new line of code, or modifying an existing one.


Next, let's add the missing contents and style to the form:
- The form should have two fields, with corresponding labels:
  - The pilot field should accept a string of any kind.
  - The password field should also accept a string, but should hide its input behind `*`
    characters.
- The `Launch` button should have a **teal** background and a **white** foreground color.

Lastly, you need to write some logics for what will happen when you press the button:
- When the `Launch` button is pressed, the following should happen:
  - First, check if both username and password have been filled out. If not, do nothing.
  - If both have been filled out and it is the first time the user clicks the button, change the text of the button from `Launch` to `3`.
  - The second time it is clicked, change text to `2`.
  - The third time, change text to `1`
  - The fourth time, change text to `LIFTOFF!`
  - For successive presses, do nothing. The rocket has already been launched, you can't _unlaunch_ it.

If you did everything correctly, it should look like this:

![Major Tom to Ground Control](https://imgur.com/kq15Fij.gif)

Once you're done with your task, [**you can sign up here**](https://docs.google.com/forms/d/1yONgphOadXxLZW6dDXNjWKe-_vEls5jYvWUcslE6gBo)!
