![image](https://github.com/user-attachments/assets/0f2a8813-abf7-4393-aa3f-ca54a43a344a)

A secure deployment must guarantee:
Client authenticity

Server authenticity

Data privacy

Data integrity

Access control

Auditability

Availability

Security Protocols

PLAINTEXT
PLAINTEXT transport layer with no authentication. Is suitable only for use
within private networks for processing data that is not sensitive since no authen‐
tication or encryption is used.
SSL
SSL transport layer with optional SSL client authentication. Is suitable for use in
insecure networks since client and server authentication as well as encryption are
supported.
SASL_PLAINTEXT
PLAINTEXT transport layer with SASL client authentication. Some SASL mech‐
anisms also support server authentication. Does not support encryption and
hence is suitable only for use within private networks.
SASL_SSL
SSL transport layer with SASL authentication. Is suitable for use in insecure net‐
works since client and server authentication as well as encryption are supported


## configures SSL for the inter-broker and internal listeners, and SASL_SSL for the external listener:
