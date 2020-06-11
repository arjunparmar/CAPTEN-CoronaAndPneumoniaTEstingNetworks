[![GitHub issues](https://img.shields.io/github/issues/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks?style=for-the-badge)](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/issues) [![GitHub forks](https://img.shields.io/github/forks/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks?style=for-the-badge)](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/network) [![GitHub stars](https://img.shields.io/github/stars/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks?style=for-the-badge)](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/stargazers) [![GitHub license](https://img.shields.io/github/license/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks?style=for-the-badge)](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/LICENSE)
### NOTE: CAPTEN is improvisation of our previous project [COVID-19](https://github.com/arjunparmar/COVID-19). For model Architecture and Dataset prefer description given [here](https://github.com/arjunparmar/COVID-19/blob/master/README.md).
## In CAPTEN, we have added support for Pneumonia Detection!
# CAPTEN-CoronaAndPneumoniaTEstingNetworks
The novel coronavirus 2019 (COVID-2019), which first appeared in Wuhan city of China in December 2019, spread rapidly around the world and became a pandemic. It has caused a devastating effect on both daily lives, public health, and the global economy. It is critical to detect the positive cases as early as possible so as to prevent the further spread of this epidemic and to quickly treat affected patients. The need for auxiliary diagnostic tools has increased as there are no accurate automated toolkits available. Recent findings obtained using radiology imaging techniques suggest that such images contain salient information about the COVID-19 virus. Application of advanced artificial intelligence (AI) techniques coupled with radiological imaging can be helpful for the accurate detection of this disease, and can also be assistive to overcome the problem of a lack of specialized physicians in remote villages.The proposed model provides accurate diagnosis for multi-class classification (COVID vs. No-Findings vs. Pneumonia). Our model produced a classification accuracy of 96% for multi-class cases.Our model can be employed to assist radiologists in validating their initial screening, and can also be employed via cloud to immediately screen patients.
# Result
|Train Acc:98.17%|Test Acc:96.89%|
|:---:|:---:|
|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/Accuracy.png)|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/Loss.png)|<br/>
# Conclusion on Validation Dataset
## Confusion Matrix
### What is Confusion Matrix and why you need it?
Well, it is a performance measurement for machine learning classification problem where output can be two or more classes. It is a table with 4 different combinations of predicted and actual values.<br/>
![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/CM.png)<br/>
It is extremely useful for measuring Recall, Precision, Specificity, Accuracy and most importantly AUC-ROC Curve.<br/>
#### True Positive:
**Interpretation**: You predicted positive and it’s true.
#### True Negative:
**Interpretation**: You predicted negative and it’s true.
#### False Positive: (Type 1 Error)
**Interpretation**: You predicted positive and it’s false.
#### False Negative: (Type 2 Error)
**Interpretation**: You predicted negative and it’s false.
## Confusion Matrix of Validation Data:
|159|0|1|
|:---:|:---:|:---:|
|**03**|**39**|**41**|
|**01**|**06**|**153**|<br/>
## Accuracy Score: 0.87
## Report:
![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/precison.png)<br/>
![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/recall.png)<br/>
![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/F-measure.png)<br/>
|Class|Precision|Recall|F1 Score|
|:---:|:---:|:---:|:---:|
|**COVID19**|**0.98**|**0.99**|**0.98**|
|**NORMAL**|**0.87**|**0.47**|**0.61**|
|**PNEUMONIA**|**0.79**|**0.96**|**0.86**|<br/>
## GradCAM of input images:
### Grad-CAM Reveals the "Why" Behind Deep Learning Decisions.
|Class: 'COVID19'|GradCAM|
|:---:|:---:|
|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/VC49x.jpeg)|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/VC49.jpeg)|
|**Class: 'Pneumonia'**|**GradCAM**|
|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/VP61x.jpeg)|![](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/VP61.jpeg)|
## Final testing video of CAPTEN:
[![WEB-GUI](https://github.com/arjunparmar/CAPTEN-CoronaAndPneumoniaTEstingNetworks/blob/master/Images/ScreenStart.png)](https://youtu.be/oNuQ3tcgOWs)
