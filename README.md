# 🔒 DSA with MD5 for Digital Signatures

This project aims to implement a digital signature system using the Digital Signature Algorithm (DSA) combined with the Message-Digest Algorithm 5 (MD5) hash function. The goal is to create a secure method for ensuring the integrity and authenticity of digital messages.

---

## 📋 Prerequisites

- 🖥️ **Programming Language**: Python
- 🛠️ **Python Version**: 3.x
- 🔧 **IDE/Text Editor**: Any text editor or IDE for editing Python code (e.g., VSCode)
- 📄 **Knowledge**: Basic understanding of cryptographic algorithms, specifically DSA and MD5

## 🌟 Key Elements

### 🔒 Digital Signature Algorithm (DSA):
  - **Key Generation**: Generate and compute prime numbers and keys.
  - **Message Hashing**: Convert the message to its hash value using MD5.
  - **Signing**: Generate a digital signature based on the message digest.
  - **Verification**: Verify the signature to ensure message authenticity.

### 🗝️ MD5 Hash Function:
  - Transform the message into a hash value using the MD5 algorithm.
  - Process the message through a series of rounds and operations to produce a fixed-size digest.

## 🚧 Project Constraints

- ⚠️ **Security Considerations**: While MD5 provides a quick hash function, its security limitations should be considered. The project demonstrates principles for educational purposes.

## 🚀 Usage Instructions

1. **Clone the Repository:**
   
    ```bash
    git clone https://github.com/taniafatmawati/dsa-md5-digital-signature.git
    cd dsa-md5-digital-signature
    ```

2. **Run the Signing Program:**
   
    ```bash
    python dss_signing.py
    ```

3. **Run the Verification Program:**
   
    ```bash
    python dss_verifying.py
    ```

4. **View Results:**

    The programs will display the digital signature for the input message and verification results.

## 📝 Algorithm and Implementation

### DSA Algorithm

- **Key Generation**:
  - Generate prime numbers `p` and `q` with the condition `(p-1) mod q = 0`.
  - Compute `g = h^((p-1)/q) mod p`, where `1 < h < p-1` and `h^((p-1)/q) mod p > 1`.
  - Select private key `x < q`.
  - Compute public key `y = g^x mod p`.

- **Message Hashing**:
  - Convert the message `M` to its hash value using MD5.
  - Perform padding and block processing to compute the message digest.

- **Signing**:
  - Generate a random integer `k < q`.
  - Compute signature values `r` and `s`.

- **Verification**:
  - Compute message digest and verify the signature using public key values.

### MD5 Hash Function

- Transform the message into a hash value using the MD5 algorithm.
- Process the message through a series of rounds and operations to produce a fixed-size digest.

## 📋 Result and Documentation

### 📄 Results

- **Signature Creation**: Successfully generated and verified digital signatures using DSA and MD5.
- **Performance Metrics**: The implementation demonstrates practical use of cryptographic principles with efficient performance for digital signatures.

### 📚 Documentation

Includes source code files, usage instructions, and additional details in this README.md.

## 📝 Conclusion

The integration of DSA and MD5 provides a robust framework for digital signatures, ensuring the integrity and authenticity of digital communications. This project offers practical implementation and insights into digital signatures.

## 🔗 Additional Notes

- Ensure to test the implementation thoroughly with different messages to verify correctness.
- Refer to DSA and MD5 specifications for detailed algorithm descriptions and implementations.
