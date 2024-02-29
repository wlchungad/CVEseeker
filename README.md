<h1>Seeker - The Automated CVE Reader</h1>
<h2>Description</h2>
<p>This is the repo of automation of GovCERT Security Alert Collector. <br>This project is written in python, which means it should be executed without the need of other extra software such as chromedriver.</p>
<h2>Why this project?</h2>
<ul>
  <li>to simplify work and minimize error by human factor</li>
  <li>to free manpower from repetitive checking</li>
  <li>to experiment with multi-module python development</li>
</ul>
<p>Other than "train myself", the background of the project is quite unique (usage-specific and region-specific), meaning that I cannot just <code>git clone</code> some projects and call it a day.</p>

<h2>Prerequisites:</h2>
<ol>
  <li>
    <p>Install Python 3 (3.10+ recommended) and pip</p>
  </li>
  <li>
    <p>Install browser (Firefox/Chrome)</p>
  </li>
  <li>
    <p>Install the required modules:</p>
    <table>
      <tr>
        <th>Module used</th>
        <th>Usage</th>
      </tr>
      <tr>
        <td>selenium</td>
        <td>scrapping dynamic websites that requires interaction<br><i>e.g. Microsoft Update Catalog</i></td>
      </tr>
      <tr>
        <td>openpyxl</td>
        <td>handling excel and csv files</td>
      </tr>
      <tr>
        <td><s>validators</s></td>
        <td><s>validating if URL is reachable</s></td>
      </tr>
      <tr>
        <td>tqdm</td>
        <td>showing progress bar</td>
      </tr>
      <tr>
        <td>request</td>
        <td>getting static HTML content</td>
      </tr>
      <tr>
        <td>BeautifulSoup</td>
        <td>extracting information from webpage</td>
      </tr>
      <tr>
        <td>virtualenv</td>
        <td>(Optional)<br>creating virtual environment</td>
      </tr>
    </table>   
  </li>
</ol>
<p>Module "virtualenv" is <b>not</b> in requirement.txt. You can always <code>pip install</code> if you prefer to do so.</p>

```
pip install -r requirements.txt
```

<h2>How to use:</h2>
<ol>
  <li>Start python with anaconda / python console</li>
  <li>Run the python file in CMD</li>
<h3>CMD:</h3>

```console
cd /d "<path/to/folder>"
python main.py
```

  <li>Input the link, and let python do the job for you</li>
</ol>
<p><b>Link format:</b> https://www.govcert.gov.hk/en/alerts_detail.php?id=xxxx</p>
<h3>Happy <s>crawling</s> scrapping!</h3>

<h1>v1.0</h1>
<p>The first build is just a self-challenge and a "support tool" for work.</p>

<h1>v2.0</h1>
<p>To comply with migration from cve.mitre.org to cve.org, a new version is made. <br>
You can refer to <a href="/blob/main/modules/CVEDownloader2.py">CVEDownloader2.py</a> for updates.</p>


<h3>v2.1 (<i>"headless"</i>)</h3>
<p>With FirefoxProfile updated, now the service can scrap sliently without the big Firefox window.</p>

<h1>v3.0?</h1>
<p>BeautifulSoup is better for static scrapping. However selenium is still needed for some major tasks, such as interactive downloads.
I may sync this version to main-branch.</p>

<h1>Note:</h1>
<ol>
  <li>
    <p>I will update the system should there be any impactful changes in source websites.</p>
  </li>
  <li>
    <p>For those who:
      <ul>
        <li>do not want to tackle the hassle of installation, configuration, etc...</li>
        <li>cannot install python and modules due to security/network limitation</li>
      </ul>
      <p>Please go to the <a href="https://github.com/wlchungad/CVEseeker/tree/APP-development">APP</a> version. The source code is as same as main branch (here). <b>Please note that the APP branch might be delayed.</b> </p>
    </p>
  </li>
  <li>
    <p>Using venv is a recommended approach. You can copy this code and make a <code>start.bat</code> at wherever you clone this project.</p>

```console
python -m venv env
call "env/Scripts/activate.bat"
pip install -r requirements.txt
python main.py
```
  </li>
</ol>

<h1>Acknowledgments:</h1>
<ul>
  <li>
    Geckodriver: <a>https://github.com/mozilla/geckodriver/releases/tag/v0.33.0</a>
  </li>
</ul>