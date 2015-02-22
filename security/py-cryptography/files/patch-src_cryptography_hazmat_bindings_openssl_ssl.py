--- src/cryptography/hazmat/bindings/openssl/ssl.py.orig	2015-01-16 14:26:59.000000000 +0100
+++ src/cryptography/hazmat/bindings/openssl/ssl.py	2015-01-24 14:26:01.143880230 +0100
@@ -189,10 +189,6 @@
 const char *SSL_get_cipher_list(const SSL *, int);
 Cryptography_STACK_OF_SSL_CIPHER *SSL_get_ciphers(const SSL *);
 
-const COMP_METHOD *SSL_get_current_compression(SSL *);
-const COMP_METHOD *SSL_get_current_expansion(SSL *);
-const char *SSL_COMP_get_name(const COMP_METHOD *);
-
 /*  context */
 void SSL_CTX_free(SSL_CTX *);
 long SSL_CTX_set_timeout(SSL_CTX *, long);
@@ -415,6 +411,16 @@
 const long SSL_MODE_RELEASE_BUFFERS = 0;
 #endif
 
+#ifndef OPENSSL_NO_COMP
+const COMP_METHOD *SSL_get_current_compression(SSL *s);
+const COMP_METHOD *SSL_get_current_expansion(SSL *s);
+const char *SSL_COMP_get_name(const COMP_METHOD *comp);
+#else
+const void *SSL_get_current_compression(SSL *s);
+const void *SSL_get_current_expansion(SSL *s);
+const char *SSL_COMP_get_name(const void *comp);
+#endif
+
 #ifdef SSL_OP_NO_COMPRESSION
 static const long Cryptography_HAS_OP_NO_COMPRESSION = 1;
 #else
@@ -524,7 +530,7 @@
 #endif
 
 /* ALPN was added in OpenSSL 1.0.2. */
-#if OPENSSL_VERSION_NUMBER < 0x10002001L
+#if OPENSSL_VERSION_NUMBER < 0x10002001l && !defined (LIBRESSL_VERSION_NUMBER)
 int (*SSL_CTX_set_alpn_protos)(SSL_CTX *,
                                const unsigned char *,
                                unsigned) = NULL;
