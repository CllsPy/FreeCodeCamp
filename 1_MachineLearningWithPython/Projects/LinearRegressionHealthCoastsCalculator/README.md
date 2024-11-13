# Linear Regression Health Costs Calculator

In this project, you will build a machine learning model to predict healthcare costs using **linear regression**. You will be working on this project using **Google Colaboratory**.

## Steps to Complete the Project

1. **Create a copy of the notebook**:
   - Go to the provided Google Colaboratory link.
   - Create a copy of the notebook either in your own Google account or locally.

2. **Data Preparation**:
   - The first two cells of the notebook will import the necessary libraries and the dataset.
   - Make sure to **convert categorical data to numbers** where required.
   - Split the data into **train_dataset** (80%) and **test_dataset** (20%).

3. **Label Creation**:
   - Remove the `expenses` column from both datasets and create new datasets called `train_labels` and `test_labels`.
   - These new labels will be used when training the model.

4. **Model Training**:
   - Create a regression model and train it using the `train_dataset`.
   - Once your model is trained, run the final cell to evaluate its performance on the `test_dataset`.

5. **Evaluation**:
   - To pass the challenge, the model must return a **Mean Absolute Error (MAE)** of under **3500**. This means the model should predict healthcare costs with an error of less than $3500.

6. **Final Prediction**:
   - The final cell will also predict healthcare expenses using the `test_dataset` and generate a graph to visualize the results.

## Additional Notes
- The **interactive instructional content** for the machine learning curriculum is still in development. For now, you can watch the video challenges included in the certification. 
- You may need to **seek out additional learning resources** (e.g., tutorials, documentation) as you would in a real-world project.

## Submission Instructions

- Once you complete the project and pass the test (provided in the notebook), submit your project link.
- If submitting a **Google Colaboratory** link, make sure that **link sharing is enabled** for "anyone with the link."

Good luck, and happy coding!
