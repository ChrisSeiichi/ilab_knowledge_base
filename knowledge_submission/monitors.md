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
