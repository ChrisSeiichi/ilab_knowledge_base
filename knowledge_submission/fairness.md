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
