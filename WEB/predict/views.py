from django.shortcuts import render
from .models import Image
import cv2
from . import forms
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import io
import PIL
import numpy as np
import os
import datetime
import time
from WEB.settings import BASE_DIR
from WEB.settings import MEDIA_DIR
from django.core.files.base import ContentFile
from django.core.files import File
from rq import Queue
from .worker import conn
import matplotlib.pyplot as plt
import threading
import gzip
from threading import Thread, Lock
_db_lock = Lock()

q = Queue(connection=conn)

def home_view(request):
    return render(request, 'home.html')

def predict_menu(request):
    return render(request, 'predict.html')

def grad_cam(input_model, image, category_index, layer_name):
    cam = None
    # 1. Get placeholders for class output and last layer
    # Get the model's output
    output_with_batch_dim = input_model.output
    # Remove the batch dimension
    output_all_categories = output_with_batch_dim[0]
    #print(output_all_categories)
    # Retrieve only the disease category at the given category index
    y_c = output_all_categories[category_index]
    # Get the input model's layer specified by layer_name, and retrive the layer's output tensor
    spatial_map_layer = input_model.get_layer(layer_name).output
    #print(spatial_map_layer)

    # 2. Get gradients of last layer with respect to output

    # get the gradients of y_c with respect to the spatial map layer (it's a list of length 1)
    grads_l = K.gradients(y_c, spatial_map_layer)
    #print(grads_l)
    
    # Get the gradient at index 0 of the list
    grads = grads_l[0]
    #print(grads)
        
    # 3. Get hook for the selected layer and its gradient, based on given model's input
    # Hint: Use the variables produced by the previous two lines of code
    spatial_map_and_gradient_function = K.function([input_model.input], [spatial_map_layer, grads])
    
    # Put in the image to calculate the values of the spatial_maps (selected layer) and values of the gradients
    spatial_map_all_dims, grads_val_all_dims = spatial_map_and_gradient_function([image])

    # Reshape activations and gradient to remove the batch dimension
    # Shape goes from (B, H, W, C) to (H, W, C)
    # B: Batch. H: Height. W: Width. C: Channel    
    # Reshape spatial map output to remove the batch dimension
    spatial_map_val = spatial_map_all_dims[0]
    #print(spatial_map_val.shape)
    # Reshape gradients to remove the batch dimension
    grads_val = grads_val_all_dims[0]
    #print(grads_val.shape)
    
    # 4. Compute weights using global average pooling on gradient 
    # grads_val has shape (Height, Width, Channels) (H,W,C)
    # Take the mean across the height and also width, for each channel
    # Make sure weights have shape (C)
    weights = np.mean(grads_val,axis=(0,1))
    #print("W:"+str(weights))
    
    # 5. Compute dot product of spatial map values with the weights
    cam = np.dot(spatial_map_val,weights)
    #print(cam)

    
    # We'll take care of the postprocessing.
    H, W = image.shape[1], image.shape[2]
    #print(H,W)
    cam = np.maximum(cam, 0)    # ReLU so we only get positive importance
    #print("cam"+str(cam))
    cam = cv2.resize(cam, (W, H), cv2.INTER_NEAREST)
    cam = cam / cam.max()
    return cam

def prepare2(ima):
    IMG_SIZE = 300 
    if(len(ima.shape) == 3):
        ima = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
    ima = cv2.resize(ima,(300,300))
    cv2.normalize(ima, ima, 0, 255, cv2.NORM_MINMAX)
    ima=ima/255.0  # filepathread in the image, convert to grayscale
    new_array = cv2.resize(ima, (IMG_SIZE, IMG_SIZE))  # resize image to match model's expected sizing
    return new_array.reshape(-1,IMG_SIZE, IMG_SIZE,1)

def prepare(ima):
    IMG_SIZE = 300
    # img_array = ima*255
    # print('inside prepare')
    # print('prepare parameter type ' + str(type(ima)))
    img_array = ima
    if(len(ima.shape) == 3):
        img_array = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
    img_array=img_array/255.0  # filepathread in the image, convert to grayscale
    # print('img_array shape:' + str(img_array.shape))    #(200,200,3)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize image to match model's expected sizing
    # print('new_array shape:' + str(new_array.shape))      #(100,100,3)
    new_array =  new_array.reshape(-1,IMG_SIZE, IMG_SIZE,1)
    # print('out of prepare')
    print('prepared image shape' + str(new_array.shape))
    return new_array

