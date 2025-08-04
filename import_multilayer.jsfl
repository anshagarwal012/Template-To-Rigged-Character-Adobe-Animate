var basePath = "D:\\Character\\output\\girl\\";
var parts = [
  "right_hand_palm_holding_prop__2",
  "mouth_shape_1",
  "mouth_shape_2",
  "mouth_shape_3",
  "mouth_shape_4",
  "mouth_shape_5",
  "Body",
  "eye_background",
  "eye_balls",
  "right_palm_3",
  "right_palm_2",
  "right_palm_1",
  "thigh_right",
  "leg_lower_right",
  "thigh_left",
  "leg_lower_left",
  "head_eyes_closed",
  "head_eyes_opened",
  "arm_right",
  "arm_left",
  "left_palm_3",
  "left_palm_2",
  "left_palm_1",
  "hand_right",
  "hand_left"
];

var doc = fl.getDocumentDOM();
var lib = fl.getDocumentDOM().library;

fl.outputPanel.clear();

for (var i = 0; i < parts.length; i++) {
  var part = parts[i];
  var filePath = basePath + part + ".png";
  var uri = "file:///" + filePath.replace(/\\/g, "/");

  try {
    // Import image into library
    lib.addItem(uri);

    // Wait until it's available in library (max 50 tries)
    var item, tries = 0;
    do {
      item = lib.items.find(function(x) { return x.name === part; });
      tries++;
    } while (!item && tries < 50);

    if (!item) {
      fl.trace("❌ Not found in library: " + part);
      continue;
    }

    // Convert to symbol
    lib.selectItem(part);
    var symbolName = part + "_symbol";
    doc.convertToSymbol("movie clip", symbolName, "top left");

    // Add new layer
    var timeline = doc.getTimeline();
    timeline.addNewLayer(symbolName);
    timeline.currentLayer = timeline.layers.length - 1;

    // Add symbol instance to stage
    doc.addItem({x: 0, y: 0}, symbolName);

    fl.trace("✅ Placed symbol: " + symbolName);
  } catch (e) {
    fl.trace("❌ Error with part " + part + ": " + e);
  }
}
