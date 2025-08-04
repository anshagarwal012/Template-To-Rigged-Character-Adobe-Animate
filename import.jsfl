var folderURI = fl.browseForFolderURL("Select folder with PNGs");
if (!folderURI) {
    fl.trace("No folder selected.");
    exit;
}

var doc = fl.getDocumentDOM();
if (!doc) {
    fl.trace("No document open.");
    exit;
}

var timeline = doc.getTimeline();
var files = FLfile.listFolder(folderURI, "files");
if (!files || files.length === 0) {
    fl.trace("No PNG files found.");
    exit;
}

for (var i = 0; i < files.length; i++) {
    var fileName = files[i];
    if (!fileName.match(/\.png$/i)) continue;

    var filePath = folderURI + "/" + fileName;
    var baseName = fileName.replace(/\.[^\.]+$/, "").replace(/[^a-zA-Z0-9_]/g, "_");

    // Import file into library
    doc.importFile(filePath);

    // Get the last imported item (newest in library)
    var libItems = doc.library.items;
    var importedItem = libItems[libItems.length - 1];

    // Add new layer for this image
    timeline.addNewLayer(baseName);
    timeline.currentLayer = timeline.layers.length - 1;
    timeline.currentFrame = 0;

    // Select imported item and place on stage
    doc.library.selectItem(importedItem.name);
    doc.library.addItemToDocument({x: 0, y: 0});

    // Make sure something is selected before converting to symbol
    if (doc.selection.length > 0) {
        try {
            doc.convertToSymbol(baseName + "_symbol", "movie clip", "center");
        } catch (e) {
            fl.trace("❌ Failed to convert to symbol for: " + baseName);
        }
    } else {
        fl.trace("❌ Nothing selected after placing " + baseName);
    }

    doc.selectNone();
}

fl.trace("✅ All PNGs imported, placed in separate layers, and converted to symbols.");
