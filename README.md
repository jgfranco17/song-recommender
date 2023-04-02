<h1 align="center">Spotify Song Recommender</h1>

<div align="center">

![STATUS](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge) ![LICENSE](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

</div>

---

## Table of Contents
* [About](#about)
* [Getting Started](#getting_started)
* [Usage](#usage)
* [Authors](#authors)

## 🔎 About <a name="about"></a>

This project aims to create a song-recommendation API for users to help them pick songs.

## 🏁 Getting Started <a name="getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following must be installed on the host machine:

- [Python 3.9](https://github.com/pyenv/pyenv) or above

It is highly recommended to use `pyenv` to manage Python versions. This project is built in Ubuntu 22.04, but should also work on MacOS, as well as other Linux distros.

### Installing

To get started with this project, clone the repository to your local machine and install the required dependencies.

```bash
git clone https://github.com/jgfranco17/song-recommender.git
cd song-requirements
pip install -r requirements.txt
```

In order to support Spotipy's authentication, set the following environment variables:
```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

## 🚀 Usage <a name="usage"></a>

Once the work is ready for use, the instructions will be updated here.

## ✒️ Authors <a name="authors"></a>

- [Chino Franco](https://github.com/jgfranco17)