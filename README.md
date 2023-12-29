<h1>Seeker</h1>
<h2>Description</h2>
<p>This is the repo of automation of GovCERT Security Alert Collector. <br>This project is written in python, which means it should be executed without the need of other extra software such as chromedriver.</p>
<h2>Why this project?</h2>
<ul>
  <li>to simplify work and minimize error by human factor</li>
  <li>to free manpower from repetitive checking</li>
  <li>to train myself with multi-module python development</li>
</ul>

<h2>Prerequisites:</h2>
<ol>
  <li>
    <p>Install Python 3 (3.9+ recommended) and pip</p>
  </li>
  <li>
    <p>Install the required modules:</p>
    <!-- module and usage -->
    <ul>
      <li>selenium</li>
      <li>openpyxl</li>
      <li>validators</li>
      <li>tqdm</li>
    </ul>   
  </li>
</ol>

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
<h4>Link format:</h4> 
<p>https://www.govcert.gov.hk/en/alerts_detail.php?id=xxxx</p>
<h3>Happy <s>crawling</s> scrapping!</h3>

<h1>v1.0</h1>
<p>The first build is just a self-challenge and a "support tool" for work.</p>

<h1>v2.0</h1>
<p>To comply with migration from cve.mitre.org to cve.org, a new version is made. <br>
You can refer to <a href="/blob/main/modules/CVEDownloader2.py">CVEDownloader2.py</a> for updates.</p>


<h1>v2.1 (<i>"headless"</i>)</h1>
<p>With FirefoxProfile updated, now the service can scrap sliently without the big Firefox window.</p>

<h1>Note:</h1>
<ol>
  <li>
    <p>I will update the system should there be any impactful changes in source websites.</p>
  </li>
  <li>
    <p>For those who:
      <ul>
        <li>do not want to tackle the hassle of installation, configuration, etc...</li>
        <li>cannot install python and modules due to security</li>
      </ul>
      <p>Please go to the <a href="https://github.com/wlchungad/CVEseeker/tree/APP-development">APP</a> version. The source code are, will be, and should be the same.<br>Please note that the update time of APP branch might be delayed. </p>
    </p>
  </li>
</ol>

<h1>Acknowledgments:</h1>
<ul>
  <li>
    Geckodriver: <a>https://github.com/mozilla/geckodriver/releases/tag/v0.33.0</a>
  </li>
</ul>