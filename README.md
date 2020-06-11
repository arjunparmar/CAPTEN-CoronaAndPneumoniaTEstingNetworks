[![GitHub issues](https://img.shields.io/github/issues/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks?style=for-the-badge)](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/issues) [![GitHub forks](https://img.shields.io/github/forks/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks?style=for-the-badge)](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/network) [![GitHub stars](https://img.shields.io/github/stars/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks?style=for-the-badge)](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/stargazers) [![GitHub license](https://img.shields.io/github/license/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks?style=for-the-badge)](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/LICENSE)
### NOTE: CAPTEN is development of our previous project [COVID-19](https://github.com/arjunparmar/COVID-19). For model Architecture and Dataset prefer description given [here](https://github.com/arjunparmar/COVID-19/blob/master/README.md).
# CAPTEN-CoronaAndPneumoniaTEstingNetworks
The novel coronavirus 2019 (COVID-2019), which first appeared in Wuhan city of China in December 2019, spread rapidly around the world and became a pandemic. It has caused a devastating effect on both daily lives, public health, and the global economy. It is critical to detect the positive cases as early as possible so as to prevent the further spread of this epidemic and to quickly treat affected patients. The need for auxiliary diagnostic tools has increased as there are no accurate automated toolkits available. Recent findings obtained using radiology imaging techniques suggest that such images contain salient information about the COVID-19 virus. Application of advanced artificial intelligence (AI) techniques coupled with radiological imaging can be helpful for the accurate detection of this disease, and can also be assistive to overcome the problem of a lack of specialized physicians in remote villages.The proposed model is provide accurate diagnostics for multi-class classification (COVID vs. No-Findings vs. Pneumonia). Our model produced a classification accuracy of 87% for multi-class cases.Our model can be employed to assist radiologists in validating their initial screening, and can also be employed via cloud to immediately screen patients.
# Result
|Train Acc:98.17%|Test Acc:96.89%|
|:---:|:---:|
|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/Accuracy.png)|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/Loss.png)|<br/>
# Conclusion on Validation Dataset
## Confusion Matrix
|159|0|1|
|:---:|:---:|:---:|
|**03**|**39**|**41**|
|**01**|**06**|**153**|<br/>
## Accuracy Score: 0.87
## Report:
|Class|Precision|Recall|F1 Score|
|:---:|:---:|:---:|:---:|
|**COVID19**|**0.98**|**0.99**|**0.98**|
|**NORMAL**|**0.87**|**0.47**|**0.61**|
|**PNEUMONIA**|**0.79**|**0.96**|**0.86**|<br/>
## GradCAM of input images:
|Class: COVID19|GradCAM|
|:---:|:---:|
|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/VC49x.jpeg)|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/VC49.jpeg)|
|Class: Pneumonia|GradCAM|
|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/VP61x.jpeg)|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/VP61.jpeg)|
