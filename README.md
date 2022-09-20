[Link to Video Tutorial on Google Drive](https://drive.google.com/file/d/15UfrifvAaXTU2PCWBU5DWMH07y8Vg-gG/view?usp=sharing)

## Needed:
- [Python](https://www.python.org/downloads/);

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/): `pip install beautifulsoup4`

- [pdfkit](https://pypi.org/project/pdfkit/): `pip install pdfkit`

## Steps:
1. Open the [Adobe Certmetrics](https://www.certmetrics.com/adobe/);
2. Go to "**Test Results**" page;
3. Open the console (F12);
4. Paste the following code and press Enter:

```
var intervalTime = 500, question = 0;
let questionInterval = setInterval(() => {
	try {
		document.getElementById("reviewSelectedQuestionButton_" + question).click();
		question++;
	}
	catch(err) {clearInterval(questionInterval);}
}, intervalTime);
```

5. After the script is finished, save the page in the same folder as the "**script.py**" file;
6. Execute the "**script.py**" file;
6. It will be generated a "**.pdf**" file.