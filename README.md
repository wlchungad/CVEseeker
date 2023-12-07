<h1>Seeker</h1>
<h2>Description</h2>
<p>This is the repo of automation of GovCERT Security Alert Collector. <br>This project is written in python, without the need of other extra software such as chromedriver.</p>
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
    <ul>
      <li>selenium</li>
      <li>openpyxl</li>
      <li>validators</li>
    </ul>   
  </li>
</ol>

```
pip install -r requirements.txt
```

<h2>How to use:</h2>
<ol>
  <li>Start python with anaconda / python console</li>
  <li>Run the python file</li>
<h3>CMD:</h3>

```console
cd /d <path/to/folder>
python main.py
```

  <li>Input the link, and let python do the job for you</li>
</ol> 
<p>Link format: https://www.govcert.gov.hk/en/alerts_detail.php?id=xxxx</p>

<h1>v2.0</h1>
<p>To comply with migration from cve.mitre.org to cve.org, A new version will be purposed.</p>

---

<h2>Future:</h2>
<p>I will update the system should there be any impactful changes.</p>

<h2>Note:</h2>
<p>For those who:</p>
<ul>
  <li>do not want to tackle the hassle of installation, configuration, etc...</li>
  <li>cannot install python and modules due to security</li>
</ul>
<p>Please go to the <a href="https://github.com/wlchungad/CVEseeker/tree/APP-development">APP</a> version. The source code are, will be, and should be the same.<br>Please note that the update time of APP branch might be delayed. </p>
