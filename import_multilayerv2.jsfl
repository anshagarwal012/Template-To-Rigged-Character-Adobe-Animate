var folderURI = fl.browseForFolderURL("Select folder with PNG images");
if (!folderURI) {
  fl.trace("❌ Folder selection cancelled.");
  exit;
}

var doc = fl.getDocumentDOM();
if (!doc) {
  fl.trace("❌ No FLA document open.");
  exit;
}

var flFolder = folderURI.replace("file:///", "");
var pngFiles = FLfile.listFolder(folderURI + "/", "files");
if (!pngFiles || pngFiles.length === 0) {
  fl.trace("❌ No PNG files found in the folder.");
  exit;
}

var timeline = doc.getTimeline();
fl.outputPanel.clear();

for (var i = 0; i < pngFiles.length; i++) {
  var file = pngFiles[i];
  if (!file.match(/\.png$/i)) continue;

  var name = file.replace(/\.[^.]+$/, "");
  var filePath = folderURI + "/" + file;

  // Import into library
  doc.importFile(filePath);

  fl.trace("✅ Imported into library: " + file);

  // Convert bitmap library item to symbol
  doc.library.selectItem(name);
  doc.convertToSymbol("movie clip", name, "top-left");

  // Add a new layer and place symbol instance
  timeline.addNewLayer(name);
  timeline.currentLayer = timeline.layers.length - 1;

  // Add instance of symbol to stage
  doc.library.addItemToDocument({ x: 0, y: 0 }, name);

  fl.trace("✅ Placed symbol on layer: " + name);
}
