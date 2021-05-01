// Use this code snippet in your app.
// If you need more information about configurations or implementing the sample code, visit the AWS docs:
// https://aws.amazon.com/developers/getting-started/nodejs/

// Load the AWS SDK
const { SecretsManager } = require('aws-sdk')
const region = 'eu-central-1'
let client, secret, decodedBinarySecret

async function getSecret(secretName) {
  // Create a Secrets Manager client
  if (client == null) {
    console.log('Creating client')
    client = new SecretsManager({
      region: region,
    })
  }
  console.log('Fetching secret', secretName)
  const data = await client.getSecretValue({ SecretId: secretName }).promise()
  if ('SecretString' in data) {
    secret = JSON.parse(data.SecretString)
    console.log('secret', secret)
    return secret
  } else {
    const buff = new Buffer.from(data.SecretBinary, 'base64')
    decodedBinarySecret = buff.toString('ascii')
    console.log('decodedBinarySecret', decodedBinarySecret)
    return decodedBinarySecret
  }
}

module.exports.getSecret = getSecret
