import os,re
try:
    import idna
except:
    os.system("pip install idna")
    os.system("pip install dnstwist[full]")
    import idna
try:
    from fpdf import FPDF
except:
    os.system("pip install fpdf")
    from fpdf import FPDF
import subprocess
import glob
import csv
try:
    from fuzzywuzzy import fuzz
except:
    os.system("pip install fuzzywuzzy")
    os.system("pip install python-Levenshtein")
    from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
'''
run "pip install fpdf" to install the PDF library that generates the pdf file.
'''
class Permutation():
    def __init__(self):
        self.images = []
        self.pdf = FPDF()
        self.logo=None
        self.fuzz_output = list()
        self.business_name = 'Google '
        self.customer_name = 'John'
        self.business_address = '123 street'
        self.customer_phone = '123456'
        self.customer_email = 'abc@gmail.com'
        self.brands_count = 0
        self.brands = []
        self.pun_codes = []
        self.show_menu()
        self.createPDF_And_CSV()

    def show_menu(self):
        count=1
        txt_files = []
        txt_file = ""
        for filename in glob.glob(os.getcwd() + '/*.txt'):
            print(str(count) + ' ' + str(os.path.basename(filename)))
            txt_files.append(filename)
            count = count + 1
        print("filenames: ",txt_files)
#        index = int(input('Select text File : '))
 #       print(txt_files[index-1])
#        file1 = open(txt_files[index-1], 'r')
        file1 = open("input.txt", 'r')

        Lines = file1.readlines()
        linesq = []
        for line in Lines:
            linesq.append(line.strip('\n'))
            print(line.strip())
        print(len(Lines))



 #       self.logo = self.images[index - 1]

        self.fuzz_output = list()
#        self.business_name = input('Enter the business name: ')
 #       self.customer_name = input('Enter the customer name: ')
  #      self.business_address = input('Enter the business address: ')
   #     self.customer_phone = input('Enter the customer phone number: ')
    #    self.customer_email = input('Enter the customer email: ')
        self.brands_count = len(Lines)
        self.brands = []
        self.brands = linesq
        print(linesq)
        countt = 0
        for i in range(self.brands_count):
            getOutput = self.get_formatted_output(self.fuzz_dns(self.brands[i]),self.brands[i])
            self.fuzz_output.append((self.brands[i], getOutput))

        get_csv_output = self.get_formatted_output_csv(getOutput)
        with open("twist.csv", 'w', encoding="utf-8",newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(get_csv_output)

    def fuzz_dns(self, url):
        result = subprocess.run(f'dnstwist {url}', stdout=subprocess.PIPE)
        data = result.stdout.decode('utf-8')
        print("99999999999999")
        print(data)
        print(type(data))
        print("99999999999999")

        return data

    def remove_url_extension(self, url):
        return url.replace('.com', '')

    def get_formatted_output(self, dns_output,chickw):
        temp = dns_output.split('\n')
        L = ""
        check = True

        for each in temp:
            x = each.split(' ')
            x = ' '.join(x).split()
            if len(x) > 0:
  #              print("x1", x[1])
                t = re.findall("original",x[0])
                if(len(t)>0):
                    check = False
                if(check):
                    continue
                ratio = fuzz.ratio(chickw,x[1])
                ratio = ratio / 10
                try:
                    pun_code = idna.encode(self.remove_url_extension(x[1]))
                    print("pun_code :",x, " : ",pun_code)
                    print(type(pun_code))
                except:
                    pun_code = "...."
                temp_str = x[0] + ' ' + self.remove_url_extension(x[1]) + ' '+ str(ratio) +' '+ str(pun_code) + '\n'
                L += temp_str
        return L

    def get_formatted_output_csv(self, dns_output):
        main_list = []
        temp = dns_output.split('\n')
        print("....................................temp")
        print(dns_output)
        print("....................................temp1")
        print(temp)
        for te in temp:
            sublist = []
            temp1 = te.split(' ')
            for tu in temp1:
                sublist.append(tu)
            main_list.append(sublist)
        print("0000000000000000000000000000000000000")
        print(main_list)
        return main_list

    def createPDF_And_CSV(self):
        for brand in self.fuzz_output:
            rows=[]
            for brandData in str(brand[1]).split('\n'):
                row = []
                row.append(brandData)
                rows.append(row)
                # brandData = brandData[: -1]
   #             self.pdf.cell(200, 10, txt=brandData, ln=1, align='C')
            print("rows: ",rows)
            rows1 = []
            for row in rows:
                row = row[0].split(" ")
                rows1.append(row)
                print(row)
            rows = rows1
            print("rows   : ",rows)

            with open(self.remove_url_extension(brand[0]) + '.csv', 'w', newline='', encoding='utf-8') as f:
                write = csv.writer(f)
                write.writerows(rows)
                f.close()
permutation = Permutation()
print('Done!!')