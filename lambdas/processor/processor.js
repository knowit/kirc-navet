const { sendMessage } = require("./dynamodb")
// Handler
async function handler(event, context) {
  console.log('Started handling event', event)
  const message = JSON.parse(event.Records[0].body)
  const processedMessage = processMessage(message)
  await sendMessage(processedMessage)
  console.log('Finished handling event')
  context.succeed('Exit')
}

//{'message': 'test hest', 'id': '78d20fc2-9c27-4e53-96d2-d28cd2031983', 'timestamp': '2021-05-04T18:13:17.192683+02:00', 'style': '{\n    "color": "Red",\n    "size": "12px",\n    "bgcolor": "White",\n    "italic": false,\n    "bold": false\n}'}

//"color: Red; bgcolor: Violet;"

const processMessage = function (messageAsString) {
  const message = JSON.parse(messageAsString)
  const style = message.style

  var styleString = ""
  styleString += "color: " + style.color + ";"
  styleString += "size: " + style.size + ";"
  styleString += "background-color: " + style.bgcolor + ";"
  if (style.italic){
    styleString += "font-style: italic;"
  } 
  if (style.bold){
    styleString +=  "font-weight: bold;"
  } 


  return {
    message: message.message,
    timestamp: new Date().toISOString(),
    id: message.id,
    nickname: message.nickname,
    style: styleString
  }
}

exports.processMessage = processMessage
exports.handler = handler
