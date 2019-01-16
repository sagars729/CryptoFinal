# Cryptography Final Project
01/16/18

Cryptography Period 3

Created By Sagar Saxena and Vibhu Kundeti

This repository contains the Python3 implementations for two algorithms that use public and private keys to encrypt and decrypt messages. 
 
## Digital Signature Algorithm (DSA)
With DSA, messages are signed by the signer's private key and the signatures are verified by the signer's corresponding public key. The private key consists of a single integer x, while the public key consists of four integers (p,q,g,y) which is accompanied with the signature (r,s). The entropy, secrecy, and uniqueness of the random value k are crucial to the security of this algorithm. If any of the three are violated, it is possible that the entire private key could be revealed. The security of DSA, overall, relies on the difficulty of the discrete logarithmic problem (as compared to RSA, which relies on the difficulty of factoring large numbers). One alternative to DSA is the Eliptic Curve Digital Signature Algorithm (ECDSA) which is a faster, more lightweight variant of DSA. 

## Pallier Cryptosystem

 
