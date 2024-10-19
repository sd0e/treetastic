import torch

def objectDetection(imageLocation):
    # model = torch.hub.load('ultralytics/yolov5', 'yolov5x6', pretrained=False)

    model = torch.hub.load('C:/Users/sebas/Dev/github/treetastic/model/yolov5','custom', path='C:/Users/sebas/Dev/github/treetastic/model/yolov5/last.pt',force_reload=True,source='local')

    modelWithCars = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # Images
    imgs = [imageLocation]  # batch of images

    # Inference
    results = model(imgs)
    resultsCars = modelWithCars(imgs)

    # Results
    results.print()
    results.save()  # or .show()

    # Results
    resultsCars.print()
    resultsCars.save()  # or .show()

    results.xyxy[0]  # img1 predictions (tensor)
    results.pandas().xyxy[0]  # img1 predictions (pandas)
    #      xmin    ymin    xmax   ymax  confidence  class    name
    # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
    # 1  433.50  433.50   517.5  714.5    0.687988     27     tie
    # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
    # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
    return results.pandas().xyxy[0]

# objectDetection("C:/Users/sebas/Downloads/MVIMG_20230317_213244.jpg")
# objectDetection("C:/Users/sebas/Downloads/Photos/IMG_20241019_121612143.jpg")
print(objectDetection("C:/Users/sebas/Downloads/Photos/IMG_20241019_121830025.jpg"))