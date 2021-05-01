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

const processMessage = function (messageAsString) {
  const message = JSON.parse(messageAsString)
  return {
    message: message.message,
    timestamp: new Date().toISOString(),
    id: message.id,
    nickname: message.nickname,
    style: message.style,
  }
}

exports.processMessage = processMessage
exports.handler = handler
