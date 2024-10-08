# Explaining model transactions

Last Updated: 2024-06-19

The Watson OpenScale service provides explanations for your model transactions to help you understand how predictions are determined.

You can analyze local explanations to understand the impact of factors for specific transactions or analyze global explanations to understand the general factors that impact model outcomes. The type of model that you configure determines the type of explanation that you can use to analyze your transactions.

Watson OpenScale supports explanations for structured, image, and unstructured text models. Structured models can use binary, multiclass, or regression classification problems. Image or unstructured text models can use binary or multiclass classification problems.

When you configure explainability in Watson OpenScale, you can use Local Interpretable Model-Agnostic Explanations (LIME), contrastive explanations, or Shapley Additive explanations (SHAP) to analyze transactions.

LIME identifies which features are most important for a specific data point by analyzing up to 5000 other close-by data points. In an ideal setting, the features with high importance in LIME are the features that are most important for that specific data point.

Contrastive explanations calculate how many values need to change to change the prediction or maintain the same prediction. The factors that need the maximum change are considered more important, so the features with the highest importance in contrastive explanations are the features where the model is least sensitive. For contrastive explanations, Watson OpenScale displays the maximum changes for the same outcome and the minimum changes for a changed outcome. These categories are also known as pertinent positive and pertinent negative values. These values help explain the behavior of the model in the vicinity of the data point for which an explanation is generated.

SHAP is a game-theoretic approach that explains the output of machine learning models. It connects optimal credit allocation with local explanations by using Shapley values and their related extensions. SHAP assigns each model feature an importance value for a particular prediction, which is called a _Shapley value_. The Shapley value is the average marginal contribution of a feature value across all possible groups of features. The SHAP values of the input features are the sums of the difference between baseline or expected model output and the current model output for the prediction that is being explained. The baseline model output can be based on the summary of the training data or any subset of data that explanations must be generated for. The Shapley values of a set of transactions can be combined to get global explanations that provide an overview of which features of a model are most important.

Note:

Watson OpenScale only supports global explanations for online subscriptions. SHAP explanations only support tabular data.

## Analyzing local explanations[](/docs/en/cloud-paks/cp-data/5.0.x?topic=transactions-explaining-model#analyze-explain-local "Copy to clipboard")

Watson OpenScale provides different methods that you can use to view local explanations.

When you [review evaluation results](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-insight-timechart.html), you can select the **Number of explanations** link to open the **Select an explanation** window.

![Select an explanation window displays](/docs/en/SSQNUZ_5.0.x/wsj/model/images/wos-select-explanation.png)

In the **Action** column select **Explain** to display the **Transaction** details page. The **Transactions details** provides different explanations, depending on which explanation methods and model types that you use.

For categorical models, on the **Explain** tab, the **Transaction details** page provides an analysis of the features that influenced the outcome of the transaction with the local explanation method that you use. For SHAP, you can select the background data that you use in the **Background data** menu to regenerate the explanation.

![Transaction details](/docs/en/SSQNUZ_5.0.x/wsj/model/images/wos-shap-explain-transactions.png)

On the **Inspect** tab, Watson OpenScale generates advanced contrastive explanations for binary classification models that you can use to experiment with features by changing the values to see whether the outcome changes.

![Transaction details on the inspect tab show values that might produce a different outcome](/docs/en/SSQNUZ_5.0.x/wsj/model/images/wos-explainability-inspect.png)

You can also view different explanations for the following type of transactions:

  * Explaining image transactions
  * Explaining unstructured text transactions
  * Explaining tabular transactions



### Explaining image transactions[](/docs/en/cloud-paks/cp-data/5.0.x?topic=transactions-explaining-model#ie-image "Copy to clipboard")

For image models, you can view which parts of an image contribute positively and negatively to the predicted outcome. In the following example, the image in the positive panel shows the parts which impacted positively to the prediction. The image in the negative panel shows the parts of images that had a negative impact on the outcome.

