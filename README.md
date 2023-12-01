# UnityUtopia - Chatting Web Application with Abusive Word Sensing


## Overview

UnityUtopia is a web application built using Django that provides users with a chatting platform. It incorporates real-time chat functionality with integrated web sockets for a seamless communication experience. Additionally, the application includes an abusive word sensing ML model to maintain a respectful and safe environment for users.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Abusive Word Sensing](#abusive-word-sensing)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Real-time Chatting**: Users can engage in real-time chat with each other.
- **Web Socket Integration**: Integrated web sockets for instant message delivery.
- **Abusive Word Sensing**: Utilizes an ML model to detect and filter abusive language.



## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Django
- Any other specific prerequisites...

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/unity-utopia.git
cd unity-utopia
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Migrate the database:

```bash
python manage.py migrate
```

## Usage

1. Run the development server:

```bash
python manage.py runserver
```

2. Open [http://localhost:8000](http://localhost:8000) in your browser.

3. Explore the chat functionality and experience the real-time communication.

## Abusive Word Sensing

The application uses the [LINGUISTIC-SENSITIVITY-UPGRADE](https://github.com/DanielDominicSavioKennedy/LINGUISTIC-SENSITIVITY-UPGRADE) repository's ML model for abusive word sensing. Make sure to follow the instructions in that repository for model setup and integration.

## Technologies

- **Django**: [Link to Django Documentation](https://docs.djangoproject.com/)
- **Web Sockets**: [Link to Django Channels Documentation](https://channels.readthedocs.io/)
- **Abusive Word Sensing Model**: [LINGUISTIC-SENSITIVITY-UPGRADE](https://github.com/DanielDominicSavioKennedy/LINGUISTIC-SENSITIVITY-UPGRADE)

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) before making any pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
