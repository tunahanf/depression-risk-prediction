<div align ="center" id="toc">
  <ul style="list-style: none">
    <summary>
      <h1 align="center" id="title">Risk of Depression Prediction with Machine Learning</h1>
    </summary>
  </ul>
</div>

<h2>🧐 Rundown</h2>

*   The model predicts whether you have a high-risk or low-risk of depression.
*   Random Forest Classifier with "n_estimators=200" used as the classification algorithm.
*   The related dataset obtained from [Kaggle](https://www.kaggle.com/datasets/ikynahidwin/depression-student-dataset)

```
model.score(x_test, y_test) # Model score is mostly between .88 and .90
```

  
<h2>💻 Built with</h2>

Python libraries used in the project:

*   Pandas
*   Numpy
*   Scikit-learn


<h2>🛠️ About dataset</h2>

```
* Necessary for the prediction
```


<p>1. *Age : Age of the patient</p>

<p>2. *Academic pressure : 1 (low) to 5 (high)</p>

<p>3. *Study satisfaction : 1 (low) to 5 (high)</p>

<p>4. *Study hours : Work hours per day</p>

<p>5. *Financial stress : 1 (low) to 5 (high)</p>

<p>6. *Gender : Gender of the patient (Male/Female)</p>

<p>7. *Sleep duration : Sleep duration of the patient (in hours)</p>

<p>8. *Dietary habits : Healthy/Moderate/Unhealthy</p>

<p>9. *Have you ever had suicidal thoughts? : 1: Yes, 0: No</p>

<p>10. *Family history of mental illness? : 1: Yes, 0: No</p>
