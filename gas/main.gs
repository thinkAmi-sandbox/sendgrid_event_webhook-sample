function doPost(e) {
  const id = 'YOUR SHEET ID';
  const ss = SpreadsheetApp.openById(id);
  const sheet = ss.getSheetByName('シート1');
  
  // 一行目に最終更新日時をセット
  sheet.getRange('A1').setValue(Utilities.formatDate(new Date(), 'Asia/Tokyo', 'yyyy/MM/dd HH:mm:ss'))
  
  const rangeValues = sheet.getRange('A:A').getValues();
  let targetRow = rangeValues.filter(String).length + 1;  // A列の最終行の次の行へ入力
  
  const posts = JSON.parse(e.postData.getDataAsString());
  for (const post of posts) {
    sheet.getRange(`A${targetRow}`).setValue(toDateTime(post.timestamp));
    sheet.getRange(`B${targetRow}`).setValue(post.email);
    sheet.getRange(`C${targetRow}`).setValue(post.event);
    sheet.getRange(`D${targetRow}`).setValue(post);
  
    targetRow++;
  }
  const firstRecord = pj[0]
  
  // SendGridのEvent WebhookではHTTPステータスコードさえあれば良いけど念のため
  const result = {
    message: "hello"
  }
  
  const response = ContentService.createTextOutput();
  response.setMimeType(ContentService.MimeType.JSON);
  response.setContent(JSON.stringify(result));
  
  return response;
}
  
// Unixタイムスタンプを日時に直す
function toDateTime(unixTimestamp) {
  const dtFormat = new Intl.DateTimeFormat('ja-JP', {
    dateStyle: 'medium',
    timeStyle: 'medium',
    timeZone: 'Asia/Tokyo'
  });
    
  return dtFormat.format(new Date(unixTimestamp * 1e3));
}