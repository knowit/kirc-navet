const { processMessage } = require('./processor')

const message = {
  id: '982b538f-1274-4bec-91c0-0abf3b50015c',
  message: 'This is a test',
  timestamp: '2021-04-11T12:45:20.301Z',
  nickname: 'Tom',
  style: 'font-style: italic;',
}

const result = processMessage(message)
