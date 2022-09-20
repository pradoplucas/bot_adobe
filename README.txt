Needed:
- Python;
- Beautiful Soup: pip install beautifulsoup4;
- pdfkit: pip install pdfkit.

Steps:
1. Open the https://www.certmetrics.com/adobe/;
2. Go to "Test Results" page;
3. Open the console (F12);
4. Paste the following code and press Enter:

var intervalTime = 500, question = 0;
let questionInterval = setInterval(() => {
	try {
		document.getElementById("reviewSelectedQuestionButton_" + question).click();
		question++;
	}
	catch(err) {clearInterval(questionInterval);}
}, intervalTime);

5. After the script is finished, save the page in the same folder as the "script.py" file;
6. Execute the "script.py" file;
6. It will be generated a ".pdf" file.