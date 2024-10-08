# Configuring model evaluations

Last Updated: 2024-10-03

When you're using watsonx.governance or the Watson OpenScale service, you can configure evaluations to generate insights about your model performance.

You can configure the following types of evaluations:

  * [Quality](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-monitor-accuracy.html)
Evaluates how well your model predicts correct outcomes that match labeled test data.
  * [Fairness](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-monitor-fairness.html)
Evaluates whether your model produces biased outcomes that provide favorable results for one group over another.
  * [Drift](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-monitor-drift.html) Supported models: traditional machine learning models only
Evaluates how your model changes in accuracy and data consistency by comparing recent transactions to your training data.
  * [Drift v2](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-driftv2-config.html)
Evaluates changes in your model output, the accuracy of your predictions, and the distribution of your input data.
  * [Model health](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-model-health-metrics.html)
Evaluates how efficiently your model deployment processes your transactions.
  * [Generative AI quality](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-monitor-gen-quality.html) Supported models: LLM models only
Measures how well your foundation model performs tasks



If you're evaluating traditional machine learning models, you can also create [custom evaluations and metrics](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-custom-metrics.html) to generate a greater variety of insights about your model performance.

Each evaluation generates metrics that you can analyze to gain insights about your model performance.

When you configure evaluations, you can choose to run evaluations continuously on the following default scheduled intervals:

**Parent topic:** [Evaluating AI models with Watson OpenScale](/docs/en/SSQNUZ_5.0.x/wsj/model/getting-started.html)
