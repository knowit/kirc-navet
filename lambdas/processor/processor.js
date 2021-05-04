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

const translationTable = {
  color: "color:",
  size: "font-size:",
  bgcolor: "background-color:",
  italic: "font-style: italic",
  bold: "font-weight: bold",
  normal: "font-weight: normal",
  
}

/* takes an object of attr:value pairs and creates an inline-style string */
const parseStyles = (styles) => {
  let styleStr = "";
  if(Object.keys(styles).length) {
    for (const [attr, value] of Object.entries(styles)) {
        if(attr === "italic" || attr === "bold" || attr === "normal") {
            if(value == "true") {
              styleStr += translationTable[attr]
              styleStr += ";"
            }
        } else {
          styleStr += translationTable[attr] + value
          styleStr += ";"
        }
        
    }
  }

    return styleStr;
}


const processMessage = function(messageAsString) {
  const message = JSON.parse(messageAsString)
  return {
    message: message.message,
    timestamp: new Date().toISOString(),
    id: message.id,
    nickname: message.nickname,
    style: parseStyles(message.style),
  }
}
exports.processMessage = processMessage
exports.handler = handler
