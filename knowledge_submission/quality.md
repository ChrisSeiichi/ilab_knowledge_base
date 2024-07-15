# Quality evaluations

If you're using the Watson OpenScale or watsonx.governance service, you can use quality evaluations to monitor your model's ability to provide correct outcomes based on how well the model performs.

Quality evaluations monitor how well your model predicts accurate outcomes by identifying when model quality declines, so you can retrain your model appropriately. To evaluate the model, you provide _feedback data_ , which is labeled data where the outcome is known. Quality evaluations use metrics to evaluate how well the model predicts outcome that match the actual outcomes in the labeled data set.

The following sections describe how to configure quality evaluations:

## Configuring quality evaluations in Watson OpenScale

### Before you begin: Providing the feedback data

The feedback data is like providing an answer sheet with actual observed outcomes. The monitor can run the model as if the answers are not known, then compare the predicted outcomes to the actual outcomes and provide accuracy scores based on quality metrics.

To provide the feedback data you will use to evaluate the model click the **Endpoints** page and do one of the following:

  * Click **Upload feedback data** and upload a file with labeled data.
  * Click the **Endpoints** tab and specify an endpoint that connects to the feedback data source.



For details, see [Managing feedback data](wos-manage-feedback-data.html).

### Setting Quality thresholds

After your feedback data is available for the evaluation, configure the monitor settings. You set thresholds for acceptable performance for the model as compared to the known outcomes.

To set the threshold values, from the **Quality** tab, click the **Edit** ![The edit icon](images/wos-edit-icon.png) icon to enter values for **Quality threshold** box, then edit the values for sample size.

### Quality alert threshold

Select a value that represents an acceptable accuracy level. For example, in the sample **German Credit Risk model** provided with the auto setup, the alert for the Area under ROC metric is set **95%**. If the measured quality for the model dips below that value, an alert is triggered. A typical value for Area under ROC is 80%.

### Minimum and maximum sample sizes

By setting a minimum sample size, you prevent measuring quality until a minimum number of records are available in the evaluation data set. This ensures that the sample size is not too small to skew results. Every time quality checking runs, it uses the minimum sample size to decide the number of records on which it does the quality metrics computation.

The maximum sample size helps better manage the time and resources required to evaluate the data set. Only the most recent records are evaluated if this size is exceeded. For example, in the **German Credit Risk model** sample, the minimum sample size is set to **50** and there is no maximum size specified as it is a small sample.

## Configuring quality evaluations in watsonx.governance

When you [evaluate prompt templates](wos-eval-prompt.html), you can review a summary of quality evaluation results for the text classification task type.

The summary displays scores and violations for metrics that are calculated with default settings.

To configure quality evaluations with your own settings, you can set a minimum sample size and set threshold values for each metric. The minimum sample size indicates the minimum number of model transaction records that you want to evaluate and the threshold values create alerts when your metric scores violate your thresholds. The metric scores must be higher than the threshold values to avoid violations. Higher metric values indicate better scores.

## Supported quality metrics

When you enable quality evaluations with the Watson OpenScale or watsonx.governance service, you can generate metrics that help you determine how well your model predicts outcomes. The values that are set as your metric thresholds determine how you can interpret your metric scores. For metrics that are configured with lower thresholds, higher scores indicate better results. For metrics that are configured with upper thresholds, lower scores indicate better results.

Quality evaluations generate the following metrics:

## Area under ROC

  * **Supported services** : Watson OpenScale
  * **Description** : Area under recall and false positive rate curve to calculate sensitivity against the fallout rate
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Binary classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix



## Area under PR

  * **Supported services** : Watson OpenScale
  * **Description** : Area under precision and recall curve
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Binary classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



Area under Precision Recall gives the total for both `Precision + Recall`.
    
    
           n
    AveP = ∑ P(k)∆r(k)
          k=1
    

Precision (P) is defined as the number of true positives (Tp) over the number of true positives plus the number of false positives (Fp).
    
    
                   number of true positives
    Precision =   ______________________________________________________
    
                  (number of true positives + number of false positives)
    

Recall (R) is defined as the number of true positives (Tp) over the number of true positives plus the number of false negatives (Fn).
    
    
                number of true positives
    Recall =   ______________________________________________________
    
               (number of true positives + number of false negatives)
    

## Accuracy

  * **Supported services** : Watson OpenScale and Watsonx.governance
  * **Description** : The proportion of correct predictions
  * **Default thresholds** : Lower limit = 80%
  * **Problem types** : Binary classification and multiclass classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Understanding accuracy** :  
