# Supported machine learning providers

Last Updated: 2024-10-03

Watson Machine Learning and many third-party machine learning providers are supported for model evaluations.

Use one of these supported machine learning providers to perform payload logging, feedback logging, and to measure performance accuracy, runtime bias detection, explainability, and auto-debias function as part of your model evaluation.

  * [Watson Machine Learning](/docs/en/SSYOK8/wsj/model/wos-frameworks-wml-cloud.html#frmwrks-wml)
  * [Azure ML Studio](/docs/en/SSYOK8/wsj/model/wos-frameworks-azure-ml-studio.html#frmwrks-azure)
  * [Azure ML Service](/docs/en/SSYOK8/wsj/model/wos-frameworks-azure-ml-service.html#frmwrks-azureservice)
  * [AWS SageMaker](/docs/en/SSYOK8/wsj/model/wos-frameworks-aws-sagemaker.html#frmwrks-aws-sage)
  * [Custom](/docs/en/SSYOK8/wsj/model/wos-frameworks-custom.html#frmwrks-custom) (The custom machine learning framework must have equivalent functionality to Watson Machine Learning.)



## Support for multiple machine learning engines[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-multmleng "Copy to clipboard")

You can provision multiple machine learning engines through the Watson OpenScale dashboard configuration or the [Python SDK](https://client-docs.aiopenscale.cloud.ibm.com/html/index.html "Opens a new window or tab").

## Adding providers using the Watson OpenScale dashboard[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-multmleng-dashboard "Copy to clipboard")

  1. After you open Watson OpenScale, from the **Configure** ![configuration icon is shown](/docs/en/SSYOK8/wsj/model/images/wos-insight-config-tab.png) tab, click **Add machine learning provider**.
  2. Select the provider you want to add.
  3. Enter the required information, such as credentials, and click **Save**.



### Changing or updating details for machine learning providers[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-editingproviders-dashboard "Copy to clipboard")

Click the tile menu ![the tile menu icon](/docs/en/SSYOK8/wsj/model/images/wos-v-three-dots.png) icon and then click **View & edit details**.

## Adding machine learning providers by using the Python SDK[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-multmleng-binding "Copy to clipboard")

You can add more than one machine learning engine to Watson OpenScale by using the Python API `wos_client.service_providers.add` method.

### IBM Watson Machine Learning[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-multmleng-binding-wml "Copy to clipboard")

To add the IBM Watson Machine Learning machine learning engine, run the following command:


    WML_CREDENTIALS = {
                       "url": "https://us-south.ml.cloud.ibm.com",
                       "apikey": IBM CLOUD_API_KEY
    }
     
    wos_client.service_providers.add(
            name=SERVICE_PROVIDER_NAME,
            description=SERVICE_PROVIDER_DESCRIPTION,
            service_type=ServiceTypes.WATSON_MACHINE_LEARNING,
            deployment_space_id = WML_SPACE_ID,
            operational_space_id = "production",
            credentials=WMLCredentialsCloud(
                apikey=CLOUD_API_KEY,      ## use `apikey=IAM_TOKEN` if using IAM_TOKEN to initiate client
                url=WML_CREDENTIALS["url"],
                instance_id=None
            ),
            background_mode=False
        ).result


Copy to clipboard

### Microsoft Azure ML Studio[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-multmleng-binding-azurestudio "Copy to clipboard")

To add the Azure ML Studio machine learning engine, run the following command:


    AZURE_ENGINE_CREDENTIALS = {
        "client_id": "",
        "client_secret": "",
        "subscription_id": "",
        "tenant": ""
    }
     
    wos_client.service_providers.add(
            name=SERVICE_PROVIDER_NAME,
            description=SERVICE_PROVIDER_DESCRIPTION,
            service_type=ServiceTypes.AZURE_MACHINE_LEARNING,
            #deployment_space_id = WML_SPACE_ID,
            #operational_space_id = "production",
            credentials=AzureCredentials(
                subscription_id= AZURE_ENGINE_CREDENTIALS['subscription_id'],
                client_id = AZURE_ENGINE_CREDENTIALS['client_id'],
                client_secret= AZURE_ENGINE_CREDENTIALS['client_secret'],
                tenant = AZURE_ENGINE_CREDENTIALS['tenant']
            ),
            background_mode=False
        ).result


Copy to clipboard

### Amazon SageMaker[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-multmleng-binding-aws "Copy to clipboard")

To add the AWS Sagemaker machine learning engine, run the following command:


    SAGEMAKER_ENGINE_CREDENTIALS = {
                       'access_key_id':””,
                       'secret_access_key':””,
                       'region': '}
     
    wos_client.service_providers.add(
            name="AWS",
            description="AWS Service Provider",
            service_type=ServiceTypes.AMAZON_SAGEMAKER,
            credentials=SageMakerCredentials(
                access_key_id=SAGEMAKER_ENGINE_CREDENTIALS['access_key_id'],
                secret_access_key=SAGEMAKER_ENGINE_CREDENTIALS['secret_access_key'],
                region=SAGEMAKER_ENGINE_CREDENTIALS['region']
            ),
            background_mode=False
        ).result


Copy to clipboard

### Microsoft Azure ML Service[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-multmleng-binding-azureservice "Copy to clipboard")

To add the Azure ML Service machine learning engine, run the following command:


    service_type = "azure_machine_learning_service"
    added_service_provider_result = wos_client.service_providers.add(
            name=SERVICE_PROVIDER_NAME,
            description=SERVICE_PROVIDER_DESCRIPTION,
            service_type = service_type,
            credentials=AzureCredentials(
                subscription_id= AZURE_ENGINE_CREDENTIALS['subscription_id'],
                client_id = AZURE_ENGINE_CREDENTIALS['client_id'],
                client_secret= AZURE_ENGINE_CREDENTIALS['client_secret'],
                tenant = AZURE_ENGINE_CREDENTIALS['tenant']
            ),
            background_mode=False
        ).result


Copy to clipboard

### Producing a list of machine learning providers[](/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks#fmrk-workaround-multmleng-binding-list "Copy to clipboard")

To view a list of all the bindings, run the `list` method:

`client.service_providers.list()`

For information about specific machine learning engines, see the following topics:

  * [Add your Custom machine learning engine](/docs/en/SSYOK8/wsj/model/wos-frameworks-custom.html#cml-cusbind).
  * [Add your Microsoft Azure machine learning studio engine](/docs/en/SSYOK8/wsj/model/wos-frameworks-azure-ml-studio.html)
  * [Add your Microsoft Azure machine learning service engine](/docs/en/SSYOK8/wsj/model/wos-frameworks-azure-ml-service.html#cml-azsrvbind)
  * [Add your Amazon SageMaker machine learning engine](/docs/en/SSYOK8/wsj/model/wos-frameworks-aws-sagemaker.html)



For a coding example, see [the Watson OpenScale sample notebooks](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2FIBM%2Fwatson-openscale-samples).

**Parent topic:** [Evaluating AI models with Watson OpenScale](/docs/en/SSYOK8/wsj/model/getting-started.html)
