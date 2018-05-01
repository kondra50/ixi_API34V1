define({ "api": [
  {
    "type": "get",
    "url": "/user/:id",
    "title": "",
    "version": "0.0.0",
    "filename": "ixi_API34/EXPANDABLE/Expandable.py",
    "group": "C__Python34_ixi_API34_EXPANDABLE_Expandable_py",
    "groupTitle": "C__Python34_ixi_API34_EXPANDABLE_Expandable_py",
    "name": "GetUserId"
  },
  {
    "type": "get",
    "url": "/parts/",
    "title": "",
    "name": "EEPROM",
    "group": "User",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "partid",
            "description": "<p>PART_ID of the User.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "part_desc",
            "description": "<p>PART_DESC of the User.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "ixi_API34/EEPROM/Eeprom.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/users/",
    "title": "Request User information",
    "name": "GetUser",
    "group": "User",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "firstname",
            "description": "<p>Firstname of the User.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lastname",
            "description": "<p>Lastname of the User.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "ixi_API34/EXPANDABLE/Expandable.py",
    "groupTitle": "User"
  }
] });