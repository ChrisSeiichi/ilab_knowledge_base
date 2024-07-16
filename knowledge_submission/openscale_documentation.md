# Configuring model evaluations

If you're using the Watson OpenScale or watsonx.governance service, you can configure evaluations to generate insights about your model performance.

## Configuring model evaluations with Watson OpenScale

If you're using the Watson OpenScale service, you can configure the following types of evaluations:

  * [Quality](wos-monitor-accuracy.html)  
Evaluates how well your model predicts correct outcomes that match labeled test data.
  * [Fairness](wos-monitor-fairness.html)  
Evaluates whether your model produces biased outcomes that provide favorable results for one group over another.
  * [Drift](wos-monitor-drift.html)  
Evaluates how your model changes in accuracy and data consistency by comparing recent transactions to your training data.
  * [Drift v2](wos-driftv2-config.html)  
Evaluates changes in your model output, the accuracy of your predictions, and the distribution of your input data.
  * [Model health](wos-model-health-metrics.html)  
Evaluates how efficiently your model deployment processes your transactions.



You can also create [custom evaluations and metrics](wos-custom-metrics.html) to generate a greater variety of insights about your model performance.

Each evaluation generates metrics that you can analyze to gain insights about your model performance. For more information see, [Reviewing evaluation results](wos-insight-timechart.html).

## Configuring model evaluations with watsonx.governance

If you're using the watsonx.governance service, you can configure the following types of evaluations:

  * [Quality](wos-monitor-accuracy.html)  
Evaluates how well your model predicts correct outcomes that match labeled test data.
  * [Drift v2](wos-driftv2-config.html)  
Evaluates changes in your model output, the accuracy of your predictions, and the distribution of your input data
  * [Generative AI quality](wos-monitor-gen-quality.html)  
Measures how well your foundation model performs tasks
  * [Model health](wos-model-health-metrics.html)  
Evaluates how efficiently your model deployment processes your transactions.



**Parent topic:** [Evaluating AI models with Watson OpenScale](getting-started.html)

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


# Watson OpenScale fairness metrics

When you configure fairness evaluations in IBM Watson OpenScale, you can generate a set of metrics to evaluate the fairness of your model. You can use the fairness metrics to determine whether your model produces biased outcomes.