Accuracy can mean different things depending on the type of algorithm; 
    * **Multi-class classification** : Accuracy measures the number of times any class was predicted correctly, normalized by the number of data points. For more details, see [Multi-class classification](https://spark.apache.org/docs/2.1.0/mllib-evaluation-metrics.html#multiclass-classification) in the Apache Spark documentation.

    * **Binary classification** : For a binary classification algorithm, accuracy is measured as the area under an ROC curve. See [Binary classification](https://spark.apache.org/docs/2.1.0/mllib-evaluation-metrics.html#binary-classification) in the Apache Spark documentation for more details.

    * **Regression** : Regression algorithms are measured by using the Coefficient of Determination, or R2. For more details, see [Regression model evaluation](https://spark.apache.org/docs/2.1.0/mllib-evaluation-metrics.html#regression-model-evaluation) in the Apache Spark documentation.




## True positive rate

  * **Supported services** : Watson OpenScale
  * **Description** : Proportion of correct predictions in predictions of positive class
  * **Default thresholds** : lower limit = 80%
  * **Problem type** : Binary classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



The True positive rate is calculated by the following formula:
    
    
                      number of true positives
    TPR =  _________________________________________________________
    
            (number of true positives + number of false negatives)
    

## False positive rate

  * **Supported services** : Watson OpenScale
  * **Description** : Proportion of incorrect predictions in positive class
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Binary classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



The false positive rate is quotient of the total number of false positives that is divided by the sum of false positives and true negatives.
    
    
                            number of false positives
    False positive rate =  ______________________________________________________
    
                           (number of false positives + number of true negatives)
    

## Brier score

  * **Supported services** : Watson OpenScale
  * **Description** : Measures the mean squared difference between the predicted probability and the target value. Higher scores indicate that the model's predicted probabilities are not matching the target value.
  * **Default thresholds** : 
    * Upper limit= 80%
  * **Problem type** : Binary classification
  * **Do the math** :



The brier score metric is calculated with the following formula:
    
    
    BrierScore = 1/N * sum( (p - y)^2 )
    Where  y = actual outcome, and p = predicted probability
    

## Gini coefficient

  * **Supported services** : Watson OpenScale
  * **Description** : Gini coefficient measures how well models distinguish between two classes. It is calculated as twice the area between the ROC curve and the diagonal line of the graph plot. If the gini coefficient value is 0, the model shows no discrimination ability and a value of 1 indicates perfect discrimination.
  * **Default thresholds** : 
    * Lower limit = 80%
  * **Problem type** : Binary classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



The gini coefficient metric is calculated with the following formula:
    
    
    Gini = 2 * Area under ROC - 1
    
    

## Label skew

  * **Supported services** : watsonx.governance and Watson OpenScale
  * **Description** : Measures the asymmetry of label distributions. If skewness is 0, the dataset is perfectly balanced, if it is less than -1 or greater than 1, the distribution is highly skewed, anything in between is moderately skewed.
  * **Default thresholds** : 
    * Lower limit = -0.5
    * Upper limit = 0.5
  * **Problem type** : Binary classification and multiclass classification
  * **Chart values** : Last value in the timeframe



## Matthews correlation coefficient

  * **Supported services** : watsonx.governance and Watson OpenScale
  * **Description** : Measures the quality of binary and multiclass classifications by accounting for true and false positives and negatives. Balanced measure that can be used even if the classes are different sizes. A correlation coefficient value between -1 and +1. A coefficient of +1 represents a perfect prediction, 0 an average random prediction and -1 and inverse prediction.
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Binary classification and multiclass classification
  * **Chart values** : Last value in the timeframe
  * **Metric details available** : Confusion matrix



## Recall

  * **Supported services** : Watson OpenScale
  * **Description** : Proportion of correct predictions in positive class
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Binary classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do th math** :



Recall (R) is defined as the number of true positives (Tp) over the number of true positives plus the number of false negatives (Fn).
    
    
                           number of true positives
    Recall =   ______________________________________________________
    
               (number of true positives + number of false negatives)
    

## Precision

  * **Supported services** : Watson OpenScale
  * **Description** : Proportion of correct predictions in predictions of positive class
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Binary classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



Precision (P) is defined as the number of true positives (Tp) over the number of true positives plus the number of false positives (Fp).
    
    
                               number of true positives
    Precision =  __________________________________________________________
    
                 (number of true positives + the number of false positives)
    

## F1-Measure

  * **Supported services** : Watson OpenScale
  * **Description** : Harmonic mean of precision and recall
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Binary classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



The F1-measure is the weighted harmonic average or mean of precision and recall.
    
    
              (precision * recall)
    F1 = 2 *  ____________________
    
              (precision + recall)
    

## Logarithmic loss

  * **Supported services** : Watson OpenScale
  * **Description** : Mean of logarithms target class probabilities (confidence). It is also known as Expected log-likelihood.
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Binary classification and multiclass classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : None
  * **Do the math** :



For a binary model, Logarithmic loss is calculated by using the following formula:
    
    
    -(y log(p) + (1-y)log(1-p))
    

Where p = true label and y = predicted probability

For a multi-class model, Logarithmic loss is calculated by using the following formula:
    
    
      M
    -SUM Yo,c log(Po,c)
     c=1 
    

Where M > 2, p = true label, and y = predicted probability

## Proportion explained variance

  * **Supported services** : Watson OpenScale
  * **Description** : Proportion explained variance is the ratio of explained variance and target variance. Explained variance is the difference between target variance and variance of prediction error.
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Regression
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : None
  * **Do the math** :



The Proportion explained variance is calculated by averaging the numbers, then for each number, subtract the mean, and square the results. Then, work out the squares.
    
    
                                      sum of squares between groups 
    Proportion explained variance =  ________________________________
    
                                          sum of squares total
    

## Mean-absolute error

  * **Supported services** : Watson OpenScale
  * **Description** : Mean of absolute difference between model prediction and target value
  * **Default thresholds** : Upper limit = 80%
  * **Problem type** : Regression
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : None
  * **Do the math** :



The Mean absolute error is calculated by adding up all the absolute errors and dividing them by the number of errors.
    
    
                             SUM  | Yi - Xi | 
    Mean absolute errors =  ____________________
    
                              number of errors
    

## Mean-squared error

  * **Supported services** : Watson OpenScale
  * **Description** : Mean of squared difference between model prediction and target value
  * **Default thresholds** : Upper limit = 80%
  * **Problem type** : Regression
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : None
  * **Do the math** :



The Mean squared error in its simplest form is represented by the following formula.
    
    
                             SUM  (Yi - ^Yi) * (Yi - ^Yi)
    Mean squared errors  =  ____________________________
    
                                 number of errors
    

## R-squared

  * **Supported services** : Watson OpenScale
  * **Description** : Ratio of difference between target variance and variance for prediction error to target variance
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Regression
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : None
  * **Do the math** :



The R-squared metric is defined in the following formula.
    
    
                      explained variation
    R-squared =       _____________________
    
                        total variation
    

## Root of mean squared error

  * **Supported services** : Watson OpenScale
  * **Description** : Square root of mean of squared difference between model prediction and target value
  * **Default thresholds** : Upper limit = 80%
  * **Problem type** : Regression
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : None
  * **Do the math** :



The root of the mean-squared error is equal to the square root of the mean of (forecasts minus observed values) squared.
    
    
              ___________________________________________________________
    RMSE  =  √(forecasts - observed values)*(forecasts - observed values)
    

## Weighted True Positive Rate

  * **Supported services** : Watson OpenScale and Watsonx.governance
  * **Description** : Weighted mean of class TPR with weights equal to class probability
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Multiclass classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



The True positive rate is calculated by the following formula:
    
    
                      number of true positives
    TPR =  _________________________________________________________
    
            number of true positives + number of false negatives
    

## Weighted False Positive Rate

  * **Supported services** : Watson OpenScale and Watsonx.governance
  * **Description** : Proportion of incorrect predictions in positive class
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Multiclass classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



The Weighted False Positive Rate is the application of the FPR with weighted data.
    
    
                       number of false positives
    FPR =  ______________________________________________________
    
           (number of false positives + number of true negatives)
    

## Weighted recall

  * **Supported services** : Watson OpenScale and Watsonx.governance
  * **Description** : Weighted mean of recall with weights equal to class probability
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Multiclass classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



Weighted recall (wR) is defined as the number of true positives (Tp) over the number of true positives plus the number of false negatives (Fn) used with weighted data.
    
    
                              number of true positives
    Recall =   ______________________________________________________
    
               number of true positives + number of false negatives
    

## Weighted precision

  * **Supported services** : Watson OpenScale and watsonx.governance
  * **Description** : Weighted mean of precision with weights equal to class probability
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Multiclass classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



Precision (P) is defined as the number of true positives (Tp) over the number of true positives plus the number of false positives (Fp).
    
    
                                number of true positives
    Precision =  ________________________________________________________
    
                 number of true positives + the number of false positives
    

## Weighted F1-Measure

  * **Supported services** : Watson OpenScale and Watsonx.governance
  * **Description** : Weighted mean of F1-measure with weights equal to class probability
  * **Default thresholds** : Lower limit = 80%
  * **Problem type** : Multiclass classification
  * **Chart values** : Last value in the timeframe
  * **Metrics details available** : Confusion matrix
  * **Do the math** :



The Weighted F1-Measure is the result of using weighted data.
    
    
               precision * recall
    F1 = 2 *  ____________________
    
               precision + recall
    

If you are using the Watson OpenScale service, you can view the results of your quality evaluations on the Watson OpenScale Insights dashboard. For more information, see [Reviewing quality results](wos-insight-timechart.html#analyze-quality).

**Parent topic:** [Configuring model evaluations](wos-monitors-overview.html)
