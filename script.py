import pdfkit, os
from bs4 import BeautifulSoup

directory = 'Test Results_files'
filename_base = 'QuestionFeedback'
path_to_wkhtmltopdf = './wkhtmltopdf/bin/wkhtmltopdf.exe'

filename_output = 'AEM_SitesDeveloperExpert.pdf'

question = 0
path_to_file = []

for filename in os.listdir(directory):
    if filename_base in filename:
        file_path = os.path.join(directory, filename)

        
        file = open(file_path, 'r')

        file_partial = BeautifulSoup(file, 'html.parser')

        for one_div in file_partial.find_all('div', {'class': 'multipleChoiceButton'}):
            feedbackCorrect_i = one_div.find('i', {'class': 'feedbackCorrect'})

            try:
                if 'block' in feedbackCorrect_i.attrs['style']:
                    one_div.attrs['style'] += '; background-color: rgb(0, 128, 0); color: rgb(255, 255, 255)'
            
            except:
                no = 1

        question += 1

        #file_content = '<h2 style="color: #fff; background-color: #000; ">Q' +  str(question) + '</h2>' + str(file_partial.find(id={'FeedbackDiv'}))
        file_content = '<h2 style="color: #fff; background-color: #000; ">Q' +  str(question) + '</h2>' + str(file_partial)

        file_content = file_content.replace(' background-color: rgb(201, 80, 73); color: rgb(255, 255, 255);','')
        file_content = file_content.replace(' multipleChoiceButtonClicked','')
        
        f = open(file_path, 'w')
        f.write(file_content)
        f.close()

        path_to_file.append(file_path)

config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

options = {
    'page-size': 'A4',
    'orientation': 'Portrait',
    'encoding': 'UTF-8',
    'zoom': 1,
    'margin-top': '0.2in',
    'margin-right': '0.3in',
    'margin-bottom': '0.1in',
    'margin-left': '0.3in',
}

pdfkit.from_file(path_to_file, output_path=filename_output, configuration=config, options=options)