You can view the results of your fairness evaluations on the **Insights** dashboard in Watson OpenScale. To view results, you can select a model deployment tile and click the arrow ![navigation arrow](../model/images/wos-nav-arrow.png) in the **Fairness** evaluation section to display a summary of fairness metrics from your last evaluation. For more information, see [Reviewing fairness results](wos-insight-timechart.html#analyze-fairness).

Fairness metrics are calculated with the payload data that you provide to Watson OpenScale. For more information, see [Managing payload data](wos-payload-logging.html).

## Supported fairness metrics

Watson OpenScale supports the following fairness metrics:

## Disparate impact

In Watson OpenScale, disparate impact is specified as the fairness scores for different groups. Disparate impact compares the percentage of favorable outcomes for a monitored group to the percentage of favorable outcomes for a reference group.

  * **How it works:** When you view the details of a model deployment, the **Fairness** section of the model summary that is displayed, provides the fairness scores for different groups that are described as metrics. The fairness scores are calculated with the disparate impact formula.

  * **Uses the confusion matrix to measure performance** : No

  * **Do the math:**



    
    
                        (num_positives(privileged=False) / num_instances(privileged=False))
    Disparate impact =   ______________________________________________________________________
                        (num_positives(privileged=True) / num_instances(privileged=True))              
    

The `num_positives` value represents the number of individuals in the group who received a positive outcome, and the `num_instances` value represents the total number of individuals in the group. The `privileged=False` label specifies unprivileged groups and the `privileged=True` label specifies privileged groups. In Watson OpenScale, the positive outcomes are designated as the favorable outcomes, and the negative outcomes are designated as the unfavorable outcomes. The privileged group is designated as the reference group, and the unprivileged group is designated as the monitored group.

The calculation produces a percentage that specifies how often the rate that the unprivileged group receives the positive outcome is the same rate that the privileged group receives the positive outcome. For example, if a credit risk model assigns the “no risk” prediction to 80% of unprivileged applicants and to 100% of privileged applicants, that model has a disparate impact of 80%.

  * **Supported fairness details**

    * Watson OpenScale supports the following details for fairness metrics: 
      * The favorable percentages for each of the groups
      * Fairness averages for all the fairness groups
      * Distribution of the data for each of the monitored groups
      * Distribution of payload data



## Statistical parity difference

The statistical parity difference compares the percentage of favorable outcomes for monitored groups to reference groups in Watson OpenScale.

  * **Description** : Fairness metric that describes the fairness for the model predictions. It is the difference between the ratio of favorable outcomes in monitored and reference groups

    * **Under 0** : Higher benefits for the monitored group.
    * **At 0** : Both groups have equal benefit.
    * **Over 0** Implies higher benefit for the reference group.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :



    
    
                                        num_positives(privileged=False)     num_positives(privileged=True) 
    Statistical parity difference =  ________________________________ -  ________________________________
                                        num_instances(privileged=False)     num_instances(privileged=True)
    

## False negative rate difference

The false negative rate difference gives the percentage of positive transactions that were incorrectly scored as _negative_ by your model in Watson OpenScale.

  * **Description** : Returns the difference in false negative rates for the monitored and reference groups

    * **At 0** : Both groups have equal benefit.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating false negative rate (FNR):
    
    
                                            false negatives         
                False negative rate  =  __________________________
                                            all positives
    

The following formula is used for calculating false negative rate difference:
    
    
                False negative rate difference  =  FNR of monitored group - FNR of reference group
    

## False positive rate difference

The false positive rate difference gives the percentage of negative transactions that were incorrectly scored as _positive_ by your model in Watson OpenScale.

  * **Description** : Returns the ratio of false positive rate for the monitored group and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating false positive rate (FPR):
    
    
                                            false positives       
                False positive rate   =   ________________________
                                            total negatives
    

The following formula is used for calculating false positive rate difference:
    
    
                False positive rate difference  =   FPR of monitored group - FPR of reference group
    

## False discovery rate difference

The false discovery rate difference gives the amount of false positive transactions as a percentage of all transactions with a positive outcome in Watson OpenScale. It describes the pervasiveness of false positives among all positive transactions.

  * **Description** : Returns the difference in false discovery rate for the monitored and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating the false discovery rate (FDR):
    
    
                                                    false positives        
                False discovery rate  =   _________________________________________
                                            true positives + false positives
    

The following formula is used for calculating the false discovery rate difference:
    
    
                False discovery rate difference  = FDR of monitored group - FDR of reference group
    

## False omission rate difference

The false omission rate difference gives the number of false negative transactions as a percentage of all transactions with a negative outcome in Watson OpenScale. It describes the pervasiveness of false negatives among all negative transactions.

  * **Description** : Returns the difference in false omission rate for the monitored and reference groups

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating the false omission rate (FOR):
    
    
                                                    false negatives        
                False omission rate   =   ________________________________________
                                            true negatives + false negatives
    

The following formula is used for the false omission rate difference:
    
    
                False omission rate difference  =   FOR of monitored group - FOR of reference group                                         
    

## Error rate difference

The error rate difference gives the percentage of transactions that was incorrectly scored by your model in Watson OpenScale.

  * **Description** : Returns the difference in error rate for the monitored and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating the the error rate (ER):
    
    
                                    false positives + false negatives        
                Error rate  =   ___________________________________________
                                    all positives + all negatives
    

The following formula is used for calculating the error rate difference:
    
    
                Error rate difference  = ER of monitored group - ER of reference group
    

## Average odds difference

The average odds difference gives the percentage of transactions that was incorrectly scored by your model in Watson OpenScale.

  * **Description** : Returns the difference in error rate for the monitored and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating false positive rate (FPR):
    
    
                                            false positives       
                False positive rate   =   _________________________
                                            total negatives
    

The following formula is used for calculating true positive rate (TPR):
    
    
                                            True positives      
                True positive rate   =   ______________________
                                            All positives
    

The following formula is used for calculating average odds difference:
    
    
                                            (FPR monitored group - FPR reference group) + (TPR monitored group - TPR reference group)       
                Average odds difference  =   ___________________________________________________________________________________________
    
                                                                                        2
    

## Average absolute odds difference

The average absolute odds difference compares the average of absolute difference in false positive rates and true positive rates between monitored groups and reference groups in Watson OpenScale.

  * **Description** : Returns the average of the absolute difference in false positive rate and true positive rate for the monitored and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating false positive rate (FPR):
    
    
                                                false positives       
                False positive rate   =   ____________________________
                                                all negatives
    

The following formula is used for calculating true positive rate (TPR):
    
    
                                            True positives      
                True positive rate   =   ________________________
                                            All positives
    

The following formula is used for calculating average absolute odds difference:
    
    
                                                    |FPR monitored group - FPR reference group| + |TPR monitored group - TPR reference group|      
                Average absolute odds difference  =   ______________________________________________________________________________________________
    
                                                                                                2
    

### Measure Performance with Confusion Matrix

Watson OpenScale uses a confusion matrix to measure performance. The confusion matrix categorizes positive and negative predictions into four quadrants that represent the measurement of actual and predicted values as shown in the following example:

The true negative (TN) quadrant represents values that are actually negative and predicted as negative and the true positive (TP) quadrant represents values that are actually positive and predicted as positive. The false positive (FP) quadrant represents values that are actually negative but are predicted as positive and the the false negative (FN) quadrant represents values that are actually positive but predicted as negative.

Note: Watson OpenScale doesn't support performance measures for regression models.

**Parent topic:** [Configuring fairness evaluations](wos-monitor-fairness.html)

# Explaining model transactions

The Watson OpenScale service provides explanations for your model transactions to help you understand how predictions are determined.

You can analyze local explanations to understand the impact of factors for specific transactions or analyze global explanations to understand the general factors that impact model outcomes. The type of model that you configure determines the type of explanation that you can use to analyze your transactions.

Watson OpenScale supports explanations for structured, image, and unstructured text models. Structured models can use binary, multiclass, or regression classification problems. Image or unstructured text models can use binary or multiclass classification problems.

When you configure explainability in Watson OpenScale, you can use Local Interpretable Model-Agnostic Explanations (LIME), contrastive explanations, or Shapley Additive explanations (SHAP) to analyze transactions.

LIME identifies which features are most important for a specific data point by analyzing up to 5000 other close-by data points. In an ideal setting, the features with high importance in LIME are the features that are most important for that specific data point.

Contrastive explanations calculate how many values need to change to change the prediction or maintain the same prediction. The factors that need the maximum change are considered more important, so the features with the highest importance in contrastive explanations are the features where the model is least sensitive. For contrastive explanations, Watson OpenScale displays the maximum changes for the same outcome and the minimum changes for a changed outcome. These categories are also known as pertinent positive and pertinent negative values. These values help explain the behavior of the model in the vicinity of the data point for which an explanation is generated.

SHAP is a game-theoretic approach that explains the output of machine learning models. It connects optimal credit allocation with local explanations by using Shapley values and their related extensions. SHAP assigns each model feature an importance value for a particular prediction, which is called a _Shapley value_. The Shapley value is the average marginal contribution of a feature value across all possible groups of features. The SHAP values of the input features are the sums of the difference between baseline or expected model output and the current model output for the prediction that is being explained. The baseline model output can be based on the summary of the training data or any subset of data that explanations must be generated for. The Shapley values of a set of transactions can be combined to get global explanations that provide an overview of which features of a model are most important.

Note:

Watson OpenScale only supports global explanations for online subscriptions. SHAP explanations only support tabular data.

## Analyzing local explanations

Watson OpenScale provides different methods that you can use to view local explanations.

When you [review evaluation results](wos-insight-timechart.html), you can select the **Number of explanations** link to open the **Select an explanation** window.

![Select an explanation window displays](images/wos-select-explanation.png)

In the **Action** column select **Explain** to display the **Transaction** details page. The **Transactions details** provides different explanations, depending on which explanation methods and model types that you use.

For categorical models, on the **Explain** tab, the **Transaction details** page provides an analysis of the features that influenced the outcome of the transaction with the local explanation method that you use. For SHAP, you can select the background data that you use in the **Background data** menu to regenerate the explanation.

![Transaction details](images/wos-shap-explain-transactions.png)

On the **Inspect** tab, Watson OpenScale generates advanced contrastive explanations for binary classification models that you can use to experiment with features by changing the values to see whether the outcome changes.

![Transaction details on the inspect tab show values that might produce a different outcome](images/wos-explainability-inspect.png)

You can also view different explanations for the following type of transactions:

  * Explaining image transactions
  * Explaining unstructured text transactions
  * Explaining tabular transactions



### Explaining image transactions

For image models, you can view which parts of an image contribute positively and negatively to the predicted outcome. In the following example, the image in the positive panel shows the parts which impacted positively to the prediction. The image in the negative panel shows the parts of images that had a negative impact on the outcome.

![Explainability image classification confidence detail displays with an image of a tree frog. Different parts of the picture are highlighted in separate frames. Each part shows the extent to which it did or did not help to determine that the image is a frog.](images/wos-insight-explain-image.png)

You can also use the following notebooks to generate explanations for image models:

  * [Tutorial on generating an explanation for an image-based multiclass classification model](https://github.com/IBM/watson-openscale-samples/blob/main/IBM%20Cloud/WML/notebooks/unstructured_image/keras/Watson%20OpenScale%20Explanation%20for%20Image%20Multiclass.ipynb)
  * [Tutorial on generating an explanation for an image-based binary classification model](https://github.com/IBM/watson-openscale-samples/blob/main/IBM%20Cloud/WML/notebooks/unstructured_image/keras/Watson%20OpenScale%20Explanation%20for%20Image%20Binary%20Classification.ipynb)



### Explaining unstructured text transactions

For unstructured text models, you can view which keywords had a positive or a negative impact on the model prediction. Unstructured text models explain the importance of words or tokens.

![Explainability image classification chart is displayed. It shows confidence levels for the unstructured text](images/wos-insight-explain-text.png)

The explanation also shows the position of the identified keywords in the original text that was fed as input to the model. To change the language, select a different language from the list. The explanation runs again by using a different tokenizer.

You can also use the following notebook to generate explanations for unstructured text models:

[Tutorial on generating an explanation for a text-based model](https://github.com/IBM/watson-openscale-samples/blob/main/IBM%20Cloud/WML/notebooks/unstructured_text/spark/Watson%20OpenScale%20Explanation%20for%20Text%20Model.ipynb)

### Explaining tabular transactions

For tabular classification models, you can view the top three features that positively influence the model prediction and the top three features that negatively influence the prediction.

![Explainability image classification chart is displayed. It shows confidence levels for the tabular data model](images/wos-tabular-transactions.png)

To view local explanations, you can also select the **Explain a transaction** tab ![Explain a transaction](images/wos-insight-transact-tab.png) to open the **Recent transactions** page. The page displays all of the transactions that are processed by your model.

## Analyzing global explanations

If you enable the SHAP global explanation method when you configure explainability, you can view details for the [global explanation stability](wos-explainability-global-stability.html) metric on your dashboard. The global explanation metric calculates the degree of consistency in the global explanation over time.

When you review evaluation results for explainability, you can view the following details:

  * **Feature influence** : The most important features in descending order of the average absolute SHAP values
  * **Distribution** : The SHAP values for distribution of each feature
  * **Comparison** : The change in features influence between current global and baseline global explanation



![global explanation metrics display](images/wos-explainability-insights.png)

You can also test what-if scenarios by adjusting model transaction values to determine how different changes can affect your outcomes.

**Parent topic:** [Reviewing model transactions](wos-insight-explain.html)