def predict_image(image,name_image):
    try:
        print('Inside predict_image shape :' + str(image.shape))
        model_path = os.path.join(BASE_DIR, '01densenet.h5')
        model = load_model(model_path, compile = False)
        image1 = image.copy()
        print('name of image to be predicted is : ' + str(name_image))
        prediction = model.predict(prepare(image1))
        # print('prediction is : ' + str(prediction))
        prediction = np.argmax(prediction)
        x1=str(prediction)
        print('x1 is : ' + x1)
        try :
            cam = q.enqueue(grad_cam(model, prepare2(image), prediction, 'conv5_block16_concat'))
        except : 
            print('inside except')
            cam = grad_cam(model, prepare2(image), prediction, 'conv5_block16_concat')
        im_path=image
        im_path = cv2.resize(im_path,(300,300))
        plt.imshow(im_path, cmap='gray')
        plt.imshow(cam, cmap='magma', alpha=0.5)
        plt.title("Features Extracted")
        plt.axis('off')
        path = MEDIA_DIR + 'gradcam_images/gradcam.jpg'                   #For deploying on heroku, change this path to just 'gradcam.jpg' as can't use plt.savefig() with relative path on heroku                      
        plt.savefig(path)
        print(name_image)
        _,buffer_image1 = cv2.imencode('.jpeg', image1)
        f_image1 = buffer_image1.tobytes()
        f1 = ContentFile(f_image1)
        image_file = File(f1, name = name_image )
        return image_file,x1
    except Exception as e:
        print(e)


def formpage(request):
    global flag
    global ans 
    upload_image = Image()
    modified_image = Image()
    gradcam_image = Image()
    temp_form = forms.TempForm({'predictIt':'no'})
    image_form = forms.ImageForm()
    if request.method == 'POST' :
        temp_form = forms.TempForm(request.POST)
        t_value = request.POST.get('predictIt')
        if t_value == 'yes' :
            img_obj = Image.objects.filter().order_by('-id')[0]
            name_image = img_obj.uploads.name
            test_image = img_obj.uploads
            image_bytes = test_image.read()
            target_image = PIL.Image.open(io.BytesIO(image_bytes))
            target_image = target_image.resize((300,300),PIL.Image.ANTIALIAS)
            # print(type(target_image))
            image_array = np.array(target_image)
            image_file, x1 = predict_image(image_array,name_image)
            if x1 == '0':
                ans = 'You are infected with COVID-19!'
            elif x1 == '1':
                ans = 'You are not infected! You are safe!!'
            else:
                ans = 'You are infected with PNEUMONIA'
            print('Imgage_file type: ' + str(type(image_file)))
            modified_image.uploads = img_obj.uploads
            # print("next step")
            modified_image.save()
            if x1 == '0' or x1 == '2':
                gradcam_img = cv2.imread(MEDIA_DIR + '/gradcam_images/gradcam.jpg')                #For deploying on heroku, change this path to just 'gradcam.jpg' as can't use plt.savefig() with relative path on heroku
                _,buffer_gradcam = cv2.imencode('.jpeg', gradcam_img)
                f_image1 = buffer_gradcam.tobytes()
                f1 = ContentFile(f_image1)
                gradimage_file = File(f1, name = 'gradcam.jpg')
                gradcam_image.uploads = gradimage_file
                gradcam_image.save()
                context_dict = {'form' : image_form,'temp_form' : temp_form, 'prediction' : ans, 'image_show' : modified_image, 'gradcam_image' : gradcam_image, 'flag' : 1}   
            else:
                context_dict = {'form' : image_form,'temp_form' : temp_form, 'prediction' : ans, 'image_show' : modified_image}
        else :
            image_form = forms.ImageForm(request.POST,request.FILES)
            if image_form.is_valid():
                # print('inside form.vaid')
                if request.FILES.get("uploads",None) is not None:
                    # print('image prese')
                    test_image = request.FILES['uploads']
                    image_byte = test_image.read()
                    target_image = PIL.Image.open(io.BytesIO(image_byte))
                    target_image = target_image.resize((300,300),PIL.Image.ANTIALIAS)
                #   target_image = prepare(target_image, category)
                    target_image = np.array(target_image)
                    name_image = image_form.cleaned_data['uploads'].name
                #   print(type(target_image))
                #   print(target_image.shape)
                #   image_file ,x1 = predict_image(target_image,category,name_image)
                #   modified_image.uploads = image_file
                #   modified_image.save()
                    flag = 1
                    if 'uploads' in request.FILES:
                        # print('inside function')
                        upload_image.uploads = request.FILES['uploads']
                        upload_image.save()
                        # print('Saved image' + str(upload_image.uploads.name))
                        upload_obj = Image.objects.filter().order_by('-id')[0]
                        image_id = upload_obj.id
                        print("image id = {}".format(image_id))
                        context_dict = {'form' : image_form, 'temp_form' : temp_form, 'image_show':upload_image}     #uploaded image
                else:
                    context_dict = {'form' : image_form , 'temp_form' : temp_form}
            #return HttpResponse('The predicted class is {}'.format(x1))
            #messages.success(request,'The predicted class is {}'.format(x1))
            else:
                print(image_form.errors)

    else:
        image_form = forms.ImageForm()
        context_dict = {'form' : image_form, 'temp_form' : temp_form}
    print(context_dict)
    return render(request,'predict.html',context = context_dict)
