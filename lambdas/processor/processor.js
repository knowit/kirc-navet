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

const parseStyle = (styleObject) => {
    return Object.entries(styleObject).map(([k, v]) => {
      if(k == "bold" && v){
        return "font-weight: bold"
      }
      else if(k == "italic" && v){
        return "font-style: italic"
      }
      else{
        return `${k}: ${v}`
      }
    }).join(';')
}

const processMessage = function (messageAsString) {
  const message = JSON.parse(messageAsString)
  const style = parseStyle(message.style)
  return {
    message: message.message,
    timestamp: new Date().toISOString(),
    id: message.id, 
    nickname: message.nickname,
    style: style,      
  }
}

exports.processMessage = processMessage
exports.handler = handler
