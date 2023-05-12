# rtabmap-tags

This repository [AprilTag PDFs][] contains pre-generated PDFs of AprilTag 3 tags. Currently available tags are from the tag36h11 family, in sizes of 100mm and 200mm, in US Letter and A4 paper sizes.

tagsize: The size of the tag in meters. Each tag design has a black border and a white border, but some designs have the white border on the inside and some have the black border on the inside. The tagsize is thus measured from where the two borders meet.

Source image repository: [AprilTag IMGs][]

[AprilTag PDFs]: https://github.com/rgov/apriltag-pdfs/tree/main/tag36h11

[AprilTag IMGs]:https://github.com/AprilRobotics/apriltag-imgs

# To convert .png to .pdf

## Installation 

Run command:

```
sudo apt install imagemagick
```

To reproduce these files you may need to modify the ImageMagick security policy to allow writing PDFs.

```
/etc/ImageMagick-6/policy.xml
```

In policy.xml comment line:

```
<policy domain="coder" rights="none" pattern="PDF" />
```

## Conversion

Printing a 250 mm by 250 mm square on a sheet of A3 paper. 25.4 - constant large for conversion to inches

```
convert tag36_11_00001.png \
    -density 300 \
    -scale $((100 * 250./10 * 300/25.4))% \
    -bordercolor black -border 1 \
    -gravity center -extent $((300*11.7))x$((300*16.5)) \ 
    -gravity south -annotate +0+$((300*0.25)) 'AprilTag family = tag36h11, size = 250 mm, id = 1' \
    tag1_a3.pdf
```
**Printer paper size**

| Paper     | mm               | inches |
| :-------------:|:------------------:| :-----:|
| A3    | 	297 x 420 mm    | 11.7 x 16.5 inches |
| A4     | 210 x 297 mm |  	8.3 x 11.7 inches |
| A5  | 	148.5 x 210 mm        | 5.8 x 8.3 inches |
|  AGV markers  | 	550 x 550 mm        | 21.6535 x 21.6535 inches |