![Explainability image classification confidence detail displays with an image of a tree frog. Different parts of the picture are highlighted in separate frames. Each part shows the extent to which it did or did not help to determine that the image is a frog.](/docs/en/SSQNUZ_5.0.x/wsj/model/images/wos-insight-explain-image.png)

You can also use the following notebooks to generate explanations for image models:

  * [Tutorial on generating an explanation for an image-based multiclass classification model](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2FIBM%2Fwatson-openscale-samples%2Fblob%2Fmain%2FIBM%2520Cloud%2FWML%2Fnotebooks%2Funstructured_image%2Fkeras%2FWatson%2520OpenScale%2520Explanation%2520for%2520Image%2520Multiclass.ipynb)
  * [Tutorial on generating an explanation for an image-based binary classification model](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2FIBM%2Fwatson-openscale-samples%2Fblob%2Fmain%2FIBM%2520Cloud%2FWML%2Fnotebooks%2Funstructured_image%2Fkeras%2FWatson%2520OpenScale%2520Explanation%2520for%2520Image%2520Binary%2520Classification.ipynb)



### Explaining unstructured text transactions[](/docs/en/cloud-paks/cp-data/5.0.x?topic=transactions-explaining-model#ie-unstruct "Copy to clipboard")

For unstructured text models, you can view which keywords had a positive or a negative impact on the model prediction. Unstructured text models explain the importance of words or tokens.

![Explainability image classification chart is displayed. It shows confidence levels for the unstructured text](/docs/en/SSQNUZ_5.0.x/wsj/model/images/wos-insight-explain-text.png)

The explanation also shows the position of the identified keywords in the original text that was fed as input to the model. To change the language, select a different language from the list. The explanation runs again by using a different tokenizer.

You can also use the following notebook to generate explanations for unstructured text models:

[Tutorial on generating an explanation for a text-based model](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2FIBM%2Fwatson-openscale-samples%2Fblob%2Fmain%2FIBM%2520Cloud%2FWML%2Fnotebooks%2Funstructured_text%2Fspark%2FWatson%2520OpenScale%2520Explanation%2520for%2520Text%2520Model.ipynb)

### Explaining tabular transactions[](/docs/en/cloud-paks/cp-data/5.0.x?topic=transactions-explaining-model#ie-tabular-xplan "Copy to clipboard")

For tabular classification models, you can view the top three features that positively influence the model prediction and the top three features that negatively influence the prediction.

![Explainability image classification chart is displayed. It shows confidence levels for the tabular data model](/docs/en/SSQNUZ_5.0.x/wsj/model/images/wos-tabular-transactions.png)

To view local explanations, you can also select the **Explain a transaction** tab ![Explain a transaction](/docs/en/SSQNUZ_5.0.x/wsj/model/images/wos-insight-transact-tab.png) to open the **Recent transactions** page. The page displays all of the transactions that are processed by your model.

## Analyzing global explanations[](/docs/en/cloud-paks/cp-data/5.0.x?topic=transactions-explaining-model#analyze-explain-global "Copy to clipboard")

If you enable the SHAP global explanation method when you configure explainability, you can view details for the [global explanation stability](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-explainability-global-stability.html) metric on your dashboard. The global explanation metric calculates the degree of consistency in the global explanation over time.

When you review evaluation results for explainability, you can view the following details:

  * **Feature influence** : The most important features in descending order of the average absolute SHAP values
  * **Distribution** : The SHAP values for distribution of each feature
  * **Comparison** : The change in features influence between current global and baseline global explanation



![global explanation metrics display](/docs/en/SSQNUZ_5.0.x/wsj/model/images/wos-explainability-insights.png)

You can also test what-if scenarios by adjusting model transaction values to determine how different changes can affect your outcomes.

**Parent topic:** [Reviewing model transactions](/docs/en/SSQNUZ_5.0.x/wsj/model/wos-insight-explain.html)
