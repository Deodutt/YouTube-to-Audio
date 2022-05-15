<!-- TABLE OF CONTENTS -->
<h1 align="center">Youtube to MP3 Converter</h1>

 <details style="display: inline-block" pen="open">
  <summary> Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#current-version">Current Version</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>
<br/>

## About The Project

This open source project is a simple way to convert Youtube videos to MP3 files. Get high-quality audio files such as 320kbps for any video on YouTube! Conversion time is almost instant for hour-long videos. The purpose of this application is for personal use only. Only download your own YouTube videos. This is for educational purposes only!
<br/><br/>

#### Current Version

Release 2.5 is has memory saving tactics implemented. In this version, old downloaded videos are deleted from the local workspace. Users will still have their downloaded version but will no long have it in the local file.
<br/>

### Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
- [Web Scraping](https://en.wikipedia.org/wiki/Web_scraping)
  <br/><br/>

## Getting Started

To get a local copy up and running follow these simple steps.
<br/><br/>

1. Clone the repository and change directories into it

   ```sh
   git clone https://github.com/Deodutt/YouTube-to-Audio.git
   cd YouTube-to-Audio\
   ```

2. Create a virtual environment and activate it. (Windows command)

   ```sh
   py -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required dependencies

   ```sh
   pip3 install git+https://github.com/pytube/pytube
   pip3 install -r requirements.txt
   ```

4. Run the flask application

   ```sh
   (for windows)
   $env:FLASK_APP = "application.py"
   flask run

   (for linux)
   export FLASK_APP=application.py
   flask run
   ```

5. Go to the local callback IP on your browser
   ```sh
   http://127.0.0.1:5000/
   ```

<br/><br/>

## Version History

- 2.5
  - Memory saving tactics have been deployed! This stable uses built in os module to remove old downloaded videos from the local directory
- 2.0
  - Stable and more secure version with pytube module to download videos. Uses web scrapping BS4 to obtain youtube video information
- 1.0 \* Initial Release with third party API
  <br/><br/>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
   <br/><br/>

## Acknowledgements

- [Sai Ho Yip - Troubleshooting & Advice](https://www.linkedin.com/in/saihoyip/)
  <br/><br/>

## Contact

[![Linkedin Badge](https://img.shields.io/badge/-Ricardo%20Deodutt-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rixardo/)](https://www.linkedin.com/in/rixardo/) [![GitHub Badge](https://img.shields.io/badge/-Deodutt-black?style=flat-square&logo=GitHub&logoColor=white&link=https://www.github.com/Deodutt)](https://www.github.com/Deodutt) [![Twitter Badge](https://img.shields.io/badge/-@RixardoDe-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://www.twitter.com/RixardoDe)](https://www.twitter.com/RixardoDe)
