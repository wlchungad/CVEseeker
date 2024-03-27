<h1>Seeker - The Automated CVE Reader</h1>
<h2>Description</h2>
<p>This is the repo of automation of GovCERT Security Alert Collector. This project is specifically working for <a>www.govcert.com.hk</a> and <a>cve.org</a>.<br>This project is written in python, and I will try to reduce dependency, so that it can be executed without the need of other extra software such as chromedriver.</p>
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

<h2>v1.0</h2>
<p>The first build is just a self-challenge and works as a "support tool".</p>

<h2>v2.x</h2>
<h3>v2.0</h3>
<p>To comply with migration from cve.mitre.org to cve.org, a new version is made. <br>
You can refer to <a href="/blob/main/modules/CVEDownloader2.py">CVEDownloader2.py</a> for updates.</p>


<h3>v2.1 (<i>"headless"</i>)</h3>
<p>With FirefoxProfile updated, now the service can scrap sliently without the big Firefox window.</p>

<h3>v2.2</h3>
<p>This version works more specifically for personal usage.<br>
Also, to comply with changes of developing environment, vituralenv is employed.</p>

<h3>v2.3</h3>
<p>Now it allows customization by changing the <code>conf</code> folder to include/exclude CVEs to be recorded.</p>

<h3>v2.4</h3>
<p>Due to the change of URL used by GovLink, requestLink module is update to accommodate this issue.</p>

<h2>v3.0 update?</h2>
<p>BeautifulSoup is better for static scrapping. However selenium is still needed for some major tasks, such as interactive downloads.</p>

<h2>Note:</h2>
<ol>
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
    <p>Using venv is a recommended approach. You can download the <code>bat</code> file, or copy the following code and make your <code>start.bat</code> at wherever this project is cloned to.</p>

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