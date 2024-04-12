### Updated README.md for the "V" Virus Program


# "V" Virus Program Analysis and Simulation

This repository hosts the "V" Virus Program, a Python-based simulation designed to demonstrate the behavior and propagation mechanics of a computer virus. This project is part of the CS361 Computer Security course at the Indian Institute of Information Technology, Guwahati.

## Project Overview

The "V" virus program is crafted to explore the functionalities of a typical file-infecting virus which targets files with specific extensions and propagates itself through removable media and across systems. This educational project aims to provide insight into the basic principles of malware operations and their implications, as well as to foster a deeper understanding of the importance of cybersecurity measures.

## Key Features

- **File Infection**: Automatically identifies and modifies `.foo` files within the user's document directory by appending malicious code.
- **Propagation via USB Drives**: Detects connected USB drives and replicates itself onto them, infecting `.foo` files found within.
- **Cross-Computer Infection**: Capable of spreading to new computers where the infected USB drives are connected.
- **Simulated Antivirus Interaction**: Documents the responses of antivirus software when interacting with the program.

## Repository Contents

- `V.py` - Main Python script for the "V" virus.
- `Report.docx` and `Report.pdf` - Comprehensive reports that detail the behavior, impact, and analysis of the "V" virus.
- `Assignment1_CS361.pdf` - Contains the project's assignment sheet and detailed requirements.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of Python and command-line operations.

### Setup

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/abhisheksingh789/assignment1-cs361.git
   cd assignment1-cs361
   ```

2. It is **highly recommended** to run this script in a controlled environment, such as a virtual machine or a sandbox, to prevent unintended side effects.

### Running the Program

To execute the "V" program, navigate to the repository's directory and run:
```
python V.py
```

## Safety and Legal Notice

This project is intended **strictly for educational purposes** and should not be used for illegal activities. The creators and contributors do not endorse misuse and will not be liable for any damages caused by the deployment or misuse of this software. Please adhere to your local laws and regulations regarding the use of such software.

## Contribution

**B.Tech CSE 3rd year**

- **Abhishek Kumar** - Development and Documentation
- **Harsh Rajput** - Code Review and Enhancements

## Acknowledgments

- **Rakesh Matam** - Course Instructor
- Faculty and peers at IIIT Guwahati for their support and feedback throughout the development of this project.

## License

This project is distributed under the MIT License. See the `LICENSE` file for more information (a LICENSE file should be included in your repository).
