# Important

Para llevar a cabo la comunicación TLS con el broker, es necesario convertir los ficheros de clave privada y certificado a formato "DER", para lo cual se utiliza el siguiente comando

```
openssl x509 -in client.crt -out certificate.der -outform DER
openssl rsa -in client.key -out private.der -outform DER
```