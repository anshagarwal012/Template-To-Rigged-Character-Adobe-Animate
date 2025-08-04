from split import *
from create_fla import *

name = "ghost"
output_folder = f"output/{name}"
chords = chords = [
  {
    "layer": "mouth_shape_1_layer",
    "tx": 565.65,
    "ty": 350.75,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "head_eyes_closed_layer",
    "tx": 408.35,
    "ty": 107.15,
    "x": 380.8,
    "y": 478.05,
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "left_palm_2_layer",
    "tx": 907.7,
    "ty": 1291,
    "x": 434.7,
    "y": 58.95,
    "a": 0.780059814453125,
    "b": -0.625701904296875,
    "c": 0.625701904296875,
    "d": 0.780059814453125
  },
  {
    "layer": "Body_layer",
    "tx": 203.65,
    "ty": 292,
    "x": 595.4,
    "y": 864.35,
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "arm_left_layer",
    "tx": 669.45,
    "ty": 607.75,
    "x": 312,
    "y": 141.75,
    "a": 0.998413086,
    "b": -0.056137085,
    "c": 0.056137085,
    "d": 0.998413086
  },
  {
    "layer": "hand_left_layer",
    "tx": 810.4,
    "ty": 1189.85,
    "x": 358.65,
    "y": 141.35,
    "a": 0.423370361328125,
    "b": -0.905868530273438,
    "c": 0.905868530273438,
    "d": 0.423370361328125
  },
  {
    "layer": "arm_right_layer",
    "tx": 389.1,
    "ty": 442,
    "x": 406.2,
    "y": 54.45,
    "a": 0.866027832,
    "b": 0.499984741,
    "c": -0.499984741,
    "d": 0.866027832
  },
  {
    "layer": "hand_right_layer",
    "tx": 144.1,
    "ty": 661.8,
    "x": 389.8,
    "y": 222.3,
    "a": 0.996475219726562,
    "b": 0.0838165283203125,
    "c": -0.0838165283203125,
    "d": 0.996475219726562
  },
  {
    "layer": "eye_balls_layer",
    "tx": 476.4,
    "ty": 187.7,
    "x": 310.2,
    "y": 257.95,
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "eye_background_layer",
    "tx": 484.1,
    "ty": 226.2,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "right_palm_3_layer",
    "tx": -84.6,
    "ty": 1003.05,
    "x": 518.8,
    "y": 68.7,
    "a": 0.993133544921875,
    "b": 0.116973876953125,
    "c": -0.116973876953125,
    "d": 0.993133544921875
  },
  {
    "layer": "head_eyes_opened_layer",
    "tx": -1788.05,
    "ty": -26,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "left_palm_1_layer",
    "tx": 2204.25,
    "ty": 2147.55,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "left_palm_3_layer",
    "tx": 2231.4,
    "ty": 1903.1,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "leg_lower_left_layer",
    "tx": 1498.5,
    "ty": 82.4,
    "x": 590.65,
    "y": 1850.55,
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "leg_lower_right_layer",
    "tx": 267.6,
    "ty": 1828.8,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "mouth_shape_2_layer",
    "tx": -854.5,
    "ty": -569,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "mouth_shape_3_layer",
    "tx": -824.5,
    "ty": -539,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "mouth_shape_4_layer",
    "tx": -794.5,
    "ty": -509,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "right_hand_palm_holding_prop__1_layer",
    "tx": 2611.05,
    "ty": -388,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "right_hand_palm_holding_prop__2_layer",
    "tx": 2412.25,
    "ty": 292,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "right_palm_1_layer",
    "tx": 2412.25,
    "ty": "",
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "right_palm_2_layer",
    "tx": 2846.4,
    "ty": 44,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "thigh_left_layer",
    "tx": 1498.5,
    "ty": 82.4,
    "x": 614.65,
    "y": 1532.8,
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  },
  {
    "layer": "thigh_right_layer",
    "tx": 306,
    "ty": 1532.8,
    "x": "",
    "y": "",
    "a": "",
    "b": "",
    "c": "",
    "d": ""
  }
]

exported = slice_character(f"characters/{name}.png", output_folder, target_size=(4096, 4096))
print("✅ Exported files:", exported)
output = os.path.join(output_folder,name)
create_xfl_project(output_folder, output, chords)

