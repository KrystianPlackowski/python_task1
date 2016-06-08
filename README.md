# Python Excercises (Task 1)

Create a file `solution.py` with the functions described below.

### Preparation

First fork this repository, by clicking the nice [**Fork**](https://github.com/ccfd/python_task1#fork-destination-box) button on the top of the page. Then you'll have your own copy of the repository. You can open it in your favorite Python editor.

Create the needed files and add them to your repository (`git add solution.py`). Then, push them to your fork at github (`git push`). You should see yourself in the [network graph](https://github.com/ccfd/python_task1/network). Now you are ready to solve the problems at hand.

### Testing

You should test your functions before you submit them to us.

After you've solved all the excercises, push them all to your fork. Check if all your changes are visible on github.com and create a Pull Request (a nice green button on top of your fork page). The pull request will be automagickly tested with [Travis-CI](https://travis-ci.org/). The results will show as a green checkmark or a sad red x.

**Libraries:** In this task, you *can* use `scipy`, `numpy`, or `matplotlib`

## Excercise

Write a python script `solution.py` that will read a `input.png` file, reduce the resolution to 20x20 and create a text file `output.txt` filled with 20x20 characters. The character should depend on the brightness of the pixel of the image:
- ' ' for brightness < 0.3
- '-' for brightness in [0.3 0.6]
- '|' for brightness above 0.6
