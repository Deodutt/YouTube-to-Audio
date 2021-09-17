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

This application uses a simple way to convert Youtube videos to MP3 files. Get high-quality audio files such as 320kbps for any video on YouTube! Conversion time is mostly instant for hour-long videos. The purpose of this application is for educational purposes only!
<br/><br/>


#### Current Version

This current version uses an unofficial API (From https://www.yt2mp3.ws/developers/) to embed a download button onto a webpage. When on a webpage, the user will fill out a form (Enter a URL in the bar and press convert) and this will cause a POST request. Inside the code, if there is a post request and a variable called "youtube_link" it will run some code. It will get the information and strip it from white spaces. It will then call an id_grabber function that is inside the helper.py function and store that result to a variable called youtube_id. Inside the helper.py file, the program uses urllib module to parse through the URL and extract the youtube_id. It checks multiple cases of different ways users can enter a youtube URL. Once extracted, the value will be returned to the application.py file. The youtube ID is then concatenated with the provided API route. There is then a return with the render_template() function called. This function is used to generate output to an index.html file inside a templates folder based on Jinja2 engine. The passed variables are the HTML page and data values that will be used in the HMTL page.
<br/>

### Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
<br/><br/>


## Getting Started

To get a local copy up and running follow these simple steps.
<br/><br/>

1. Clone the repository and change directories into it
   ```sh
   git clone https://github.com/Deodutt/YouTube-to-Audio.git
   cd .\YouTube-to-Audio\
   ```

2. Create a virtual environment and activate it
   ```sh
   py -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required dependencies
   ```sh
   pip install -r requirements.txt
   ```

4. Run the flask application
   ```sh
   $env:FLASK_APP = "application.py"
   flask run
   ```

5. Go to the local callback IP on your browser
   ```sh
   http://127.0.0.1:5000/
   ```
   
<br/><br/>


## Version History

* 0.1
    * Initial Release
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

- [Sai Ho Yip - Debugging](https://www.linkedin.com/in/saihoyip/)
<br/><br/>

## Contact

[![Linkedin Badge](https://img.shields.io/badge/-Ricardo%20Deodutt-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rixardo/)](https://www.linkedin.com/in/rixardo/)   [![GitHub Badge](https://img.shields.io/badge/-Deodutt-black?style=flat-square&logo=GitHub&logoColor=white&link=https://www.github.com/Deodutt)](https://www.github.com/Deodutt)    [![Twitter Badge](https://img.shields.io/badge/-@RixardoDe-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://www.twitter.com/RixardoDe)](https://www.twitter.com/RixardoDe)
