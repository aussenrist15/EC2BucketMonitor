import boto3

from PIL import Image

cat = set()
dog = set()
car = set()
bike = set()
cycle = set()
s3Bucket = boto3.resource('s3')

myBucket = s3Bucket.Bucket("basitbucket326input")

while(True):
    count = 0
    for filee in myBucket.objects.all():
        fileName = filee.key
        # print(fileName)
        if('cat') in fileName:
            cat.add(fileName)
        if('bike' in fileName):
            bike.add(fileName)
        if('dog' in fileName):
            dog.add(fileName)
        if('car' in fileName):
            car.add(fileName)
        if('cycle' in fileName):
            cycle.add(fileName)
        count += 1
    if(count == 15):
        break

print("All files uploaded to the bucket. Now Downloading All Of Them ...")
s3 = boto3.client('s3')


for image in cat:
    with open(image, 'wb') as f:
        s3.download_fileobj('basitbucket326input', image, f)
for image in cat:
    image1 = Image.open(image)
    im1 = image1.convert('RGB')
    im1.save("cat.pdf")
s3.upload_file("cat.pdf", "basitbucket326output", "cat.pdf")
print("Generated cat.pdf. Now Uploading ...")


for image in dog:
    with open(image, 'wb') as f:
        s3.download_fileobj('basitbucket326input', image, f)
for image in dog:
    image1 = Image.open(image)
    im1 = image1.convert('RGB')
    im1.save("dog.pdf")
s3.upload_file("dog.pdf", "basitbucket326output", "dog.pdf")
print("Generated dog.pdf. Now Uploading ...")


for image in car:
    with open(image, 'wb') as f:
        s3.download_fileobj('basitbucket326input', image, f)
for image in car:
    image1 = Image.open(image)
    im1 = image1.convert('RGB')
    im1.save("car.pdf")
s3.upload_file("car.pdf", "basitbucket326output", "car.pdf")
print("Generated car.pdf. Now Uploading ...")


for image in bike:
    with open(image, 'wb') as f:
        s3.download_fileobj('basitbucket326input', image, f)
for image in bike:
    image1 = Image.open(image)
    im1 = image1.convert('RGB')
    im1.save("bike.pdf")
s3.upload_file("bike.pdf", "basitbucket326output", "bike.pdf")
print("Generated bike.pdf. Now Uploading ...")


for image in cycle:
    with open(image, 'wb') as f:
        s3.download_fileobj('basitbucket326input', image, f)
for image in cycle:
    image1 = Image.open(image)
    im1 = image1.convert('RGB')
    im1.save("cycle.pdf")
s3.upload_file("cycle.pdf", "basitbucket326output", "cycle.pdf")
print("Generated cycle.pdf. Now Uploading ...")


print("Files uploaded to the output directory...")
