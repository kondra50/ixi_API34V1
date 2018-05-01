define({ "api": [
  {
    "type": "get",
    "url": "/api/alm/defect?recordtype=RHID&casenumber=122453",
    "title": "Defect Info",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/alm/defects?recordtype=RHID&casenumber=122453"
      }
    ],
    "name": "Defect_Info",
    "group": "ALM",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "recordtype",
            "description": "<p>RHID,RH</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "casenumber",
            "description": "<p>RHID,RH</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Result\": {\n    \"Defect Number\": 2781,\n    \"Status\": 1\n  }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "RecordType",
            "description": "<p>The RecordType is invalid.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found\n{\n\"Invalid RecordType\": \"select a valid RecordType\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/ALM/alm.py",
    "groupTitle": "ALM"
  },
  {
    "type": "get",
    "url": "/api/alm/sfdefect?recordtype=RHID&casenumber=354653&serialnumber=RH200-0046&custgui=a&ccsn=a&createdby=Customer+Service&ownerid=Customer+Service&subject=TEST+BY+MEHRDAD&desc=mydwsc&module=System&primecart=primecart&cartridgelot=cartridgelot",
    "title": "New Defect",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/alm/sfdefect?recordtype=RHID&casenumber=354653&serialnumber=RH200-0046&custgui=a&ccsn=a&createdby=Customer+Service&ownerid=Customer+Service&subject=TEST+BY+MEHRDAD&desc=mydwsc&module=System&primecart=primecart&cartridgelot=cartridgelot"
      }
    ],
    "name": "Defect_Update",
    "group": "ALM",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "recordtype",
            "description": "<p>RHID,RH</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "casenumber",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "serialnumber",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "custgui",
            "description": "<p>Custome GUI</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "ccsn",
            "description": "<p>Command Center Serial Number</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "createdby",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "ownerid",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "subject",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "desc",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "module",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "primecart",
            "description": "<p>Runs On Prime</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cartridgelot",
            "description": "<p>Cartridge Lot</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Result\": {\n    \"ALM Defect Number\": 2780,\n    \"Case Number\": \"354653\",\n    \"CreartedBy\": \"Customer Service\",\n    \"Subject\": \"TEST BY MEHRDAD\",\n    \"Successfull\": \"The defect has been sent to RHID database!\"\n  }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "RecordType",
            "description": "<p>The RecordType is invalid.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found\n{\n\"Invalid RecordType\": \"select a valid RecordType\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/ALM/alm.py",
    "groupTitle": "ALM"
  },
  {
    "type": "get",
    "url": "/api/ad/authenticate?username=mehrdad.nafisi&password=mypass",
    "title": "Authenticate user",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/ad/authenticate?username=mehrdad.nafisi&password=mypass"
      }
    ],
    "name": "ADauthenticated",
    "group": "Active_Directory",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Windows username</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Windows password</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Authenticate",
            "description": "<p>Authentication status.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Result\": {\n    \"Authenticate\": \"Successful\"\n  }\n}}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Result\": {\n    \"Authenticate\": \"InvalidCredentials\"\n  }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/AD/ad.py",
    "groupTitle": "Active_Directory"
  },
  {
    "type": "get",
    "url": "/api/epr/jobinfo?jobid=102840&username=MNAFISI",
    "title": "Job Information",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/epr/jobinfo"
      }
    ],
    "name": "GetJobInfo",
    "group": "EEPROM",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "jobid",
            "description": "<p>Expandable JOB_ID</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Expandable userId ()</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "PART_ID",
            "description": "<p>Expandable PART_ID.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "PART_DESC",
            "description": "<p>Expandable PART Description.</p>"
          },
          {
            "group": "Success 200",
            "type": "DATE",
            "optional": false,
            "field": "MFG_DATE",
            "description": "<p>Expandable Manufactering date.</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "SHELF_LIFE",
            "description": "<p>SHELF_LIFE in day.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "CTYPE",
            "description": "<p>Expandable CTYPE.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "HasAccess",
            "description": "<p>If user has access to update back expandable.</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "NOU",
            "description": "<p>Number of unit.</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "PPJ",
            "description": "<p>Number of unit.</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "Part_Programmed",
            "description": "<p>Number of part proggramed.</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "ERRCODE",
            "description": "<p>error number.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Jobininfo\": {\n    \"CTYPE\": \"\",\n    \"ERRCODE\": \"0\",\n    \"HasAccess\": \"1\",\n    \"MFG_DATE\": \"2013-02-27\",\n    \"NOU\": \"0\",\n    \"PART_DESC\": \"Assy, Lysis Chamber, Cleaned, RapidHIT\",\n    \"PART_ID\": \"P038735\",\n    \"PPJ\": \"59\",\n    \"Part_Programmed\": \"1\",\n    \"SHELF_LIFE\": \"0\"\n  }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "JobNotFound",
            "description": "<p>The Jobid was not found.</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "JobisClose",
            "description": "<p>The Jobid is closed.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found\n{\n\"code\": 404,\n\"error\": \"JobNotFound\"\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found\n{\n\"code\": 404,\n\"error\": \"JobisClosed\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/EEPROM/Eeprom.py",
    "groupTitle": "EEPROM"
  },
  {
    "type": "get",
    "url": "/api/epr/logininfo?ldapuser=mehrdad.nafisi",
    "title": "User's login",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/epr/logininfo"
      }
    ],
    "name": "GetLoginInfo",
    "group": "EEPROM",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "ldapuser",
            "description": "<p>ldap user id (firtsname.lastname)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "ACCESS",
            "description": "<p>Access to write data back to Expandable.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "GROUP_NAME",
            "description": "<p>Group Name of the User.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "USERNAME",
            "description": "<p>Expandable user name of the User.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Logininfo\": {\n    \"ACCESS\": \"0\",\n    \"GROUP_NAME\": \"SYSADMIN\",\n    \"USERNAME\": \"MNAFISS\"\n  }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "UserNotFound",
            "description": "<p>The id of the User was not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found\n{\n\"code\": 404,\n\"error\": \"UserNotFound\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/EEPROM/Eeprom.py",
    "groupTitle": "EEPROM"
  },
  {
    "type": "get",
    "url": "/api/epr/parts",
    "title": "PARTS having REFERENCE CATALOG",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/epr/parts"
      }
    ],
    "name": "GetPart",
    "group": "EEPROM",
    "version": "0.1.0",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"partlist\": [\n    {\n      \"ICFPM_USER_16\": \"(Reference Catalog #400083)\",\n      \"PART_ID\": \"P040447\"\n    },\n    {\n      \"ICFPM_USER_16\": \"(Reference Catalog #400084)\",\n      \"PART_ID\": \"P040448\"\n    },\n    {\n      \"ICFPM_USER_16\": \"(Reference Catalog #400086)\",\n      \"PART_ID\": \"P040449\"\n    },\n    {\n      \"ICFPM_USER_16\": \"(Reference Catalog #400088)\",\n      \"PART_ID\": \"P040579\"\n    },\n    {\n      \"ICFPM_USER_16\": \"(Reference Catalog #400089)\",\n      \"PART_ID\": \"P040580\"\n    },\n    {\n      \"ICFPM_USER_16\": \"(Reference Catalog #400090)\",\n      \"PART_ID\": \"P040581\"\n    }\n  ]\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "PART_ID",
            "description": "<p>Part ID.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "ICFPM_USER_16",
            "description": "<p>REFERENCE CATALOG .</p>"
          }
        ]
      }
    },
    "filename": "c:/Python34/ixi_API34/EEPROM/Eeprom.py",
    "groupTitle": "EEPROM"
  },
  {
    "type": "put",
    "url": "/api/epr/jobinfo?jobid=102840&username=mnafisi&machinname=test&cartridgeid=123&expdate=12/12/2016",
    "title": "Job - Update  Part_Programmed and EXP date",
    "name": "UpdateJobInfo",
    "group": "EEPROM",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "jobid",
            "description": "<p>Expandable JOB_ID</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Expandable userId</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "machinname",
            "description": "<p>host of the Exe file</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cartridgeid",
            "description": "<p>CARTRIDGE ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Date",
            "optional": false,
            "field": "expdate",
            "description": "<p>new EXP Date to put in</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "EXPDATE_UPDATE",
            "description": "<p>Expiration date is updated.</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "PART_PROGRAMMED",
            "description": "<p>number of Part Programmed.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "PP_UPDATED",
            "description": "<p>Part Programmed is updated.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"updated\": {\n    \"EXPDATE_UPDATED\": 1,\n    \"PART_PROGRAMMED\": 2,\n    \"PP_UPDATED\": 1\n  }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "JobNotFound",
            "description": "<p>The Jobid was not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found\n{\n\"code\": 404,\n\"error\": \"JobNotFound\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/EEPROM/Eeprom.py",
    "groupTitle": "EEPROM"
  },
  {
    "type": "get",
    "url": "/api/exp/users",
    "title": "User information",
    "name": "GetUser",
    "group": "Expandable",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "FIRST_NAME",
            "description": "<p>Firstname of the User.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "GROUP_NAME",
            "description": "<p>Group Name of the User.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "LAST_NAME",
            "description": "<p>last Name of the User.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "USER_ID",
            "description": "<p>User Id of the User.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "USER_NAME",
            "description": "<p>user  Name of the User.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "UserNotFound",
            "description": "<p>The id of the User was not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found\n{\n\"error\": \"UserNotFound\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/EXPANDABLE/Expandable.py",
    "groupTitle": "Expandable"
  },
  {
    "type": "get",
    "url": "/api/exp/jobs?partid=P041746&jobstatus=c",
    "title": "jobs",
    "name": "jobs",
    "group": "Expandable",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "partid",
            "description": "<p>Expandable PART_ID</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "jobstatus",
            "description": "<p>Expandable JOB STATUS</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "DATE_LAST_UPDT",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "JOB_ID",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "JOB_STATUS",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "JOB_TYPE",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "PART_ID",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n\"Jobs\": [\n    {\n      \"DATE_LAST_UPDT\": \"Mon, 01 Aug 2011 00:00:00 GMT\",\n      \"JOB_ID\": \"100002  \",\n      \"JOB_STATUS\": \"C\",\n      \"JOB_TYPE\": \"S\",\n      \"PART_ID\": \"P003284\"\n    },}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/EXPANDABLE/Expandable_New.py",
    "groupTitle": "Expandable"
  },
  {
    "type": "put",
    "url": "/api/rfid/jobinfo?jobid=102840&username=mnafisi&machinname=test&cartridgeid=123&serialnumber=4563",
    "title": "Job - Update  Part_Programmed and keep SN tracable in Expandable",
    "name": "UpdateRFID",
    "group": "RFID",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "jobid",
            "description": "<p>Expandable JOB_ID</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Expandable userId</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "machinname",
            "description": "<p>host of the Exe file</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cartridgeid",
            "description": "<p>CARTRIDGE ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Integer",
            "optional": false,
            "field": "serialnumber",
            "description": "<p>Expandable Serial Number</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "SN_UPDATED",
            "description": "<p>SN is taken care of by Expandable.</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "PART_PROGRAMMED",
            "description": "<p>number of Part Programmed.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "PP_UPDATED",
            "description": "<p>Part Programmed is updated.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"updated\": {\n    \"SN_UPDATED\": 1,\n    \"PART_PROGRAMMED\": 2,\n    \"PP_UPDATED\": 1\n  }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "JobNotFound",
            "description": "<p>The Jobid was not found.</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "SN",
            "description": "<p>did not update to be tracked</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found\n{\n\"code\": 404,\n\"error\": \"JobNotFound\"\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Error in SN update\n{\n\"code\": 404,\n\"error\": \"SN did not update\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/EEPROM/Eeprom.py",
    "groupTitle": "RFID"
  },
  {
    "type": "get",
    "url": "/api/sfdc/account",
    "title": "Accounts",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/sfdc/account"
      }
    ],
    "name": "Accounts",
    "group": "SFDC",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "AccountNumber",
            "description": "<p>SFDC AccountNumber</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Description",
            "description": "<p>Description</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Industry",
            "description": "<p>Industry</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "BillingCity",
            "description": "<p>BillingCountry</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "BillingCountry",
            "description": "<p>Department</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "LastActivityDate",
            "description": "<p>LastActivityDate</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Name",
            "description": "<p>Name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "OwnerId",
            "description": "<p>OwnerId</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Phone",
            "description": "<p>Phone</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Account\": [\n    {\n      \"AccountNumber\": null,\n      \"BillingCity\": \"Seattle\",\n      \"BillingCountry\": \"USA\",\n      \"Description\": null,\n      \"Industry\": \"Forensics\",\n      \"LastActivityDate\": \"2015-09-01\",\n      \"Name\": \"Washington State Patrol Crime Lab\",\n      \"OwnerId\": \"005a000000BfCdVAAV\",\n      \"Phone\": \"(206) 262-6020\"\n    },\n    {\n      \"AccountNumber\": \"ADP001\",\n      \"BillingCity\": \"Phoenix\",\n      \"BillingCountry\": \"USA\",\n      \"Description\": null,\n      \"Industry\": \"Forensics\",\n      \"LastActivityDate\": \"2016-02-04\",\n      \"Name\": \"Arizona Department of Public Safety\",\n      \"OwnerId\": \"005a000000BfCdVAAV\",\n      \"Phone\": \"(602) 223-2494\"\n    },\n    {\n      \"AccountNumber\": null,\n      \"BillingCity\": \"Denver\",\n      \"BillingCountry\": \"USA\",\n      \"Description\": null,\n      \"Industry\": \"Forensics\",\n      \"LastActivityDate\": \"2015-09-01\",\n      \"Name\": \"Denver Police Department Crime Lab\",\n      \"OwnerId\": \"005a000000BfCdVAAV\",\n      \"Phone\": \"(720) 337-2010\"\n    },\n    {\n      \"AccountNumber\": null,\n      \"BillingCity\": \"Essex\",\n      \"BillingCountry\": \"United Kingdom\",\n      \"Description\": null,\n      \"Industry\": null,\n      \"LastActivityDate\": null,\n      \"Name\": \"Genetic Research Instrumentation, LTD UK\",\n      \"OwnerId\": \"005a000000BiZyIAAV\",\n      \"Phone\": \"[44]01376332900\"\n    },\n    {\n      \"AccountNumber\": \"UMS001\",\n      \"BillingCity\": \"Pleasanton\",\n      \"BillingCountry\": \"USA\",\n      \"Description\": null,\n      \"Industry\": \"Biotechnology Company\",\n      \"LastActivityDate\": \"2014-10-17\",\n      \"Name\": \"User Meetings/Shows\",\n      \"OwnerId\": \"005a0000007vmNGAAY\",\n      \"Phone\": \"(858) 202-4502\"\n    },\n    {\n      \"AccountNumber\": \"ITS001\",\n      \"BillingCity\": \"Johnstown\",\n      \"BillingCountry\": \"USA\",\n      \"Description\": null,\n      \"Industry\": \"Distributor\",\n      \"LastActivityDate\": \"2015-09-01\",\n      \"Name\": \"ITSI-Biosciences\",\n      \"OwnerId\": \"005a000000BfCdVAAV\",\n      \"Phone\": \"(814) 262-7331\"  }\n    }\n}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/SFDC/models.py",
    "groupTitle": "SFDC"
  },
  {
    "type": "get",
    "url": "/api/sfdc/report",
    "title": "Reports list",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/sfdc/report"
      }
    ],
    "name": "Gereport",
    "group": "SFDC",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "DeveloperName",
            "description": "<p>report DeveloperName</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "ID",
            "description": "<p>Oppotinity  ID DeveloperName</p>"
          },
          {
            "group": "Success 200",
            "type": "DATE",
            "optional": false,
            "field": "Name",
            "description": "<p>Oppotinity  Name DeveloperName</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n {\n  \"Report\": [\n    {\n      \"DeveloperName\": \"All_Activities_by_Rep\",\n      \"Id\": \"00Oa0000008TQU9EAO\",\n      \"Name\": \"All Activities by Rep\"\n    },\n    {\n      \"DeveloperName\": \"of_open_opportunuities\",\n      \"Id\": \"00Oa0000008TTKtEAO\",\n      \"Name\": \"# of open opportunuities\"\n    },\n    {\n      \"DeveloperName\": \"Accounts_for_Price_Book_Update\",\n      \"Id\": \"00Oa0000008nemGEAQ\",\n      \"Name\": \"Accounts for Price Book Update\"\n    },\n    {\n      \"DeveloperName\": \"Accounts_for_TAM_Updates\",\n      \"Id\": \"00Oa0000008neueEAA\",\n      \"Name\": \"Accounts for TAM Updates\"\n    },\n\n  }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/SFDC/models.py",
    "groupTitle": "SFDC"
  },
  {
    "type": "get",
    "url": "/api/sfdc/pricebook",
    "title": "Pricebooks",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/sfdc/pricebook"
      }
    ],
    "name": "Pricebook",
    "group": "SFDC",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Name",
            "description": "<p>SFDC Price Book Name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Description",
            "description": "<p>Price Book Description</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "IsActive",
            "description": "<p>IsActive</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "IsStandard",
            "description": "<p>IsStandard</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Pricebook\": [\n    {\n      \"Description\": \"Expandable ERP Price List Integration Managed Price Book\",\n      \"IsActive\": true,\n      \"IsStandard\": false,\n      \"Name\": \"GSS - GSS Price List (Qty 1)\"\n    },\n    {\n      \"Description\": \"Expandable ERP Price List Integration Managed Price Book\",\n      \"IsActive\": true,\n      \"IsStandard\": false,\n      \"Name\": \"ILB - IL Biosystems PL (Qty 1)\"\n    },\n    {\n      \"Description\": \"Expandable ERP Price List Integration Managed Price Book\",\n      \"IsActive\": true,\n      \"IsStandard\": false,\n      \"Name\": \"KFS - Key Forensic PL (Qty 1)\"\n    },\n    {\n      \"Description\": \"Expandable ERP Price List Integration Managed Price Book\",\n      \"IsActive\": true,\n      \"IsStandard\": false,\n      \"Name\": \"ODA - Orange Cty PL (Qty 1)\"\n    },\n    {\n      \"Description\": \"Expandable ERP Price List Integration Managed Price Book\",\n      \"IsActive\": true,\n      \"IsStandard\": false,\n      \"Name\": \"RYT - Ryan Price List (Qty 1)\"\n    },\n    {\n      \"Description\": \"Expandable ERP Price List Integration Managed Price Book\",\n      \"IsActive\": true,\n      \"IsStandard\": false,\n      \"Name\": \"TRI - Triolab Price List (Qty 1)\"\n    },\n    {\n      \"Description\": \"Expandable ERP Price List Integration Managed Price Book\",\n      \"IsActive\": true,\n      \"IsStandard\": false,\n      \"Name\": \"SRP - Sci Resources PL (Qty 1)\"\n    }\n  }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/SFDC/models.py",
    "groupTitle": "SFDC"
  },
  {
    "type": "get",
    "url": "/api/sfdc/product",
    "title": "Products",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/sfdc/product"
      }
    ],
    "name": "Products",
    "group": "SFDC",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Name",
            "description": "<p>SFDC Product Name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Description",
            "description": "<p>Product Description</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "IsActive",
            "description": "<p>IsActive</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Family",
            "description": "<p>Family</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "ProductCode",
            "description": "<p>ProductCode</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Product\": [\n    {\n      \"Description\": null,\n      \"Family\": \"RIDA - RapidHIT ID Accessories\",\n      \"IsActive\": true,\n      \"Name\": \"RH ID Command Cntr License, per year, per instrument\",\n      \"ProductCode\": \"500036\"\n    },\n    {\n      \"Description\": null,\n      \"Family\": \"SUPP - Support\",\n      \"IsActive\": true,\n      \"Name\": \"International, Zone 1 Travel Charge\",\n      \"ProductCode\": \"200026\"\n    },\n    {\n      \"Description\": null,\n      \"Family\": \"SUPP - Support\",\n      \"IsActive\": true,\n      \"Name\": \"Additional Day Travel Charge\",\n      \"ProductCode\": \"200028\"\n    },\n    {\n      \"Description\": null,\n      \"Family\": \"SUPP - Support\",\n      \"IsActive\": true,\n      \"Name\": \"US, Zone 2 Travel Charge\",\n      \"ProductCode\": \"200024\"\n    },\n    {\n      \"Description\": null,\n      \"Family\": \"SUPP - Support\",\n      \"IsActive\": true,\n      \"Name\": \"US, Zone 3 Travel Charge\",\n      \"ProductCode\": \"200025\"\n    },\n    {\n      \"Description\": null,\n      \"Family\": \"RHIT - RapidHit 200 Instruments\",\n      \"IsActive\": true,\n      \"Name\": \"Kinship Analysis Module requires v2.0 or higher\",\n      \"ProductCode\": \"500032\"\n    },\n    {\n      \"Description\": null,\n      \"Family\": \"SUPP - Support\",\n      \"IsActive\": true,\n      \"Name\": \"Fluidic Pogo Plunger, RapidHIT (CC) (Spare)\",\n      \"ProductCode\": \"P040474\"\n    }\n  }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/SFDC/models.py",
    "groupTitle": "SFDC"
  },
  {
    "type": "get",
    "url": "/api/sfdc/user",
    "title": "Users",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/sfdc/user"
      }
    ],
    "name": "Users",
    "group": "SFDC",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Alias",
            "description": "<p>SFDC User Alias</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "City",
            "description": "<p>City</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "CompanyName",
            "description": "<p>CompanyName</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Country",
            "description": "<p>Country</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Department",
            "description": "<p>Department</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Email",
            "description": "<p>Email</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"User\": [\n    {\n      \"Alias\": \"JGall\",\n      \"City\": \"San Francisco\",\n      \"CompanyName\": \"IntegenX\",\n      \"ContactId\": null,\n      \"Country\": \"US\",\n      \"Department\": \"Customer Service\",\n      \"Email\": \"joannag@integenx.com\"\n    },\n    {\n      \"Alias\": \"ladmi\",\n      \"City\": null,\n      \"CompanyName\": null,\n      \"ContactId\": null,\n      \"Country\": null,\n      \"Department\": null,\n      \"Email\": \"integenx@lexnetcrm.com\"\n    },\n    {\n      \"Alias\": \"hgold\",\n      \"City\": \"Pleasanton\",\n      \"CompanyName\": \"IntegenX\",\n      \"ContactId\": null,\n      \"Country\": \"USA\",\n      \"Department\": \"Commercial Operations\",\n      \"Email\": \"howardg@integenx.com\"\n    },\n    {\n      \"Alias\": \"bennyw\",\n      \"City\": \"Pleasanton\",\n      \"CompanyName\": \"IntegenX\",\n      \"ContactId\": null,\n      \"Country\": \"USA\",\n      \"Department\": \"Field Service\",\n      \"Email\": \"bennyw@integenx.com\"\n    },\n    {\n      \"Alias\": \"j_gub\",\n      \"City\": \"Pleasanton\",\n      \"CompanyName\": \"IntegenX\",\n      \"ContactId\": null,\n      \"Country\": \"USA\",\n      \"Department\": \"Customer Service\",\n      \"Email\": \"jillg@integenx.com\"\n    },\n    {\n      \"Alias\": \"larryk\",\n      \"City\": \"Pleasanton\",\n      \"CompanyName\": \"IntegenX\",\n      \"ContactId\": null,\n      \"Country\": \"USA\",\n      \"Department\": \"Sales\",\n      \"Email\": \"larryk@integenx.com\"\n    },\n    {\n      \"Alias\": \"RGuar\",\n      \"City\": \"Medina\",\n      \"CompanyName\": \"IntegenX\",\n      \"ContactId\": null,\n      \"Country\": \"USA\",\n      \"Department\": null,\n      \"Email\": \"rossg@integenx.com\"\n    }\n  }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/SFDC/models.py",
    "groupTitle": "SFDC"
  },
  {
    "type": "get",
    "url": "/api/sfanalytic/forecast",
    "title": "forecast piplene all 75 report",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/sfanalytic/forecast"
      }
    ],
    "name": "Gereport",
    "group": "SFDC_ANALYTIC",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "AccountName",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "AccountOwner",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Amount",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Date",
            "optional": false,
            "field": "CloseDate",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Date",
            "optional": false,
            "field": "CreatedDate",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "ExpandableCustomerID",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "ListPrice",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "OpportunityID",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Probability",
            "description": "<p>%</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "ProductName",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Quantity",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "SalesPrice",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "Stage",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "TotalPrice",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n {\n  \"ForecastPipeline\": [\n    {\n      \"Account Name\": \"Metropolitan Police\",\n      \"Account Owner\": \"Elaine Julian\",\n      \"Amount\": \"$4,395,000.00\",\n      \"Close Date\": \"3/4/2016\",\n      \"Created Date\": \"3/1/2016\",\n      \"Expandable Customer ID\": \"-\",\n      \"List Price\": \"$22,500.00\",\n      \"Opportunity ID\": \"006a000001HjncD\",\n      \"Opportunity Name\": \"MetPolice-RHID-NGMSE\",\n      \"Probability (%)\": \"75%\",\n      \"Product Name\": \"RapidHIT ID NGM SElect Express 150 Sample Kit\",\n      \"Quantity\": \"6\",\n      \"Sales Price\": \"$8,250.00\",\n      \"Stage\": \"Stage 3 - Negotiating\",\n      \"Total Price\": \"$49,500.00\"\n    },\n\n  }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/SFDC/models.py",
    "groupTitle": "SFDC_ANALYTIC"
  },
  {
    "type": "get",
    "url": "/api/sfdc/opportunity",
    "title": "Opportunities",
    "sampleRequest": [
      {
        "url": "http://192.168.3.146:8090/api/sfdc/opportunity"
      }
    ],
    "name": "opportunity",
    "group": "SFDC",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "AccountId",
            "description": "<p>SFDC Account ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Amount",
            "description": "<p>Oppotinity amount</p>"
          },
          {
            "group": "Success 200",
            "type": "DATE",
            "optional": false,
            "field": "CloseDate",
            "description": "<p>Oppotinity CloseDate</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "CreatedById",
            "description": "<p>SFDC user</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "FiscalYear",
            "description": "<p>Oppotinity year.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"Oppurtinity\": [\n    {\n      \"AccountId\": \"001a000001dGcAgAAK\",\n      \"Amount\": null,\n      \"CloseDate\": \"2015-06-30\",\n      \"CreatedById\": \"005a000000BfbjOAAR\",\n      \"FiscalYear\": 2015\n    },\n    {\n      \"AccountId\": \"001a000001HeDb6AAF\",\n      \"Amount\": 25000.0,\n      \"CloseDate\": \"2014-06-30\",\n      \"CreatedById\": \"005a0000007uu5aAAA\",\n      \"FiscalYear\": 2014\n    },\n    {\n      \"AccountId\": \"001a000001JE5K6AAL\",\n      \"Amount\": 347500.0,\n      \"CloseDate\": \"2016-06-15\",\n      \"CreatedById\": \"005a000000BiZyIAAV\",\n      \"FiscalYear\": 2016\n    },\n    {\n      \"AccountId\": \"001a000001ACPkcAAH\",\n      \"Amount\": 30000.0,\n      \"CloseDate\": \"2014-09-30\",\n      \"CreatedById\": \"00530000006OyS9AAK\",\n      \"FiscalYear\": 2014\n    },\n  }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "c:/Python34/ixi_API34/SFDC/models.py",
    "groupTitle": "SFDC"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "c:/Python34/ixi_API34/static/main.js",
    "group": "c__Python34_ixi_API34_static_main_js",
    "groupTitle": "c__Python34_ixi_API34_static_main_js",
    "name": ""
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "c:/Python34/ixi_API34/static/test/main.js",
    "group": "c__Python34_ixi_API34_static_test_main_js",
    "groupTitle": "c__Python34_ixi_API34_static_test_main_js",
    "name": ""
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "c:/Python34/ixi_API34/templates/main.js",
    "group": "c__Python34_ixi_API34_templates_main_js",
    "groupTitle": "c__Python34_ixi_API34_templates_main_js",
    "name": ""
  }
] });