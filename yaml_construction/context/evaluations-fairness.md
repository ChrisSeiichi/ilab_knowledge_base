# Fairness evaluations

Last Updated: 2024-10-03

You can configure fairness evaluations to determine whether your model produces biased outcomes. Use fairness evaluations to identify when your model shows a tendency to provide favorable outcomes more often for one group over another.

## Configuring fairness evaluations for traditional machine learning models[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#configuring-fairness-evaluations-for-traditional-machine-learning-models "Copy to clipboard")

If you [log payload data](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-manage-payload-data.html) when you [prepare for model evaluations](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-deploy-prepare.html), you can configure fairness evaluations.

You can configure fairness evaluations manually or you can run a [custom notebook](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2FIBM%2Fwatson-openscale-samples%2Fblob%2Fmain%2Ftraining%2520statistics%2F4.6%2Ftraining_statistics_notebook.ipynb) to generate a configuration file. You can upload the configuration file to specify the settings for your evaluation.

When you configure fairness evaluations manually, you can specify the reference group (value) that you expect to represent favorable outcomes. You can also select the corresponding model attributes (features) to monitor for bias (for example, Age or Sex), that will be compared against the reference group. Depending on your training data, you can also specify the minimum and maximum sample size for evaluations.

### Select favorable and unfavorable outcomes[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#select-favorable-and-unfavorable-outcomes "Copy to clipboard")

You must specify favorable and unfavorable outcomes when configure fairness evaluations. The values that represent a favorable outcome are derived from the `label` column in the [training data](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-manage-training-data.html). By default the `predictedLabel` column is set as the `prediction` column. Favorable and unfavorable values must be specified by using the value of the `prediction` column as a string data type, such as `0` or `1` when you are uploading training data.

### Select features[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#select-features "Copy to clipboard")

You must select the features that are the model attributes that you want to evaluate to detect bias. For example, you can evaluate features such as `Sex` or `Age` for bias. Only features that are of categorical, numeric (integer), float, or double fairness data type are supported.

The values of the features are specified as either a reference or monitored group. The monitored group represents the values that are most at risk for biased outcomes. For example, for the **`Sex`** feature, you can set `Female` and `Non-binary` as the monitored groups. For a numeric feature, such as **`Age`** , you can set `[18-25]` as the monitored group. All other values for the feature are then considered as the reference group, for example, `Sex=Male` or `Age=[26,100]`.

### Set fairness threshold[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#set-fairness-threshold "Copy to clipboard")

You can set the fairness threshold to specify an acceptable difference between the percentage of favorable outcomes for the monitored group and the percentage of favorable outcomes for the reference group. For example, if the percentage of favorable outcomes for a group in your model is 70% and the fairness threshold is set to 80%, then the fairness monitor detects bias in your model.

### Set sample size[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#set-sample-size "Copy to clipboard")

Sample sizes are used to spedicy how to process the number of transactions that are evaluated. You must set a minimum sample size to indicate the lowest number of transactions that you want to evaluate. You can also set a maximum sample size to indicate the maximum number of transactions that you want to evaluate.

### Testing for indirect bias[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#testing-for-indirect-bias "Copy to clipboard")

If you select a field that is not a training feature, called an added field, indirect bias is identified by finding associated values in the training features. For example, the profession “student” may imply a younger individual even though the Age field was excluded from model training. For details on configuring fairness evaluations to consider indirect bias, see [Configuring the Fairness monitor for indirect bias](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-indirect-bias.html).

### Mitigating bias[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#mitigating-bias "Copy to clipboard")

Passive and active debiasing are used for traditional model evaluations. Passive debiasing reveals bias, while active debiasing prevents you from carrying that bias forward by changing the model in real time for the current application. For details on interpreting results and mitigating bias in a model, see [Reviewing results from a Fairness evaluation](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-insight-debias.html).

## Configuring fairness evaluations in watsonx.governance[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#configuring-fairness-evaluations-in-watsonxgovernance "Copy to clipboard")

When you [evaluate prompt templates](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-eval-prompt.html), you can review a summary of fairness evaluation results for the text classification tasks.

### Select favorable and unfavorable outcomes[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#select-favorable-and-unfavorable-outcomes-2 "Copy to clipboard")

You must specify favorable and unfavorable outcomes when configure fairness evaluations. The values that represent a favorable outcome are derived from the `label` column in the test data that you provide. By default the `predictedLabel` column is set as the `prediction` column. Favorable and unfavorable values must be specified by using the value of the `prediction` column as a string data type, such as `0` or `1` when you are uploading training data.

### Select meta-fields[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#select-meta-fields "Copy to clipboard")

You must select meta-fields to enable watsonx.governance to identify fields that are not specified as features in the test data that you provide.

### Set fairness thresholds[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#set-fairness-thresholds "Copy to clipboard")

