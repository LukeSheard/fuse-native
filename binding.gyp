{
  "targets": [{
    "target_name": "fuse",
    "include_dirs": [
      "<!(node -e \"require('napi-macros')\")"
    ],
    "sources": [
      "fuse-native.c"
    ],
    "conditions": [
      ["OS=='mac'", {
        "variables": {
          "fuse__include_dirs%": "<!(pkg-config fuse --cflags-only-I 2>/dev/null | sed s/-I//g)",
          "fuse__libraries%": "<!(pkg-config fuse --libs-only-L --libs-only-l 2>/dev/null)"
        },
        "include_dirs": [
          "<@(fuse__include_dirs)"
        ],
        "link_settings": {
          "libraries": ["<@(fuse__libraries)"]
        },
        "defines": ["_FILE_OFFSET_BITS=64"],
        "xcode_settings": {
          "OTHER_CFLAGS": [
            "-g",
            "-O3",
            "-Wall"
          ]
        }
      }],
      ["OS=='linux'", {
        "variables": {
          "fuse__include_dirs%": "<!(pkg-config fuse3 --cflags-only-I | sed s/-I//g)",
          "fuse__library_dirs%": "",
          "fuse__libraries%": "<!(pkg-config --libs-only-L --libs-only-l fuse3)"
        },
        "include_dirs": [
          "<@(fuse__include_dirs)"
        ],
        "library_dirs": [
          "<@(fuse__library_dirs)"
        ],
        "link_settings": {
          "libraries": ["<@(fuse__libraries)"]
        },
        "cflags": [
          "-g",
          "-O3",
          "-Wall"
        ]
      }]
    ]
  }, {
    "target_name": "postinstall",
    "type": "none",
    "dependencies": ["fuse"],
    "copies": [{
      "destination": "build/Release",
      "files": [  ]
    }]
  }]
}
