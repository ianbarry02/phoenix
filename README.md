<!-- This README file was modified from the Best-README-Template created by othneildrew: https://github.com/othneildrew/Best-README-Template -->

<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="images/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Phoenix</h3>

  <p align="center">
    A module that converts course syllabi into website code with text accessibility tools.
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a> -->
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    &middot; -->
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <!-- <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul> -->
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Preparing Files</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Course syllabi contain important information that instructors want students to process. (And they take loads of time and energy to draw up!)

However, syllabi are often offered to students in a rigid format. The font, size, and color of syllabus text are just a few elements that might make digesting course syllabi challenging for students.

Phoenix is a tool that breaks down text and tables from a Word document, converts them to HTML code, and inserts that HTML code into a template. This template can be uploaded to GitHub and hosted as a website for free via GitHub Pages. Website users can change the font, text size, and text color of the syllabus.

This is a small step toward increasing accessibility of course syllabi. Phoenix was created and is maintained by a graduate student at a public university in the U.S. If you catch bugs or have suggestions for additional features to include in this tool, please see the links above to do so! Thank you for using my tool!

### Recently Resolved Issues (may still be buggy!)
* Toolbar now scales on mobile devices and minimized desktop windows
* Text scaling has a floor and ceiling

### Known Issues
* Final product not guaranteed to work on mobile devices or in older browsers
* Table headers lack distinctive styling

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- GETTING STARTED -->
## Getting Started

The instructions below will help you prepare to run Phoenix.

### Prerequisites

_Phoenix uses Python to run. The information below assumes Python is downloaded on your machine. If Python is not on your machine, please see [the Python download page](https://www.python.org/downloads/) for download instructions._

Phoenix uses the os, argparse, and Spire.Doc libraries in Python. os and argparse are included in the Python Standard Library and do not need to be installed independently. However, Spire.Doc is not included in the Standard Library and must be installed independently. To install Spire.Doc on your machine, run the following code in the terminal window:
  ```sh
  pip install spire-doc
  ```

### Preparing Files

To make sure Phoenix runs smoothly, please follow the file preparation instructions below.

First, prepare your syllabus in Word. Phoenix converts heading text, paragraph text, blank lines, and tables to HTML. Please check the following to make sure your Word doc is convertible:
<br>
* Make sure that your headings are styled as "Heading 1", "Heading 2", etc._
_* Style any "Title" elements as "Heading [X]" elements instead.
* Remove headers and footers. You can move information in headers and footers to the body of the document if you need them to be included in your syllabus site.
* Double check spacing. Phoenix uses Spire.Doc to render blank lines in Word documents as paragraphs, so blank lines will ultimately appear as blank lines on your website, too.

Next, download the [Phoenix files](https://github.com/ianbarry02/phoenix/tree/main/phoenix_files): [_phoenix.py](https://github.com/ianbarry02/phoenix/blob/main/phoenix_files/_phoenix.py) and [phoenix.py](https://github.com/ianbarry02/phoenix/blob/main/phoenix_files/phoenix.py). Store these files in a new folder on your machine.

Finally, download the [website files](https://github.com/ianbarry02/phoenix/tree/main/website_files): [index.html](https://github.com/ianbarry02/phoenix/blob/main/website_files/index.html) and [script.js](https://github.com/ianbarry02/phoenix/blob/main/website_files/script.js) from the Phoenix repository. Store these files in a new folder on your machine.
<br/>
<br/>
It can be helpful (but is not necessary) to copy your syllabus into the folder where index.html, script.js, and styles.css are stored.
<br/>
<br/>
Now you are ready to use Phoenix!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE INSTRUCTIONS -->
## Usage

Phoenix takes three arguments:
* doc — the path to your syllabus Word document
* folder — the path to the folder where index.html, script.js, and styles.css are stored
* title — the text that you want to be displayed on the tab in a browser window (course number, semester, and/or year might be useful information to include)
<br/>
First, open a terminal window and change your directory to the folder that contains the Phoenix files (_phoenix.py and phoenix.py):
<br/>

  ```sh
  cd [paste path to Phoenix files here]
  ```

<br/>
Next, modify the following command to include the paths to your Word document and folder as well as your desired title:
<br/>

  ```sh
    python phoenix.py -doc "[paste path to Word doc here]" -folder "[paste path to website files folder here]" -title "[insert title here]"
  ```
<br/>
Now, the index.html file you downloaded earlier will include the code parsed from your Word document and your desired title. To host your website with GitHub Pages, follow the instructions below:

1. Create a new GitHub repository. Make sure it is a public repository.
2. Upload your index.html and script.js files to the new repository.
3. Under the repository Settings (which you can navigate to using the bar at the top of the page), navigate to the "Pages" tab on the left.
4. Under the "Build and Deployment" heading, make sure "Source" is set to "Deploy from a branch" and "Branch" is set to "main". Click "Save".
5. It might take a few minutes for your site to be published. Refresh the page. Eventually, you will see a banner at the top that says, "Your site is live at ...". Click the link to view your site!
<br/>
You can insert the link to your site on your Canvas/online classroom page, at the top of your syllabus, or any other place you share resources with your students.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
<!-- ## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/othneildrew/Best-README-Template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=othneildrew/Best-README-Template" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Distributed under the Creative Commons Zero v1.0 Universal license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ian A. M. Barry: barry2em@dukes.jmu.edu

Project Link: [https://github.com/ianbarry02/phoenix](https://github.com/ianbarry02/phoenix)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Below are links to the resources that made this project possible.

* [Spire.Doc Documentation](https://www.e-iceblue.com/Introduce/doc-for-python.html?gad_source=1&gad_campaignid=53263203&gclid=Cj0KCQjwnJfEBhCzARIsAIMtfKI5GDKBcyfqUoF8Wd7wsZbGSIWttQE_exVYn5S5RIPLi4INBr0ZdYUaAmDOEALw_wcB)
* [Convert Word DOCX or DOC to HTML in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Conversion/Python-Convert-Word-to-HTML.html#3)
* [Extract Text from Word Documents with Python](https://medium.com/@alice.yang_10652/extract-text-from-word-documents-with-python-a-comprehensive-guide-95a67e23c35c)
* [Alice Yang's Word <-> HTML in Python Medium Guides](https://medium.com/@alice.yang_10652)
* [Python Forensics by Chet Hosmer](https://www.sciencedirect.com/book/9780124186767/python-forensics)
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com  -->
