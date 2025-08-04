import os
import shutil
import argparse
import uuid
import time
import random
import xml.etree.ElementTree as ET

ET.register_namespace('', "http://ns.adobe.com/xfl/2008/")
ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")

def generate_guid():
    return str(uuid.uuid4())

def current_timestamp():
    return str(int(time.time()))

def create_symbol_file(symbols_dir, name, bitmap_name, itemID):
    ET.register_namespace("", "http://ns.adobe.com/xfl/2008/")
    ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

    symbol_root = ET.Element("DOMSymbolItem", {
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xmlns": "http://ns.adobe.com/xfl/2008/",
        "name": name,
        "itemID": itemID,
        "symbolType": "graphic",
        "lastModified": current_timestamp()
    })

    timeline = ET.SubElement(symbol_root, "timeline")
    dom_timeline = ET.SubElement(timeline, "DOMTimeline", {
        "name": name,
        "layerDepthEnabled": "true"
    })

    layers = ET.SubElement(dom_timeline, "layers")
    dom_layer = ET.SubElement(layers, "DOMLayer", {
        "name": "Layer_1",
        "color": get_random_color(),
        "current": "true",
        "isSelected": "true"
    })

    frames = ET.SubElement(dom_layer, "frames")
    dom_frame = ET.SubElement(frames, "DOMFrame", {
        "index": "0",
        "keyMode": "9728"
    })

    elements = ET.SubElement(dom_frame, "elements")
    bitmap_instance = ET.SubElement(elements, "DOMBitmapInstance", {
        "selected": "true",
        "libraryItemName": bitmap_name
    })

    path = os.path.join(symbols_dir, f"{name}.xml")
    ET.ElementTree(symbol_root).write(path, encoding='utf-8', xml_declaration=False)
    return path

def create_structure(filename,content):
    with open(filename, "a") as f:
        f.write(content)
        
def create_xfl_project(image_folder, xfl_folder):
    os.makedirs(xfl_folder, exist_ok=True)
    bitmaps_dir = os.path.join(xfl_folder, "LIBRARY")
    os.makedirs(bitmaps_dir, exist_ok=True)
    create_structure(os.path.join(xfl_folder,'girl.xfl'),'PROXY-CS5')

    dom = ET.Element("DOMDocument", {
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xmlns": "http://ns.adobe.com/xfl/2008/",
        "width": "1280",
        "height": "2000",
        "currentTimeline": "1",
        "xflVersion": "23.0",
        "creatorInfo": "Adobe Animate",
        "platform": "Windows",
        "versionInfo": "Saved by Animate Windows 24.0 build 14",
        "majorVersion": "24",
        "buildNumber": "14",
        "viewAngle3D": "100.925968316201",
        "vanishingPoint3DX": "640",
        "vanishingPoint3DY": "1000",
        "nextSceneIdentifier": "2",
        "playOptionsPlayLoop": "false",
        "playOptionsPlayPages": "false",
        "playOptionsPlayFrameActions": "false",
        "filetypeGUID": generate_guid(),
        "fileGUID": generate_guid()
    })

    media = ET.SubElement(dom, "media")
    symbols = ET.SubElement(dom, "symbols")
    timelines = ET.SubElement(dom, "timelines")
    timeline = ET.SubElement(timelines, "DOMTimeline", {
        "name": "Scene 1",
        "layerDepthEnabled": "true"
    })
    layers = ET.SubElement(timeline, "layers")

    images = sorted([img for img in os.listdir(image_folder) if img.lower().endswith('.png')])
    for index, img in enumerate(images):
        img_name = os.path.splitext(img)[0]
        bitmap_guid = generate_guid()
        img_src = os.path.join(image_folder, img)
        dst_path = os.path.join(bitmaps_dir, img)
        shutil.copy(img_src, dst_path)

        # DOMBitmapItem
        ET.SubElement(media, "DOMBitmapItem", {
            "name": img,
            "itemID": bitmap_guid,
            "sourceExternalFilepath": f"./LIBRARY/{img}",
            "sourceLastImported": current_timestamp(),
            "externalFileSize": str(os.path.getsize(dst_path)),
            "allowSmoothing": "true",
            "useImportedJPEGData": "false",
            "compressionType": "lossless",
            "originalCompressionType": "lossless",
            "quality": "50",
            "href": img,
            # "bitmapDataHRef": f"M 1 {int(time.time() * 10)}.dat",
            "frameRight": "24440",
            "frameBottom": "36720"
        })

        # Symbol XML
        symbol_xml_path = create_symbol_file(bitmaps_dir, img_name, img,bitmap_guid)
        symbols.append(ET.Element("Include", {
            "href": os.path.basename(symbol_xml_path).replace("\\", "/"),
            "loadImmediate": "false",
            "itemID": generate_guid(),
            "lastModified": current_timestamp()
        }))

        # Timeline Layer
        layer = ET.SubElement(layers, "DOMLayer", {
            "name": f"{img_name}_layer",
            "color": get_random_color(),
            "current": "false",
            "isSelected": "false",
            "autoNamed": "false"
        })
        frames = ET.SubElement(layer, "frames")
        dom_frame = ET.SubElement(frames, "DOMFrame", {"index": "0", "keyMode": "9728"})
        elements = ET.SubElement(dom_frame, "elements")
        symbol_instance = ET.SubElement(elements, "DOMSymbolInstance", {
            "libraryItemName": img_name
        })
        matrix = ET.SubElement(symbol_instance, "matrix")
        ET.SubElement(matrix, "Matrix", {
            "tx": str(29 + index * 30),
            "ty": str(82 + index * 30)
        })
        ET.SubElement(symbol_instance, "transformationPoint", {"x": "611", "y": "918"})

    ET.SubElement(dom, "scripts")
    ET.SubElement(dom, "PrinterSettings")
    ET.SubElement(dom, "publishHistory")

    tree = ET.ElementTree(dom)
    dom_path = os.path.join(xfl_folder, "DOMDocument.xml")
    tree.write(dom_path, encoding='utf-8', xml_declaration=False)
    print(f"✅ DOMDocument created at {dom_path}")

def get_random_color():
    return "#{:06X}".format(random.randint(0, 0xFFFFFF))
