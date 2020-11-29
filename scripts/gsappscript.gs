function verify_account(){

  var ss = SpreadsheetApp.openById("1Q2etcT5A-LTPl-r_-MlBkg7CCZUDnfGvyIq8tVe5AjY"); //  please change the value of Sheet ID and Sheet name in next line
  SpreadsheetApp.setActiveSpreadsheet(ss);
 var sheet1 = ss.getSheetByName('Sheet1');

  var last = sheet1.getLastColumn();
  var lastrow = sheet1.getLastRow();
  var data
  const url = "https://us-central1-folk-dev-com-db.cloudfunctions.net/linkedProfileExists";

  for (j =2; j<=lastrow; j++){

//  for (j =2; j<=4; j++){
  data = sheet1.getRange(j, 1, j, last).getValues()[0];
  var data = {
   "primary_source": data[0],
    "secondary_source": data[1],
   "url": data[2],
   "domain": data[3],
   "name": data[4],
   "purpose":data[5],
   "performer": "Admin"
}

  var options = {
  'method': 'post',
  'contentType': 'application/json',
  'payload': JSON.stringify(data),
  'muteHttpExceptions': true
};

Logger.log(options);

 var response = UrlFetchApp.fetch(url, options);
  Logger.log(response);
    data = JSON.parse(response.getContentText());
    sheet1.getRange(j, 8).setValue(data.doc_id);

  }

}

function create_account(){

  var ss = SpreadsheetApp.openById("1Q2etcT5A-LTPl-r_-MlBkg7CCZUDnfGvyIq8tVe5AjY"); //  please change the value of Sheet ID and Sheet name in next line
  SpreadsheetApp.setActiveSpreadsheet(ss);
 var sheet1 = ss.getSheetByName('Sheet2');

  var last = sheet1.getLastColumn();
  var lastrow = sheet1.getLastRow();
  var data
  const url = "https://us-central1-folk-dev-com-db.cloudfunctions.net/createLinkedProfile";

  for (j =2; j<=lastrow; j++){

//  for (j =2; j<=4; j++){
  data = sheet1.getRange(j, 1, j, last).getValues()[0];
  var data = {
   "doc_id": data[0],
    "url": data[1],
   "domain": data[2],
   "type": data[3],
   "user_name": data[4],
   "performer": 'Admin'
}
  var options = {
  'method': 'post',
  'contentType': 'application/json',
  'payload': JSON.stringify(data),
  'muteHttpExceptions': true
};

Logger.log(options);

 var response = UrlFetchApp.fetch(url, options);
  Logger.log(response);
    data = JSON.parse(response.getContentText());
    sheet1.getRange(j, 8).setValue(data.status);

  }

}

function addSkills() {
  var ss = SpreadsheetApp.openById("1Q2etcT5A-LTPl-r_-MlBkg7CCZUDnfGvyIq8tVe5AjY"); //  please change the value of Sheet ID and Sheet name in next line
  SpreadsheetApp.setActiveSpreadsheet(ss);
  var sheet1 = ss.getSheetByName('Sheet2');

  var last = sheet1.getLastColumn();
  var lastrow = sheet1.getLastRow();
  var data
  const url = "https://us-central1-folk-dev-com-db.cloudfunctions.net/createLinkedProfile";

  for (j =2; j<=lastrow; j++){

//  for (j =2; j<=4; j++){
  data = sheet1.getRange(j, 1, j, last).getValues()[0];
  var data = {
   "doc_id": data[0],
    "url": data[1],
   "domain": data[2],
   "type": data[3],
   "user_name": data[4],
   "performer": 'Admin'
}
  var options = {
  'method': 'post',
  'contentType': 'application/json',
  'payload': JSON.stringify(data),
  'muteHttpExceptions': true
};

Logger.log(options);

 var response = UrlFetchApp.fetch(url, options);
  Logger.log(response);
    data = JSON.parse(response.getContentText());
    sheet1.getRange(j, 8).setValue(data.status);

  }
}


function onOpen() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var entries = [{
    name : "Linked Profile Exists",
    functionName : "verify_account"

  },{
    name : "Create Linked Profile",
    functionName : "create_account"

  }];
  sheet.addMenu("Additional Actions", entries);
};