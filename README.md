# Portuguese Man-of-war images classification using CNNs

## About the project

TODO: Insert the paper link

## Data

The data used for training, validation and testing of the models is available [here](https://drive.google.com/file/d/10938QYMglsS5pXHGS6g2-2lx2VC4wD_C/view?usp=sharing). The class "caravela" is equivalent to class `PMW` and the class "naocaravela" is equivalent to class `not-PMW`.

## Usage

For now, this repository provides the best model obtained in the study tests, the ResNet50 pre-trained with ImageNet. 

### Load the model
```
>> from resnet50-imagenet.utils import load_best_model
>> model = load_best_model()
```

### Predict one image
```
>> from resnet50-imagenet.utils import predict_image
>> img_path = "path/img.png"
>> predict_image(img_path)
>> "PMW"
```