To configure fairness evaluations with your own settings, you can set a minimum and maximum sample size for each metric. The minimum or maximum sample size indicates the minimum or maximum number of model transactions that you want to evaluate.

You can also configure baseline data and set threshold values for each metric. Threshold values create alerts on the evaluation summary page that apper when metric scores violate your thresholds. You must set the values between the range of 0 to 1. The metric scores must be lower than the threshold values to avoid violations.

### Set sample size[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#set-sample-size-2 "Copy to clipboard")

Watsonx.governance uses sample sizes to understand how to process the number of transactions that are evaluated during evaluations. You must set a minimum sample size to indicate the lowest number of transactions that you want watsonx.governance to evaluate. You can also set a maximum sample size to indicate the maximum number of transactions that you want watsonx.governance to evaluate.

## Supported fairness metrics[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#anlz_metrics_supfairmets "Copy to clipboard")

Supported languages: English only

When you enable fairness evaluations with the Watson OpenScale or watsonx.governance service, you can view a summary of evaluation results with metrics for the type of model that you're evaluating.

If you are using the Watson OpenScale service, you can view the results of your fairness evaluations on the Watson OpenScale Insights dashboard. For more information, see [Reviewing fairness results](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-insight-timechart.html#analyze-fairness).

The following metrics are supported by fairness evaluations:

## Disparate impact[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#disparate-impact "Copy to clipboard")

Disparate impact is specified as the fairness scores for different groups. Disparate impact compares the percentage of favorable outcomes for a monitored group to the percentage of favorable outcomes for a reference group.

  * **How it works:** When you view the details of a model deployment, the **Fairness** section of the model summary that is displayed, provides the fairness scores for different groups that are described as metrics. The fairness scores are calculated with the disparate impact formula.

  * **Uses the confusion matrix to measure performance** : No

  * **Do the math:**





                        (num_positives(privileged=False) / num_instances(privileged=False))
    Disparate impact =   ______________________________________________________________________
                        (num_positives(privileged=True) / num_instances(privileged=True))


Copy to clipboard

The `num_positives` value represents the number of individuals in the group who received a positive outcome, and the `num_instances` value represents the total number of individuals in the group. The `privileged=False` label specifies unprivileged groups and the `privileged=True` label specifies privileged groups. The positive outcomes are designated as the favorable outcomes, and the negative outcomes are designated as the unfavorable outcomes. The privileged group is designated as the reference group, and the unprivileged group is designated as the monitored group.

The calculation produces a percentage that specifies how often the rate that the unprivileged group receives the positive outcome is the same rate that the privileged group receives the positive outcome. For example, if a credit risk model assigns the “no risk” prediction to 80% of unprivileged applicants and to 100% of privileged applicants, that model has a disparate impact of 80%.

  * **Supported fairness details**

    * Watson OpenScale supports the following details for fairness metrics:
      * The favorable percentages for each of the groups
      * Fairness averages for all the fairness groups
      * Distribution of the data for each of the monitored groups
      * Distribution of payload data



## Statistical parity difference[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#statistical-parity-difference "Copy to clipboard")

The statistical parity difference compares the percentage of favorable outcomes for monitored groups to reference groups.

  * **Description** : Fairness metric that describes the fairness for the model predictions. It is the difference between the ratio of favorable outcomes in monitored and reference groups

    * **Under 0** : Higher benefits for the monitored group.
    * **At 0** : Both groups have equal benefit.
    * **Over 0** Implies higher benefit for the reference group.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :





                                        num_positives(privileged=False)     num_positives(privileged=True)
    Statistical parity difference =  ________________________________ -  ________________________________
                                        num_instances(privileged=False)     num_instances(privileged=True)


Copy to clipboard

## Impact score[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#impact-score "Copy to clipboard")

The impact score compares the rate that monitored groups are selected to receive favorable outcomes to the rate that reference groups are selected to receive favorable outcomes.

  * **Do the math** :



The following formula calculates the selection rate for each group:


                                          number of individuals receiving favorable outcomes
                Selection rate  =   ________________________________________________________
                                           total number of individuals


Copy to clipboard

The following formula calculates the impact score:


                                          selection rate for monitored groups
               Impact score  =   ________________________________________________________
                                          selection rate for reference groups


Copy to clipboard

  * **Thresholds** :

    * Lower bound: 0.8
    * Upper bound: 1.0
  * **How it works** : Higher scores indicate higher selection rates for monitored groups




## False negative rate difference[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#false-negative-rate-difference "Copy to clipboard")

The false negative rate difference gives the percentage of positive transactions that were incorrectly scored as _negative_ by your model.

  * **Description** : Returns the difference in false negative rates for the monitored and reference groups

    * **At 0** : Both groups have equal benefit.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating false negative rate (FNR):


                                            false negatives
                False negative rate  =  __________________________
                                            all positives


Copy to clipboard

The following formula is used for calculating false negative rate difference:


                False negative rate difference  =  FNR of monitored group - FNR of reference group


Copy to clipboard

## False positive rate difference[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#false-positive-rate-difference "Copy to clipboard")

The false positive rate difference gives the percentage of negative transactions that were incorrectly scored as _positive_ by your model.

  * **Description** : Returns the ratio of false positive rate for the monitored group and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating false positive rate (FPR):


                                            false positives
                False positive rate   =   ________________________
                                            total negatives


Copy to clipboard

The following formula is used for calculating false positive rate difference:


                False positive rate difference  =   FPR of monitored group - FPR of reference group


Copy to clipboard

## False discovery rate difference[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#false-discovery-rate-difference "Copy to clipboard")

The false discovery rate difference gives the amount of false positive transactions as a percentage of all transactions with a positive outcome. It describes the pervasiveness of false positives among all positive transactions.

  * **Description** : Returns the difference in false discovery rate for the monitored and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating the false discovery rate (FDR):


                                                    false positives
                False discovery rate  =   _________________________________________
                                            true positives + false positives


Copy to clipboard

The following formula is used for calculating the false discovery rate difference:


                False discovery rate difference  = FDR of monitored group - FDR of reference group


Copy to clipboard

## False omission rate difference[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#false-omission-rate-difference "Copy to clipboard")

The false omission rate difference gives the number of false negative transactions as a percentage of all transactions with a negative outcome. It describes the pervasiveness of false negatives among all negative transactions.

  * **Description** : Returns the difference in false omission rate for the monitored and reference groups

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating the false omission rate (FOR):


                                                    false negatives
                False omission rate   =   ________________________________________
                                            true negatives + false negatives


Copy to clipboard

The following formula is used for the false omission rate difference:


                False omission rate difference  =   FOR of monitored group - FOR of reference group


Copy to clipboard

## Error rate difference[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#error-rate-difference "Copy to clipboard")

The error rate difference calculates the percentage of transactions that are incorrectly scored by your model.

  * **Description** : Returns the difference in error rate for the monitored and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating the the error rate (ER):


                                    false positives + false negatives
                Error rate  =   ___________________________________________
                                    all positives + all negatives


Copy to clipboard

The following formula is used for calculating the error rate difference:


                Error rate difference  = ER of monitored group - ER of reference group


Copy to clipboard

## Average odds difference[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#average-odds-difference "Copy to clipboard")

The average odds difference gives the percentage of transactions that was incorrectly scored by your model.

  * **Description** : Returns the difference in error rate for the monitored and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating false positive rate (FPR):


                                            false positives
                False positive rate   =   _________________________
                                            total negatives


Copy to clipboard

The following formula is used for calculating true positive rate (TPR):


                                            True positives
                True positive rate   =   ______________________
                                            All positives


Copy to clipboard

The following formula is used for calculating average odds difference:


                                            (FPR monitored group - FPR reference group) + (TPR monitored group - TPR reference group)
                Average odds difference  =   ___________________________________________________________________________________________

                                                                                        2


Copy to clipboard

## Average absolute odds difference[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#average-absolute-odds-difference "Copy to clipboard")

The average absolute odds difference compares the average of absolute difference in false positive rates and true positive rates between monitored groups and reference groups.

  * **Description** : Returns the average of the absolute difference in false positive rate and true positive rate for the monitored and reference groups.

    * **At 0** : Both groups have equal odds.
  * **Uses the confusion matrix to measure performance** : Yes

  * **Do the math** :




The following formula is used for calculating false positive rate (FPR):


                                                false positives
                False positive rate   =   ____________________________
                                                all negatives


Copy to clipboard

The following formula is used for calculating true positive rate (TPR):


                                            True positives
                True positive rate   =   ________________________
                                            All positives


Copy to clipboard

The following formula is used for calculating average absolute odds difference:


                                                    |FPR monitored group - FPR reference group| + |TPR monitored group - TPR reference group|
                Average absolute odds difference  =   ______________________________________________________________________________________________

                                                                                                2


Copy to clipboard

### Measure Performance with Confusion Matrix[](/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness#performance_measures "Copy to clipboard")

The confusion matrix measures performance categorizes positive and negative predictions into four quadrants that represent the measurement of actual and predicted values as shown in the following example:

The true negative (TN) quadrant represents values that are actually negative and predicted as negative and the true positive (TP) quadrant represents values that are actually positive and predicted as positive. The false positive (FP) quadrant represents values that are actually negative but are predicted as positive and the the false negative (FN) quadrant represents values that are actually positive but predicted as negative.

Note: Performance measures are not supported for regression models.

**Parent topic:** [Configuring fairness evaluations](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-monitor-fairness.html)
