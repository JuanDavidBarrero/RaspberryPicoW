# Important

To carry out the TLS communication with the broker, it is necessary to convert the private key and certificate files to "DER" format, for which the following command is used

```
openssl x509 -in client.crt -out certificate.der -outform DER
openssl rsa -in client.key -out private.der -outform DER
```